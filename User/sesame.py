import os

from sublime import load_settings
from sublime import packages_path
from sublime import save_settings
from sublime_plugin import WindowCommand


class SesameCommandPaletteCommand(WindowCommand):
    def run(self):
        self.window.run_command('show_overlay', {
            'overlay': 'command_palette'
        })


class SesamePreferencesCommand(WindowCommand):
    def run(self):
        self.window.run_command('open_file', {
            'file': os.path.join(
                packages_path(),
                'User',
                'Preferences.sublime-settings'
            )
        })


class SesameToggleTemporaryFolder(WindowCommand):
    def run(self):
        preferences = load_settings('Preferences.sublime-settings')

        folder_exclude_patterns = preferences.get('folder_exclude_patterns', [])

        if 'tmp' not in folder_exclude_patterns:
            folder_exclude_patterns.append('tmp')
        else:
            folder_exclude_patterns.remove('tmp')

        folder_exclude_patterns.sort()
        preferences.set('folder_exclude_patterns', folder_exclude_patterns)

        save_settings('Preferences.sublime-settings')


class SesameToggleFullScreenCommand(WindowCommand):
    _is_active = False
    _original_is_menu_visible = False

    def run(self):
        self.window.run_command('toggle_full_screen')

        if self._is_active:
            self.window.set_menu_visible(self._original_is_menu_visible)
            self._is_active = False
        else:
            self._original_is_menu_visible = self.window.is_menu_visible()
            self.window.set_menu_visible(False)
            self._is_active = True


class SesameToggleDistractionFreeCommand(WindowCommand):
    _is_active = False
    _original_is_menu_visible = False

    def run(self):
        self.window.run_command('toggle_distraction_free')

        if self._is_active:
            self.window.set_menu_visible(self._original_is_menu_visible)
            self._is_active = False
        else:
            self._original_is_menu_visible = self.window.is_menu_visible()
            self.window.set_menu_visible(False)
            self._is_active = True

