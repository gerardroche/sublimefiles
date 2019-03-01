# When you see something you like and would like to use it, open an issue about
# abstracting it out into a reusable package, possibly installable via Package
# Control.

import functools
import logging
import os
import re

from sublime import load_resource
from sublime import load_settings
from sublime import packages_path
from sublime import save_settings
from sublime import set_timeout_async
import sublime_plugin


def _log_level_file():
    return os.path.join(packages_path(), 'User', '.neovintageous_log_level')


def _set_logger_log_level(level):
        level = level.strip().upper()

        valid_levels = [
            'CRITICAL',  # 50
            'ERROR',  # 40
            'WARNING',  # 30
            'INFO',  # 20
            'DEBUG',  # 10
            'NOTSET',  # 0
        ]

        if level not in valid_levels:
            raise ValueError('invalid log level')

        logging.getLogger('NeoVintageous').setLevel(getattr(
            logging,
            level,
            logging.DEBUG
        ))

        print('NeoVintageous: log level {}'.format(level))


def plugin_loaded():
    if bool(os.getenv('SUBLIME_NEOVINTAGEOUS_DEBUG')):
        log_level_file = _log_level_file()
        if os.path.isfile(log_level_file):
            with open(log_level_file, encoding='utf8') as f:
                _set_logger_log_level(f.read().strip().upper())


class NeovintageousDevCommand(sublime_plugin.WindowCommand):

    def run(self, action):
        action_method = getattr(self, action + '_action', None)
        if action_method:
            print('NeoVintageous: ', action.replace('_', ' '))
            action_method()
        else:
            raise Exception('action not found')

    def edit_help_file_action(self):
        docs_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'NeoVintageous/res/doc')

        resources = []
        for f in os.listdir(docs_path):
            if f.endswith('.txt'):
                resource = 'res/doc/%s' % f
                resources.append([f, resource])

        def on_done(index=-1):
            if index == -1:
                return

            resource = resources[index][1]

            view = self.window.open_file(os.path.join(packages_path(), 'NeoVintageous', resource))
            view.assign_syntax('Packages/NeoVintageous/res/Help.sublime-syntax')
            view.settings().set('indent_guide_options', [])
            view.settings().set('spell_check', True)
            view.settings().set('wrap_width', 78)

        self.window.show_quick_panel(resources, on_done)

    def fixup_docs_action(self):
        docs_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'NeoVintageous/res/doc')

        def set_utf8_encoding_save_and_close(view):
            view.run_command('set_encoding', {'encoding': 'utf-8'})
            view.run_command('save')
            view.close()

        for f in os.listdir(docs_path):
            if f.endswith('.txt'):
                resource = 'Packages/NeoVintageous/res/doc/%s' % f

                try:
                    load_resource(resource)
                except Exception as e:
                    print('  Error: ' + resource + ' ' + str(e))

                    file = packages_path() + '/NeoVintageous/res/doc/%s' % f
                    print('    Fixing resource encoding for \'{}\''.format(file))

                    view = self.window.open_file(file)

                    set_timeout_async(functools.partial(set_utf8_encoding_save_and_close, view), 200)

    def set_log_level_action(self):
        log_levels = [
            'CRITICAL',  # 50
            'ERROR',  # 40
            'WARNING',  # 30
            'INFO',  # 20
            'DEBUG',  # 10
            'NOTSET',  # 0
        ]

        def on_done(index):
            if index == -1:
                return

            log_level = log_levels[index].strip().upper()
            _set_logger_log_level(log_level)
            with open(_log_level_file(), 'w+', encoding='utf8') as f:
                f.write(log_level)

        self.window.show_quick_panel(log_levels, on_done)

    def dump_ex_completions_action(self):
        # Temporary hacky command to generate ex completions

        from NeoVintageous.nv import ex_routes

        routes = [r for r in ex_routes.ex_routes]

        print('')
        print('')
        print('')

        completions = []
        for route in routes:
            # print('route      =', route)
            completion = route
            completion = completion.replace('\\s', '')
            completion = completion.replace('^a', '')
            completion = completion.replace('^d', '')

            completion = re.sub('[^a-zA-Z\\|]', '', completion)
            completion = completion.strip('|')
            if not completion:
                print('completion not found in {}'.format(route))
                continue

            comps = completion.split('|')
            if len(comps) > 1:

                if comps == ['set', 's']:
                    completions.append('set')
                    print('completion {:>20} from {}'.format('set', route))
                else:

                    for comp in comps:
                        completions.append(comp)
                        print('completion {:>20} from {}'.format(comp, route))
            else:

                if completion == 'regead':
                    completion = 'read'

                if completion == 'registersaz':
                    completion = 'registers'

                if completion == 'qauit':
                    completion = 'quit'

                if completion == 'wqzAZ':
                    completion = 'wq'

                completions.append(completion)
                print('completion {:>20} from {}'.format(completion, route))

        print('')
        print("'" + "', '".join(completions) + "'")
        print('')


class NeovintageousDevDumpViewCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        settings = view.settings()

        print('>>> Neointageous: view')

        print('{} [id={}, file={}]'
              '\n buffer_id={: <10}        is_valid={: <10}     is_primary={: <10}   name={: <5}'
              '\n is_dirty={: <10}         is_read_only={: <10} is_scratch={: <10}   encoding={: <5}'
              '\n line_endings={: <10}     is_in_edit={: <10}   change_count={: <10} is_loading={: <5}'
              '\n line_height={: <10}      em_width={: <10}     is_popup_visible={: <10}'
              '\n overwrite_status={: <10} size={: <10}         is_auto_complete_visible={: <10}'
              '\n has_non_empty_selection_region={: <10}'
              .format(
                  str(view),
                  str(view.id()), str(view.file_name()),
                  str(view.buffer_id()), str(view.is_valid()), str(view.is_primary()), str(view.name()),
                  str(view.is_dirty()), str(view.is_read_only()), str(view.is_scratch()), str(view.encoding()),
                  str(view.line_endings()), str(view.is_in_edit()), str(view.change_count()), str(view.is_loading()),
                  str(view.line_height()), str(view.em_width()), str(view.is_popup_visible()),
                  str(view.overwrite_status()), str(view.size()), str(view.is_auto_complete_visible()),
                  str(view.has_non_empty_selection_region())))

        keys = [
            'action',
            'action_count',
            'autoindent',
            'cmdline_cd',
            'cmdline_mode',
            'command_mode',
            'data',
            'editor_setting',
            'external_disable',
            'external_disable_keys',
            'glue_until_normal_mode',
            'hlsearch',
            'ignorecase',
            'incsearch',
            'inverse_caret_state',
            'last_buffer_search',
            'last_buffer_search_command',
            'last_char_search_command',
            'last_character_search',
            'linux_shell',
            'linux_terminal',
            'magic',
            'mode',
            'motion',
            'motion_count',
            'must_capture_register_name',
            'non_interactive',
            'normal_insert_count',
            'osx_shell',
            'osx_terminal',
            'partial_sequence',
            'processing_notation',
            'recording',
            'register',
            'repeat_data',
            'reset_during_init',
            'rulers',
            'sequence',
            'showsidebar',
            'surround',
            'surround_spaces',
            'use_ctrl_keys',
            'use_sys_clipboard',
            'vi_editor_setting',
            'vintage',
            'visual_bloc',
            'visual_block_direction',
            'visualbell',
            'widget',
            'WrapPlus.include_line_ending',
            'xpos',
        ]

        prefixes = (
            '',
            '_',
            '__vi_',
            '_vi_',
            '_vintageous_',
            'enable_',
            'ex_',
            'is_',
            'is_vintageous_',
            'vi_',
            'vintageous_',
            'VintageousEx_',
        )

        data = {}
        for key in keys:
            for prefix in prefixes:
                _key = prefix + key
                value = settings.get(_key)
                if value is not None:
                    data[_key] = value

        print(' settings:')
        for k in sorted(data.keys()):
            v = data[k]
            if isinstance(v, dict):
                print('  {} {{'.format(k))
                for k in sorted(v.keys()):
                    print('    {:40} = {}'.format(k, v[k]))
                print('  }')
            else:
                print('  {:30} = {}'.format(k, v))

        print('<<<')
