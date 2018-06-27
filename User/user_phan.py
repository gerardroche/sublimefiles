# When you see something you like and would like to use it, open an issue about
# abstracting it out into a reusable package, possibly installable via Package
# Control.

import os

import sublime_plugin


_DEBUG = True


def debug_msg(*msg):
    if _DEBUG:
        print('Phan:', *msg)


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

    candidate_file_names = ['.phan']
    for folder in ancestor_folders:
        for file_name in candidate_file_names:
            file = os.path.join(folder, file_name)
            if os.path.isdir(file):
                return os.path.dirname(file)

    return None


class PhanCheckCommand(sublime_plugin.WindowCommand):

    def run(self):
        view = self.window.active_view()
        debug_msg('view =', view.id(), view.file_name())

        file = view.file_name()
        if not file:
            raise RuntimeError('file name not found')

        working_dir = _find_working_dir(file, self.window.folders())
        if not working_dir:
            raise RuntimeError('working directory not found')

        debug_msg('working dir =', working_dir)

        env = {}
        cmd = [_expand_variables('~/.config/composer/vendor/bin/phan')]

        debug_msg('env =', env)
        debug_msg('cmd =', cmd)

        self.window.run_command('exec', {
            'env': env,
            'cmd': cmd,
            # 'file_regex': '(\\/[a-zA-Z0-9 \\.\\/_-]+)(?: on line |\\:)([0-9]+)',
            'file_regex': '^([a-zA-Z0-9][a-zA-Z0-9 \\.\\/_-]+):([0-9]+)',
            'quiet': not _DEBUG,
            'shell': False,
            'syntax': 'Packages/User/phan.sublime-syntax',
            'word_wrap': False,
            'working_dir': working_dir
        })
