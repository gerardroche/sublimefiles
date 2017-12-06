import os

from sublime import load_settings
from sublime import packages_path
from sublime import save_settings
import sublime_plugin


class OpenPreferencesCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command('open_file', {
            'file': os.path.join(
                packages_path(),
                'User',
                'Preferences.sublime-settings'
            )
        })


class RulersCommand(sublime_plugin.TextCommand):
    def run(self, edit, action):
        col = self.view.rowcol(self.view.sel()[0].begin())[1]
        if col > 0:
            queue_save = False
            preferences = load_settings('Preferences.sublime-settings')
            rulers = preferences.get('rulers')

            if action == 'add':
                if col not in rulers:
                    rulers.append(col)
                    queue_save = True
            elif action == 'remove':
                if col in rulers:
                    rulers.remove(col)
                    queue_save = True
            elif action == 'clear':
                if rulers != []:
                    rulers = []
                    queue_save = True
            else:
                raise Exception('unknown action')

            if queue_save:
                rulers.sort()
                preferences.set('rulers', rulers)
                save_settings('Preferences.sublime-settings')


class ShowGotoCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command('show_overlay', {
            'overlay': 'goto',
            'text': '@'
        })


class ShowCommandPaletteCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command('show_overlay', {
            'overlay': 'command_palette'
        })


class ToggleDistractionFreeCommand(sublime_plugin.WindowCommand):
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


class ToggleFullScreenCommand(sublime_plugin.WindowCommand):
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


class ToggleTemporaryFolderCommand(sublime_plugin.WindowCommand):
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


class FocusUnitTestingPanelCommand(sublime_plugin.WindowCommand):
    def run(self):
        name = 'output.UnitTesting'
        self.window.run_command('show_panel', {'panel': name})

        name = 'UnitTesting'
        self.window.focus_view(self.window.find_output_panel(name))


# TODO RenameFile()
# TODO ExtractVariable()
# TODO InlineVariable()
# TODO OpenChangedFiles()
# TODO SelectaFile("name")
