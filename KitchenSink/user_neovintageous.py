import functools
import os
import re

import sublime
import sublime_plugin


class NeovintageousDevCommand(sublime_plugin.WindowCommand):

    def run(self, action):
        action_method = getattr(self, action + '_action', None)
        if not action_method:
            raise ValueError('action not found')

        print('NeoVintageous: ', action.replace('_', ' '))
        action_method()

    def edit_help_file_action(self):
        """Open up a NeoVintageous help file for editing."""
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

            view = self.window.open_file(os.path.join(sublime.packages_path(), 'NeoVintageous', resource))
            view.assign_syntax('Packages/NeoVintageous/res/Help.sublime-syntax')
            view.settings().set('indent_guide_options', [])
            view.settings().set('spell_check', True)

            if int(sublime.version()) < 4065:
                view.settings().set('wrap_width', 78)
            else:
                view.settings().set('wrap_width', 78)

            view.settings().set('word_wrap', False)
            view.settings().set('line_numbers', True)

        self.window.show_quick_panel(resources, on_done)

    def fixup_docs_action(self):
        """Fix encoding issues with Vim doc files."""
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
                    sublime.load_resource(resource)
                except Exception as e:
                    print('  Error: ' + resource + ' ' + str(e))

                    file = sublime.packages_path() + '/NeoVintageous/res/doc/%s' % f
                    print('    Fixing resource encoding for \'{}\''.format(file))

                    view = self.window.open_file(file)

                    sublime.set_timeout_async(functools.partial(set_utf8_encoding_save_and_close, view), 200)

    def dump_ex_completions_action(self):
        """Temporary hacky command to generate ex completions."""
        from NeoVintageous.nv import ex_routes
        routes = [r for r in ex_routes.ex_routes]

        print("\n\n\n")
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

        print("\n'" + "', '".join(completions) + "'\n")

    def dump_mappings_action(self):
        from NeoVintageous.nv.vi import keys  # noqa
        from NeoVintageous.nv import plugin  # noqa
        from NeoVintageous.nv import mappings  # noqa

        print("\n------------")
        print("--- KEYS ---")
        print("------------\n")

        k = []
        for mode, mapping in keys.mappings.items():
            for seq, cmd in keys.mappings[mode].items():
                k.append('{: <10} {: <35} {: <35}'.format(seq, mode, cmd))
        k.sort()
        print('\n'.join(k))

        print("\n--------------")
        print("--- PLUGIN ---")
        print("--------------\n")

        plugs = []
        for mode, mapping in plugin.mappings.items():
            for seq, cmd in plugin.mappings[mode].items():
                plugs.append('{: <35} {: <10} {}'.format(cmd, seq, mode))
        plugs.sort()
        print('\n'.join(plugs))

        print("\n\n")
        for name, obj in plugin.classes.items():
            print('    {: <35} {}'.format(name, obj))

        print("\n---------------")
        print("--- MAPPING ---")
        print("---------------\n")

        m = []
        for mode, mapping in mappings._mappings.items():
            for seq, cmd in mappings._mappings[mode].items():
                m.append('{: <10} {: <35} {: <35}'.format(seq, mode, cmd))
        m.sort()
        print('\n'.join(m))


class NeovintageousDumpViewCommand(sublime_plugin.WindowCommand):

    def run(self):
        view = self.window.active_view()
        settings = view.settings()

        view.window().run_command('dump_view')

        keys = [
            'WrapPlus.include_line_ending',
            'action',
            'action_count',
            'autoindent',
            'bell',
            'bell_color_scheme',
            'clear_auto_indent_on_esc',
            'cmdline_cd',
            'cmdline_mode',
            'command_mode',
            'data',
            'default_mode',
            'editor_setting',
            'enable_abolish',
            'enable_commentary',
            'enable_multiple_cursors',
            'enable_surround',
            'enable_unimpaired',
            'external_disable',
            'external_disable_keys',
            'glue_until_normal_mode',
            'highlightedyank',
            'highlightedyank_duration',
            'highlightedyank_style',
            'hlsearch',
            'ignorecase',
            'incsearch',
            'inverse_caret_state',
            'last_buffer_search',
            'last_buffer_search_command',
            'last_char_search',
            'last_char_search_command',
            'last_character_search',
            'linux_shell',
            'linux_terminal',
            'magic',
            'mode',
            'motion',
            'motion_count',
            'multi_cursor_exit_from_visual_mode',
            'capture_register',
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
            'reset_mode_when_switching_tabs',
            'rulers',
            'search_cur_style',
            'search_inc_style',
            'search_occ_style',
            'sequence',
            'shell_silent',
            'showsidebar',
            'surround',
            'surround_spaces',
            'use_ctrl_keys',
            'use_super_keys',
            'use_sys_clipboard',
            'vi_editor_setting',
            'vintage',
            'visual_bloc',
            'visual_block_direction',
            'visualbell',
            'widget',
            'xpos',
        ]

        prefixes = (
            '',
            'VintageousEx_',
            '_',
            '__nv_',
            '__vi_',
            '_neovintageous_',
            '_nv_',
            '_vi_',
            '_vintageous_',
            'enable_',
            'ex_',
            'is_',
            'is_vintageous_',
            'neovintageous_',
            'nv_',
            'vi_',
            'vintageous_',
        )

        data = {}
        for key in keys:
            for prefix in prefixes:
                _key = prefix + key
                value = settings.get(_key)
                if value is not None:
                    data[_key] = value

        for k in sorted(data.keys()):
            v = data[k]
            if isinstance(v, dict):
                print(' {}'.format(k))
                for k in sorted(v.keys()):
                    append = ''
                    if str(type(v)) not in ('<class \'int\'>', '<class \'str\'>', '<class \'bool\'>', '<class \'dict\'>'):  # noqa: E501
                        append += ' ' + str(type(v))
                    print('%40s = %s %s' % (k, v[k], append))
            else:
                print(' {:50} = {}'.format(k, v))
