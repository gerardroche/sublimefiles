import functools
import logging
import os
import re
import sys

from sublime import active_window
from sublime import load_resource
from sublime import load_settings
from sublime import log_build_systems
from sublime import log_commands
from sublime import log_indexing
from sublime import log_input
from sublime import log_result_regex
from sublime import packages_path
from sublime import save_settings
from sublime import set_timeout_async
from sublime import status_message
import sublime_plugin


# When you see something you like and would like to use it, open an issue about
# abstracting it out into a reusable package, possibly installable via Package
# Control.


_DEBUG = bool(os.getenv('SUBLIME_DEBUG'))


_DEBUG_EVENTS = False


_DEBUGABLE_PLUGINS = [
    'autohide_sidebar_verbose_logging',
    'color_scheme_unit.debug',
    'docblockr.debug',
    'git_gutter_debug',
    'neovintageous.debug',
    'open-sesame.debug',
    'php-grammar.debug',
    'phpunit.debug',
    'sesame.debug',
    ('SublimeLinter', 'debug'),
    'test.debug',
    'user.debug',
    'vintageous_debug'
]


def _debug_indicator_file_name():
    return os.path.join(packages_path(), 'User', '.debug')


def _debug_indicator_file_exists():
    return os.path.isfile(_debug_indicator_file_name())


def _remove_debug_indicator_file():
    os.remove(_debug_indicator_file_name())


def _create_debug_indicator_file():
    with open(_debug_indicator_file_name(), 'w+', encoding='utf8') as f:
        f.write('')


def _is_debug_mode():
    global _DEBUG

    if _DEBUG:
        return True

    if _debug_indicator_file_exists():
        return True

    return False


def _set_debug_mode(flag):
    log_commands(flag)
    log_input(flag)

    if flag:
        if not _debug_indicator_file_exists():
            _create_debug_indicator_file()
    else:
        if _debug_indicator_file_exists():
            _remove_debug_indicator_file()

    preferences = load_settings('Preferences.sublime-settings')
    plugins = {}

    for debug_preference in _DEBUGABLE_PLUGINS:
        print('DEBUG {} \'{}\' debug mode'.format('enable' if flag else 'disable', debug_preference))

        if isinstance(debug_preference, tuple):
            plugin_name = debug_preference[0]
            plugins[plugin_name] = load_settings(plugin_name + '.sublime-settings')
            if flag:
                plugins[plugin_name].set(debug_preference[1], True)
            else:
                plugins[plugin_name].erase(debug_preference[1])
        else:
            if flag:
                preferences.set(debug_preference, True)
            else:
                preferences.erase(debug_preference)

    for plugin in plugins.keys():
        save_settings(plugin + '.sublime-settings')

    save_settings('Preferences.sublime-settings')


def _toggle_debug_mode(setting=None):
    if setting is not None:
        if isinstance(setting, tuple):
            settings_name = setting[0] + '.sublime-settings'
            preferences = load_settings(settings_name)
            setting = setting[1]
        else:
            settings_name = 'Preferences.sublime-settings'
            preferences = load_settings(settings_name)

        flag = not preferences.get(setting)
        if flag:
            preferences.set(setting, True)
        else:
            preferences.erase(setting)

        save_settings(settings_name)

        return flag
    else:
        global _DEBUG
        _DEBUG = not _DEBUG
        _set_debug_mode(_DEBUG)

        return _DEBUG


def plugin_loaded():

    # What do these even do?
    log_result_regex(False)
    log_build_systems(False)

    # Can't disable log indexing.
    # See https://github.com/SublimeTextIssues/Core/issues/2131.
    log_indexing(False)

    if _is_debug_mode():

        print('DEBUG enabled')
        print('DEBUG Python v{}.{}.{} {}{}'.format(
            sys.version_info[0],
            sys.version_info[1],
            sys.version_info[2],
            sys.version_info[3],
            sys.version_info[4]))
        print('DEBUG {}'.format(sys.flags))
        print('DEBUG sys.abiflags are {}'.format(sys.abiflags))
        print('DEBUG sys.path is {}'.format(sys.path))
        print('DEBUG __debug__ is {}'.format(__debug__))

        _set_debug_mode(True)

        window = active_window()
        active_group = window.active_group()
        window.run_command('show_panel', {'panel': 'console'})
        window.focus_group(active_group)


class DebugApplicationCommand(sublime_plugin.ApplicationCommand):
    def run(self, action):

        if action == 'toggle':
            status = _toggle_debug_mode()
            status_message('Debug is ' + 'enabled' if status else 'disabled')

        elif action == 'enable':
            _set_debug_mode(True)
            status_message('Debug is enabled')

        elif action == 'disable':
            _set_debug_mode(False)
            status_message('Debug is enabled')

        elif action == 'toggle_plugin':
            self.toggle_plugins = [str(p) for p in _DEBUGABLE_PLUGINS]
            self.window = active_window()
            self.window.show_quick_panel(self.toggle_plugins, self._toggle_plugin_on_done)

        else:
            raise Exception('unknown action')

    def _toggle_plugin_on_done(self, index):
        if index >= 0:
            status = _toggle_debug_mode(_DEBUGABLE_PLUGINS[index])
            status_message('Debug is ' + 'enabled' if status else 'disabled')


class DebugViewToScopeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        scopes = []
        for point in range(self.view.size()):
            # scope_name() needs to striped due to a bug in ST:
            # See https://github.com/SublimeTextIssues/Core/issues/657.
            scopes.append(self.view.scope_name(point).strip())

        print('>>>')
        print("\n".join(scopes))
        print('<<<')


class DebugViewCommand(sublime_plugin.TextCommand):

    def run(self, edit=None):
        view = self.view

        print('>>> DEBUG {} [id={}, file={}'
              '\n buffer_id={: <5}        is_valid={: <5}     is_primary={: <5}   name={: <5}'
              '\n is_dirty={: <5}         is_read_only={: <5} is_scratch={: <5}   encoding={: <5}'
              '\n line_endings={: <5}     is_in_edit={: <5}   change_count={: <5} is_loading={: <5}'
              '\n line_height={: <5}      em_width={: <5}     is_popup_visible={: <5}'
              '\n overwrite_status={: <5} size={: <5}         is_auto_complete_visible={: <5}'
              '\n has_non_empty_selection_region={: <5}'
              .format(
                  str(view),
                  str(view.id()), str(view.file_name()),
                  str(view.buffer_id()), str(view.is_valid()), str(view.is_primary()), str(view.name()),
                  str(view.is_dirty()), str(view.is_read_only()), str(view.is_scratch()), str(view.encoding()),
                  str(view.line_endings()), str(view.is_in_edit()), str(view.change_count()), str(view.is_loading()),
                  str(view.line_height()), str(view.em_width()), str(view.is_popup_visible()),
                  str(view.overwrite_status()), str(view.size()), str(view.is_auto_complete_visible()),
                  str(view.has_non_empty_selection_region())))

        print(' sel={}:{}'.format(type(view.sel()), list(view.sel())))

        for i, sel in enumerate(view.sel()):
            print('   sel[{}] {} a = {}, b = {}'.format(i, sel, sel.a, sel.b))
            print('   sel[{}] begin = {}, end = {}, begin substr = "{}", end substr = "{}"'.format(
                i, sel.begin(), sel.end(),
                view.substr(sel.begin()).replace('\n', '\\n'),
                view.substr(sel.end()).replace('\n', '\\n')
            ))
            print('   sel[{}] empty? {}'.format(i, sel.empty()))
            print('   sel[{}] word {} substr >>>{}<<<'.format(
                i, view.word(sel.begin()), view.substr(view.word(sel.begin()))).replace('\n', '\\n'))
            print('   sel[{}] rowcol {} {}'.format(i, view.rowcol(sel.begin()), type(view.rowcol(sel.begin()))))
            print('   sel[{}] visible_region {} {}'.format(i, view.visible_region(), type(view.visible_region())))
            print('   sel[{}] viewport_position {} {}'.format(i, view.viewport_position(), type(view.viewport_position())))  # noqa: E501
            print('   sel[{}] viewport_extent {} {}'.format(i, view.viewport_extent(), type(view.viewport_extent())))
            print('   sel[{}] layout_extent {} {}'.format(i, view.layout_extent(), type(view.layout_extent())))
            print('   sel[{}] text_to_layout (begin) {} {}'.format(
                i, view.text_to_layout(sel.begin()), type(view.text_to_layout(sel.begin()))))
            # print('    sel[{}] word classify = {}'.format(i, view.classify(sel.begin())))
            # print('    sel[{}] scope name begin = {}'.format(i, view.scope_name(sel.begin())))
            # print('    sel[{}] indentation level begin = {}'.format(i, str(view.indentation_level(sel.begin()))))
            # print('    sel[{}] indented region begin = {}'.format(i, view.indented_region(sel.begin())))
            # print('    sel[{}] indented region begin substr = >>{}<<'.format(
            #   i, view.substr(view.indented_region(sel.begin()))))


class DumpNeovintageousViewCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        settings = view.settings()

        print('>>> DEBUG NeoVintageous View')

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


class NeovintageousDevCommand(sublime_plugin.WindowCommand):

    def run(self, action):
        action_method = getattr(self, action + '_action', None)
        if action_method:
            print('NeoVintageousDev: ', action.replace('_', ' '))
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
            view.settings().set('rulers', [8, 24, 40, 80])

        self.window.show_quick_panel(resources, on_done)

    def fixup_docs_action(self):
        docs_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'NeoVintageous/res/doc')

        for f in os.listdir(docs_path):
            if f.endswith('.txt'):
                resource = 'Packages/NeoVintageous/res/doc/%s' % f

                exception = False
                try:
                    load_resource(resource)
                except Exception as e:
                    exception = e

                if exception:
                    print('  Error: ' + resource + ' ' + str(exception))

                    file = packages_path() + '/NeoVintageous/res/doc/%s' % f
                    print('    Fixing resource encoding for \'{}\''.format(file))

                    view = self.window.open_file(file)

                    def f(view):
                        view.run_command('set_encoding', {'encoding': 'utf-8'})
                        view.run_command('save')
                        view.close()

                    set_timeout_async(functools.partial(f, view), 200)

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
            logging.getLogger('NeoVintageous').setLevel(getattr(
                logging,
                log_level,
                logging.DEBUG
            ))

            indicator_file = os.path.join(packages_path(), 'User', '.neovintageous_log_level')
            with open(indicator_file, 'w+', encoding='utf8') as f:
                f.write(log_level)

        self.window.show_quick_panel(log_levels, on_done)

    def toggle_use_ctrl_keys_action(self):
        preferences = load_settings('Preferences.sublime-settings')
        use_ctrl_keys = preferences.get('vintageous_use_ctrl_keys')
        preferences.set('vintageous_use_ctrl_keys', not use_ctrl_keys)
        save_settings('Preferences.sublime-settings')


class VarDumpCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        pt = self.view.sel()[0].b
        line = self.view.line(pt)
        if line.empty():
            row, col = self.view.rowcol(pt)
            prev_row = max(row - 1, 0)
            if prev_row != row:
                pt = self.view.text_point(prev_row, 0)

        if self.view.substr(pt) == ' ':
            f = self.view.find('\\s*', pt)
            pt = f.end()

        word_region = self.view.word(pt)
        word = self.view.substr(word_region)
        if not re.match('^[a-zA-Z_][a-zA-Z0-9_]*$', word):
            return

        scope_name = self.view.scope_name(pt)

        if 'php' in scope_name:
            dump_stmt = 'var_dump(' + word + ');'
        elif 'python' in scope_name:
            dump_stmt = 'print(\'' + word.upper() + ' =\', ' + word + ')'
        else:
            raise NotImplementedError('unknown scope')

        self.view.insert(edit, line.end(), '\n' + dump_stmt)
        self.view.run_command('move', {'by': 'lines', 'forward': True})
        self.view.run_command('reindent', {'single_line': True})
        self.view.run_command('save')


if _DEBUG_EVENTS:

    class DebugEvents(sublime_plugin.EventListener):

        def on_new(self, view):
            print('*** EVENT *** on_new', view.id(), view.file_name())

        def on_new_async(self, view):
            print('*** EVENT *** on_new_async', view.id(), view.file_name())

        def on_clone(self, view):
            print('*** EVENT *** on_clone', view.id(), view.file_name())

        def on_clone_async(self, view):
            print('*** EVENT *** on_clone_async', view.id(), view.file_name())

        def on_load(self, view):
            print('*** EVENT *** on_load', view.id(), view.file_name())

        def on_load_async(self, view):
            print('*** EVENT *** on_load_async', view.id(), view.file_name())

        def on_pre_close(self, view):
            print('*** EVENT *** on_pre_close', view.id(), view.file_name())

        def on_close(self, view):
            print('*** EVENT *** on_close', view.id(), view.file_name())

        def on_pre_save(self, view):
            print('*** EVENT *** on_pre_save', view.id(), view.file_name())

        def on_pre_save_async(self, view):
            print('*** EVENT *** on_pre_save_async', view.id(), view.file_name())

        def on_post_save(self, view):
            print('*** EVENT *** on_post_save', view.id(), view.file_name())

        def on_post_save_async(self, view):
            print('*** EVENT *** on_post_save_async', view.id(), view.file_name())

        def on_modified(self, view):
            print('*** EVENT *** on_modified', view.id(), view.file_name())

        def on_modified_async(self, view):
            print('*** EVENT *** on_modified_async', view.id(), view.file_name())

        def on_selection_modified(self, view):
            print('*** EVENT *** on_selection_modified', view.id(), view.file_name())

        def on_selection_modified_async(self, view):
            print('*** EVENT *** on_selection_modified_async', view.id(), view.file_name())

        def on_activated(self, view):
            print('*** EVENT *** on_activated', view.id(), view.file_name())

        def on_activated_async(self, view):
            print('*** EVENT *** on_activated_async', view.id(), view.file_name())

        def on_deactived(self, view):
            print('*** EVENT *** on_deactivated', view.id(), view.file_name())

        def on_deactivated_async(self, view):
            print('*** EVENT *** on_deactivated_async', view.id(), view.file_name())

        def on_query_context(self, view, key, operator, operand, match_all):
            print('*** EVENT *** on_query_context {} \'{}\' key={} operator={} operand={} match_all={}'
                  .format(view.id(), view.file_name(), key, operator, operand, match_all))

        def on_query_completions(self, view, prefix, locations):
            print('*** EVENT *** on_query_completions {} \'{}\' prefix={} locations={}'
                  .format(view.id(), view.file_name(), prefix, locations))

        # def on_hover(self, view, point, hover_zone):
        #     print('*** EVENT *** on_hover', view.id(), view.file_name())

        def on_text_command(self, view, name, args):
            print('*** EVENT *** on_text_command {} \'{}\' {} args={}'
                  .format(view.id(), view.file_name(), name, args))

        def on_window_command(self, window, name, args):
            print('*** EVENT *** on_window_command {} {} args={}'
                  .format(window.id(), name, args))

        def on_post_text_command(self, view, name, args):
            print('*** EVENT *** on_post_text_command {} \'{}\' {} args={}'
                  .format(view.id(), view.file_name(), name, args))

        def on_post_window_command(self, window, name, args):
            print('*** EVENT *** on_post_window_command {} {} args={}'
                  .format(window.id(), name, args))
