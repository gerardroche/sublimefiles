from contextlib import contextmanager

from sublime import load_settings
from sublime import save_settings
from sublime import status_message
from sublime import windows
import sublime_plugin


class ToggleCommand(sublime_plugin.WindowCommand):

    def run(self, name=None):
        with save_preferences() as preferences:
            preference_name = name if name else self.get_preference_name()

            value = self.get_on_value()
            if preferences.get(preference_name) == value:
                value = self.get_off_value()

            preferences.set(preference_name, value)

            for window in windows():
                for view in window.views():
                    view.settings().erase(preference_name)

        status_message('{} is {}'.format(
            self.get_preference_description(),
            'enabled' if value == self.get_on_value() else 'disabled'
        ))

    def description(self):
        view = self.window.active_view()
        if view:
            current_value = view.settings().get(self.get_preference_name())
            if current_value == self.get_off_value():
                return 'Show ' + self.get_preference_description()
            if current_value == self.get_on_value():
                return 'Hide ' + self.get_preference_description()

        return 'Toggle ' + self.get_preference_description()

    def get_preference_name(self):
        return self.name()[7:]

    def get_preference_description(self):
        return self.get_preference_name().replace('_', ' ').title()

    def get_off_value(self):
        return self.get_off_value_or(False)

    def get_on_value(self):
        return self.get_on_value_or(True)

    def get_off_value_or(self, default=None):
        return self.get_setting('%s_toggle_off' % self.get_preference_name(), default)

    def get_on_value_or(self, default=None):
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

    def get_off_value(self):
        return self.get_off_value_or([])

    def get_on_value(self):
        return self.get_on_value_or(['draw_normal', 'draw_active'])


class ToggleInvisiblesCommand(ToggleCommand):

    def get_preference_name(self):
        return 'draw_white_space'

    def get_off_value(self):
        return self.get_on_value_or('selection')

    def get_on_value(self):
        return self.get_off_value_or('all')


class ToggleLineNumbersCommand(ToggleCommand):
    pass


class TogglePreviewOnClickCommand(ToggleCommand):

    def get_preference_description(self):
        return 'Preview on Click'


class ToggleRulersCommand(ToggleCommand):

    def get_off_value(self):
        return self.get_off_value_or([])

    def get_on_value(self):
        return self.get_on_value_or([80, 120])


class ToggleSaveOnFocusLostCommand(ToggleCommand):
    pass


# class ToggleUserSettingCommand(sublime_plugin.ApplicationCommand):

#     def run(self, key):
#         with save_preferences() as preferences:
#             preferences = preferences.set(key, not bool(preferences.get(key, False)))


@contextmanager
def save_preferences():
    yield load_settings('Preferences.sublime-settings')
    save_settings('Preferences.sublime-settings')
