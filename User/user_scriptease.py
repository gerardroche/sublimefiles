# When you see something you like and would like to use it, open an issue about
# abstracting it out into a reusable package, possibly installable via Package
# Control.

import os
import re
import sys

from sublime import active_window
from sublime import load_settings
from sublime import log_commands
from sublime import log_input
from sublime import packages_path
from sublime import save_settings
from sublime import status_message
import sublime_plugin


_DEBUG = bool(os.getenv('SUBLIME_DEBUG'))


_DEBUG_EVENTS = False


_debug_plugins_meta = [
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
    # We have to use a function to generate (rather than doing it at  module
    # level) because the the Sublime Text API `sublime.package_path` is not
    # available until all plugins are loaded.
    return os.path.join(packages_path(), 'User', '.debug')


def _debug_indicator_file_exists():
    return os.path.isfile(_debug_indicator_file_name())


def _set_debug_mode(flag):
    log_commands(flag)
    log_input(flag)

    # Create or remove the debug indicator file.
    if _debug_indicator_file_exists():
        if not flag:
            os.remove(_debug_indicator_file_name())
    else:
        if flag:
            with open(_debug_indicator_file_name(), 'w+', encoding='utf8') as f:
                f.write('')

    preferences = load_settings('Preferences.sublime-settings')

    plugins = {}
    for setting in _debug_plugins_meta:
        if isinstance(setting, tuple):
            plugin_name, settings = setting
            plugins[plugin_name] = load_settings(plugin_name + '.sublime-settings')

            if isinstance(settings, str):
                settings = [settings]

            for key in settings:
                print('Scriptease: {} \'{}\''.format('enable' if flag else 'disable', setting))
                if flag:
                    plugins[plugin_name].set(key, True)
                else:
                    plugins[plugin_name].erase(key)
        else:
            print('Scriptease: {} \'{}\''.format('enable' if flag else 'disable', setting))
            if flag:
                preferences.set(str(setting), True)
            else:
                preferences.erase(str(setting))

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
    if _DEBUG or _debug_indicator_file_exists():
        # Debug all the things.
        _set_debug_mode(True)

        print('Scriptease: debug enabled')

        # Show some system information.
        print('Scriptease: Python v{}.{}.{} {}{}'.format(
            sys.version_info[0],
            sys.version_info[1],
            sys.version_info[2],
            sys.version_info[3],
            sys.version_info[4]))
        print('Scriptease: {}'.format(sys.flags))
        print('Scriptease: sys.abiflags are {}'.format(sys.abiflags))
        print('Scriptease: sys.path is {}'.format(sys.path))
        print('Scriptease: __debug__ is {}'.format(__debug__))

        # Auto show the console.
        window = active_window()
        active_group = window.active_group()
        window.run_command('show_panel', {'panel': 'console'})
        window.focus_group(active_group)


class ScripteaseCommand(sublime_plugin.ApplicationCommand):

    def run(self, action):
        action_method = getattr(self, action + '_action', None)
        if action_method:
            action_method()
        else:
            raise Exception('action not found')

    def enable_debug_mode_action(self):
        _set_debug_mode(True)

    def disable_debug_mode_action(self):
        _set_debug_mode(False)

    def enable_st_debug_mode_action(self):
        log_commands(True)
        log_input(True)

    def disable_st_debug_mode_action(self):
        log_commands(False)
        log_input(False)

    def toggle_plugin_debug_mode_action(self):
        toggle_plugins = [str(p) for p in _debug_plugins_meta]
        def on_done(index):
            if index >= 0:
                status = _toggle_debug_mode(_debug_plugins_meta[index])

        active_window().show_quick_panel(toggle_plugins, on_done)

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

        print('>>> Scriptease: {} [id={}, file={}'
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

        scope_name = self.view.scope_name(pt)

        if 'php' in scope_name:
            pt += 1

        word_region = self.view.word(pt)
        word = self.view.substr(word_region)
        if not re.match('^[a-zA-Z_][a-zA-Z0-9_]*$', word):
            return

        if 'php' in scope_name:
            dump_stmt = 'var_dump($' + word + ');'
        elif 'python' in scope_name:
            dump_stmt = 'print(\'' + word + ' =\', ' + word + ')'
        else:
            raise NotImplementedError('unknown scope')

        self.view.insert(edit, line.end(), '\n' + dump_stmt)
        self.view.run_command('move', {'by': 'lines', 'forward': True})
        self.view.run_command('reindent', {'single_line': True})
        self.view.run_command('save')


if _DEBUG_EVENTS:

    class DebugEvents(sublime_plugin.EventListener):

        def _debug_event(self, name, view, extra=None):
            print('*** DEBUG EVENT *** {} view {}{}{}'.format(
                name,
                view.id(),
                ' {}'.format(view.name()) if view.name() else '',
                ' {}'.format(view.file_name()) if view.file_name() else '',
            ))

            settings = view.settings()
            if not settings:
                print('    View has not settings object!')

            print('    scratch/readonly/widget = {}/{}/{}'.format(
                view.is_scratch(),
                view.is_read_only(),
                settings.get('is_widget') if settings else 'n/a'
            ))

            print('    selection =', list(view.sel()))
            print('    scope =', view.scope_name(0))
            print('    result_file_regex =', settings.get('result_file_regex') if settings else 'n/a')

            if extra:
                print('   ', extra)

            # print('CONTENT =', self.view.substr(sublime.Region(0, self.view.size())))

        def on_new(self, view):                         self._debug_event('on_new', view) # noqa
        def on_new_async(self, view):                   self._debug_event('on_new_async', view) # noqa
        def on_clone(self, view):                       self._debug_event('on_clone', view) # noqa
        def on_clone_async(self, view):                 self._debug_event('on_clone_async', view) # noqa
        def on_load(self, view):                        self._debug_event('on_load', view) # noqa
        def on_load_async(self, view):                  self._debug_event('on_load_async', view) # noqa
        def on_pre_close(self, view):                   self._debug_event('on_pre_close', view) # noqa
        def on_close(self, view):                       self._debug_event('on_close', view) # noqa
        def on_pre_save(self, view):                    self._debug_event('on_pre_save', view) # noqa
        def on_pre_save_async(self, view):              self._debug_event('on_pre_save_async', view) # noqa
        def on_post_save(self, view):                   self._debug_event('on_post_save', view) # noqa
        def on_post_save_async(self, view):             self._debug_event('on_post_save_async', view) # noqa
        # def on_modified(self, view):                    self._debug_event('on_modified', view) # noqa
        # def on_modified_async(self, view):              self._debug_event('on_modified_async', view) # noqa
        # def on_selection_modified(self, view):          self._debug_event('on_selection_modified', view) # noqa
        # def on_selection_modified_async(self, view):    self._debug_event('on_selection_modified_async', view) # noqa
        def on_activated(self, view):                   self._debug_event('on_activated', view) # noqa
        def on_activated_async(self, view):             self._debug_event('on_activated_async', view) # noqa
        def on_deactived(self, view):                   self._debug_event('on_deactivated', view) # noqa
        def on_deactivated_async(self, view):           self._debug_event('on_deactivated_async', view) # noqa

        # def on_query_context(self, view, key, operator, operand, match_all):
        #     self._debug_event('on_query_context', view, 'key = {} operator = {} operand = {} match_all = {}'.format(key, operator, operand, match_all)) # noqa

        # def on_query_completions(self, view, prefix, locations):
        #     self._debug_event('on_query_completions', view, 'prefix = {} locations = {}'.format(prefix, locations)) # noqa

        # # def on_hover(self, view, point, hover_zone):
        # #     self._debug_event('on_hover', view)
        # #     print('*** EVENT *** on_hover point = {} hover_zone = {}'.format(point, hover_zone)) # noqa

        # def on_text_command(self, view, name, args):
        #     self._debug_event('on_query_completions', view, 'name = {} args = {}'.format(name, args)) # noqa

        # def on_post_text_command(self, view, name, args):
        #     self._debug_event('on_post_text_command', view, 'name = {} args = {}'.format(name, args)) # noqa

        # def on_window_command(self, window, name, args):
        #     print('*** EVENT *** on_window_command id = {} name = {} args = {}'.format(window.id(), name, args)) # noqa

        # def on_post_window_command(self, window, name, args):
        #     print('*** EVENT *** on_post_window_command id = {} name = {} args = {}'.format(window.id(), name, args)) # noqa
