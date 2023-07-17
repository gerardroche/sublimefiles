from contextlib import contextmanager

from sublime import load_settings
from sublime import save_settings
from sublime import status_message
from sublime import windows
import sublime_plugin


@contextmanager
def save_preferences():
    yield load_settings('Preferences.sublime-settings')
    save_settings('Preferences.sublime-settings')


class ToggleCommand(sublime_plugin.WindowCommand):

    def run(self):
        with save_preferences() as preferences:
            preference_name = self.get_preference_name()

            if preferences.get(preference_name) != self.get_enabled_value():
                setting_value = self.get_enabled_value()
            else:
                setting_value = self.get_disable_value()

            preferences.set(preference_name, setting_value)

            for window in windows():
                for view in window.views():
                    view.settings().erase(preference_name)

        status_message('{} is {}'.format(
            self.get_preference_description(),
            'enabled' if setting_value == self.get_enabled_value() else 'disabled'
        ))

    def description(self):
        view = self.window.active_view()
        if view:
            current_value = view.settings().get(self.get_preference_name())
            if current_value == self.get_disable_value():
                return 'Show ' + self.get_preference_description()
            if current_value == self.get_enabled_value():
                return 'Hide ' + self.get_preference_description()

        return 'Toggle ' + self.get_preference_description()

    def get_preference_name(self):
        return self.name()[7:]

    def get_preference_description(self):
        return self.get_preference_name().replace('_', ' ').title()

    def get_disable_value(self):
        return self.get_toggle_off_value(False)

    def get_enabled_value(self):
        return self.get_toggle_on_value(True)

    def get_toggle_off_value(self, default=None):
        return self.get_setting('%s_toggle_off' % self.get_preference_name(), default)

    def get_toggle_on_value(self, default=None):
        return self.get_setting('%s_toggle_on' % self.get_preference_name(), default)

    def get_setting(self, name: str, default=None):
        view = self.window.active_view()
        if view:
            value = view.settings().get(name)
            if value:
                return value

        if default is not None:
            return default


class ToggleFoldButtonsCommand(ToggleCommand):
    pass


class ToggleHighlightLineCommand(ToggleCommand):
    pass


class ToggleIndentGuideCommand(ToggleCommand):

    def get_preference_name(self):
        return 'indent_guide_options'

    def get_preference_description(self):
        return 'Indent Guide'

    def get_disable_value(self):
        return self.get_toggle_off_value([])

    def get_enabled_value(self):
        return self.get_toggle_on_value(['draw_normal', 'draw_active'])


class ToggleInvisiblesCommand(ToggleCommand):

    def get_preference_name(self):
        return 'draw_white_space'

    def get_disable_value(self):
        return self.get_toggle_on_value('selection')

    def get_enabled_value(self):
        return self.get_toggle_off_value('all')


class ToggleLineNumbersCommand(ToggleCommand):
    pass


class TogglePreviewOnClickCommand(ToggleCommand):

    def get_preference_description(self):
        return 'Preview on Click'


class ToggleRulersCommand(ToggleCommand):

    def get_disable_value(self):
        return self.get_toggle_off_value([])

    def get_enabled_value(self):
        return self.get_toggle_on_value([80, 120])


class ToggleSaveOnFocusLostCommand(ToggleCommand):
    pass


class ToggleUserSettingCommand(sublime_plugin.ApplicationCommand):

    def run(self, key):
        with save_preferences() as preferences:
            preferences = preferences.set(key, not bool(preferences.get(key, False)))
