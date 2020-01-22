import os

from sublime import active_window
from sublime import load_settings
from sublime import log_commands
from sublime import log_input
from sublime import packages_path
from sublime import save_settings
import sublime_plugin


_DEBUG = bool(os.getenv('SUBLIME_DEBUG'))
_DEBUG_EVENTS = False
_DEBUG_VIEW_EVENTS = False


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


def _is_debug_mode():
    return _DEBUG or _debug_indicator_file_exists()


def plugin_loaded():
    if _is_debug_mode():
        _set_debug_mode(True)

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

    def enable_debug_mode_action(self):
        _set_debug_mode(True)

    def disable_debug_mode_action(self):
        _set_debug_mode(False)

    def toggle_plugin_debug_mode_action(self):
        toggle_plugins = [str(p) for p in _debug_plugins_meta]

        def on_done(index):
            if index >= 0:
                _toggle_debug_mode(_debug_plugins_meta[index])

        active_window().show_quick_panel(toggle_plugins, on_done)


if _DEBUG_VIEW_EVENTS:

    class DebugViewEvents(sublime_plugin.ViewEventListener):
        def _debug_event(self, name, extra=None):
            view = self.view
            print('*** DEBUG VIEW EVENT *** {} view {}{}{}'.format(name, view.id(), ' {}'.format(view.name()) if view.name() else '', ' {}'.format(view.file_name()) if view.file_name() else ''))  # noqa
            settings = view.settings()
            if not settings:
                print('*** NOTICE *** View has not settings object!')
            print('                         scratch/readonly/widget = {}/{}/{}'.format(view.is_scratch(), view.is_read_only(), settings.get('is_widget') if settings else 'n/a' ))  # noqa
            print('                         selection =', list(view.sel()))
            print('                         scope =', view.scope_name(0))
            if extra:
                print('                   ', extra)

        @classmethod
        def is_applicable(cls, settings):
            print('*** ViewEventListener.is_applicable?', cls, settings)
            return True

        @classmethod
        def applies_to_primary_view_only(cls):
            print('*** ViewEventListener.applies_to_primary_view_only?', cls)
            return True

        def on_activated(self):                   self._debug_event('on_activated') # noqa
        def on_activated_async(self):             self._debug_event('on_activated_async') # noqa
        def on_clone(self):                       self._debug_event('on_clone') # noqa
        def on_clone_async(self):                 self._debug_event('on_clone_async') # noqa
        def on_close(self):                       self._debug_event('on_close') # noqa
        def on_deactivated_async(self):           self._debug_event('on_deactivated_async') # noqa
        def on_deactived(self):                   self._debug_event('on_deactivated') # noqa
        def on_load(self):                        self._debug_event('on_load') # noqa
        def on_load_async(self):                  self._debug_event('on_load_async') # noqa
        def on_modified(self):                    self._debug_event('on_modified') # noqa
        def on_modified_async(self):              self._debug_event('on_modified_async') # noqa
        def on_new(self):                         self._debug_event('on_new') # noqa
        def on_new_async(self):                   self._debug_event('on_new_async') # noqa
        def on_post_save(self):                   self._debug_event('on_post_save') # noqa
        def on_post_save_async(self):             self._debug_event('on_post_save_async') # noqa
        def on_post_text_command(self, name, args):                     self._debug_event('on_post_text_command', 'name = {} args = {}'.format(name, args)) # noqa
        def on_post_window_command(self, window, name, args):           print('*** DEBUG VIEW EVENT *** on_post_window_command id = {} name = {} args = {}'.format(window.id(), name, args)) # noqa
        def on_pre_close(self):                   self._debug_event('on_pre_close') # noqa
        def on_pre_save(self):                    self._debug_event('on_pre_save') # noqa
        def on_pre_save_async(self):              self._debug_event('on_pre_save_async') # noqa
        def on_query_completions(self, prefix, locations):              self._debug_event('on_query_completions', 'prefix = {} locations = {}'.format(prefix, locations)) # noqa
        def on_query_context(self, key, operator, operand, match_all):  self._debug_event('on_query_context', 'key = {} operator = {} operand = {} match_all = {}'.format(key, operator, operand, match_all)) # noqa
        def on_selection_modified(self):          self._debug_event('on_selection_modified') # noqa
        def on_selection_modified_async(self):    self._debug_event('on_selection_modified_async') # noqa
        def on_text_command(self, name, args):                          self._debug_event('on_query_completions', 'name = {} args = {}'.format(name, args)) # noqa
        def on_window_command(self, window, name, args):                print('*** DEBUG VIEW EVENT *** on_window_command id = {} name = {} args = {}'.format(window.id(), name, args)) # noqa

        # def on_hover(self, view, point, hover_zone):
        #     self._debug_event('on_hover', view)
        #     print('*** EVENT *** on_hover point = {} hover_zone = {}'.format(point, hover_zone)) # noqa

if _DEBUG_EVENTS:

    class DebugEvents(sublime_plugin.EventListener):

        def _debug_event(self, name, view, extra=None):
            print('*** DEBUG EVENT *** {} view {}{}{}'.format(name, view.id(), ' {}'.format(view.name()) if view.name() else '', ' {}'.format(view.file_name()) if view.file_name() else ''))  # noqa

            settings = view.settings()
            if not settings:
                print('*** NOTICE *** View has not settings object!')

            print('                    scratch/readonly/widget = {}/{}/{}'.format(view.is_scratch(), view.is_read_only(), settings.get('is_widget') if settings else 'n/a'))  # noqa
            print('                    selection =', list(view.sel()))
            print('                    scope =', view.scope_name(0))
            print('                    result_file_regex =', settings.get('result_file_regex') if settings else 'n/a')
            if extra:
                print('                   ', extra)

        def on_activated(self, view):                   self._debug_event('on_activated', view) # noqa
        def on_activated_async(self, view):             self._debug_event('on_activated_async', view) # noqa
        def on_clone(self, view):                       self._debug_event('on_clone', view) # noqa
        def on_clone_async(self, view):                 self._debug_event('on_clone_async', view) # noqa
        def on_close(self, view):                       self._debug_event('on_close', view) # noqa
        def on_deactivated_async(self, view):           self._debug_event('on_deactivated_async', view) # noqa
        def on_deactived(self, view):                   self._debug_event('on_deactivated', view) # noqa
        def on_load(self, view):                        self._debug_event('on_load', view) # noqa
        def on_load_async(self, view):                  self._debug_event('on_load_async', view) # noqa
        def on_modified(self, view):                    self._debug_event('on_modified', view) # noqa
        def on_modified_async(self, view):              self._debug_event('on_modified_async', view) # noqa
        def on_new(self, view):                         self._debug_event('on_new', view) # noqa
        def on_new_async(self, view):                   self._debug_event('on_new_async', view) # noqa
        def on_post_save(self, view):                   self._debug_event('on_post_save', view) # noqa
        def on_post_save_async(self, view):             self._debug_event('on_post_save_async', view) # noqa
        def on_post_text_command(self, view, name, args): self._debug_event('on_post_text_command', view, 'name = {} args = {}'.format(name, args)) # noqa
        def on_post_window_command(self, window, name, args): print('*** DEBUG EVENT *** on_post_window_command id = {} name = {} args = {}'.format(window.id(), name, args)) # noqa
        def on_pre_close(self, view):                   self._debug_event('on_pre_close', view) # noqa
        def on_pre_save(self, view):                    self._debug_event('on_pre_save', view) # noqa
        def on_pre_save_async(self, view):              self._debug_event('on_pre_save_async', view) # noqa
        def on_query_completions(self, view, prefix, locations):                self._debug_event('on_query_completions', view, 'prefix = {} locations = {}'.format(prefix, locations)) # noqa
        def on_query_context(self, view, key, operator, operand, match_all):    self._debug_event('on_query_context', view, 'key = {} operator = {} operand = {} match_all = {}'.format(key, operator, operand, match_all)) # noqa
        def on_selection_modified(self, view):          self._debug_event('on_selection_modified', view) # noqa
        def on_selection_modified_async(self, view):    self._debug_event('on_selection_modified_async', view) # noqa
        def on_text_command(self, view, name, args):    self._debug_event('on_query_completions', view, 'name = {} args = {}'.format(name, args)) # noqa
        def on_window_command(self, window, name, args): print('*** DEBUG EVENT *** on_window_command id = {} name = {} args = {}'.format(window.id(), name, args)) # noqa

        # def on_hover(self, view, point, hover_zone):
        #     self._debug_event('on_hover', view)
        #     print('*** EVENT *** on_hover point = {} hover_zone = {}'.format(point, hover_zone)) # noqa
