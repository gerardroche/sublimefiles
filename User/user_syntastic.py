import os

import sublime_plugin


_DEBUG = False


def debug_msg(*msg):
    if _DEBUG:
        print('Syntastic:', *msg)


def _check(window, view, action='file'):
    if action not in ('file', 'project'):
        raise RuntimeError('unknown action')

    file_name = view.file_name()
    debug_msg('file =', file_name)
    if not file_name:
        raise RuntimeError('file name not found')

    file_type = os.path.splitext(file_name)[1][1:]
    if not file_type:
        raise RuntimeError('file type not found')

    working_dir = _find_working_dir(file_name, window.folders())
    debug_msg('dir =', working_dir)
    if not working_dir:
        raise RuntimeError('working directory not found')

    env = {}

    if file_type == 'php':

        # php/php

        if action == 'file':
            cmd = _build_cmd(view, 'php', 'php')
        elif action == 'project':
            raise RuntimeError('project linting is not supported by php/php linter')

        file_regex = '(\\/[a-zA-Z0-9 \\.\\/_-]+)(?: on line |\\:)([0-9]+)'

    elif file_type == 'py':

        # python/flake8

        if action == 'file':
            cmd = _build_cmd(view, 'python', 'flake8')
        elif action == 'project':
            cmd = _build_cmd(view, 'python', 'flake8', include_file_name=False)

        file_regex = '^([^:]+):([0-9]+):([0-9]+):'

    else:
        raise ValueError('unknown checker')

    debug_msg('env =', env)
    debug_msg('cmd =', cmd)

    window.run_command('exec', {
        'env': env,
        'cmd': cmd,
        'file_regex': file_regex,
        'quiet': not _DEBUG,
        'shell': False,
        'syntax': 'Packages/User/syntastic.sublime-syntax',
        'word_wrap': False,
        'working_dir': working_dir
    })


_checkers = {
    'php/php': {
        'args': ['-d', 'error_reporting=E_ALL'],
        'args_after': [
            '-l',
            '-d', 'error_logs=',
            '-d', 'display_errors=1',
            '-d', 'log_errors=0',
            '-d', 'xdebug.cli_color=0'
        ]
    },
    'python/flake8': {}
}


def _build_cmd(view, file_type, name, include_file_name=True):
    # The function returns a build cmd of the form <exe> <args> <file_name>
    # <post_args> <tail>. Each <option> consist actually of <option_before>
    # <option> <option_after>, but we omitted <option_before> and <option_after>
    # for clarity.

    defaults = _checkers[file_type + '/' + name]
    settings = view.settings()
    setting_key_prefix = 'syntastic_' + file_type + '_' + name + '_'

    def _opt(name, default=None):
        ret = []
        if name + '_before' in defaults:
            ret.extend(defaults[name + '_before'])

        value = settings.get(setting_key_prefix + name)
        if value:
            if isinstance(value, str):
                ret.append(value)
            else:
                ret.extend(value)
        elif name in defaults:
            ret.extend(defaults[name])
        elif default is not None:
            if isinstance(default, str):
                ret.append(default)
            else:
                ret.extend(default)

        if name + '_after' in defaults:
            ret.extend(defaults[name + '_after'])

        return ret

    cmd = []
    cmd.extend(map(_expand_variables, _opt('exec', name)))
    cmd.extend(_opt('args'))

    if include_file_name:
        cmd.extend(_opt('file_name', view.file_name()))

    cmd.extend(_opt('post_args'))
    cmd.extend(_opt('tail'))

    return cmd


def _expand_variables(path):
    path = os.path.expanduser(path)
    path = os.path.expandvars(path)

    return path


def _find_working_dir(file_name, folders):
    if file_name is None:
        return None

    if not isinstance(file_name, str):
        return None

    if not len(file_name) > 0:
        return None

    if folders is None:
        return None

    if not isinstance(folders, list):
        return None

    if not len(folders) > 0:
        return None

    ancestor_folders = []
    common_prefix = os.path.commonprefix(folders)
    parent = os.path.dirname(file_name)
    while parent not in ancestor_folders and parent.startswith(common_prefix):
        ancestor_folders.append(parent)
        parent = os.path.dirname(parent)

    ancestor_folders.sort(reverse=True)

    candidate_file_names = ['.flake8', 'phpunit.xml', 'phpunit.xml.dist']
    for folder in ancestor_folders:
        debug_msg('  looking for working directory at', folder, '...')
        for file_name in candidate_file_names:
            file = os.path.join(folder, file_name)
            debug_msg('    looking for ', file, '...')
            if os.path.isfile(file):
                debug_msg('  found working directory at', file)
                return os.path.dirname(file)

    return None


class SyntasticCheckCommand(sublime_plugin.TextCommand):

    # ==============================================================================
    # Syntastic              Syntax checking on the fly has never been so pimp.
    #
    #                 It's a bird! It's a plane! ZOMG It's ...
    #
    #                _____             __             __  _
    #               / ___/__  ______  / /_____ ______/ /_(_)____
    #               \__ \/ / / / __ \/ __/ __ `/ ___/ __/ / ___/
    #              ___/ / /_/ / / / / /_/ /_/ (__  ) /_/ / /__
    #             /____/\__, /_/ /_/\__/\__,_/____/\__/_/\___/
    #                  /____/
    #
    # ------------------------------------------------------------------------------
    # Quick start
    #
    # Setup a keybinding (Menu - Preferences - Key Bindings): >
    #
    #   [
    #       { "keys": ["ctrl+l"], "command": "syntastic_check"}
    #   ]
    #
    # ------------------------------------------------------------------------------
    # Choosing the executable
    #
    # The executable run by a checker is normally defined automatically, when
    # the checker is registered. You can however override it, by setting
    # 'syntastic_<filetype>_<checker>_exec' (Menu - Preferences - Settings): >
    #
    #   {
    #       "syntastic_python_flake8_exec": "~/.local/bin/flake8"
    #   }
    #
    # It can be set at project-level too (Menu - Project - Edit Project): >
    #
    #   {
    #       "settings": {
    #           "syntastic_php_php_exec": "~/.phpenv/versions/7.x/bin/php"
    #       }
    #   }

    def run(self, edit, **kwargs):
        window = self.view.window()
        if not window:
            raise ValueError('window not found')

        debug_msg('check', kwargs, 'buffer', self.view.id(),
                  self.view.file_name() if self.view.file_name() else '',
                  'in window', window.id())

        _check(window, self.view, **kwargs)
