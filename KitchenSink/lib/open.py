import os

from sublime import packages_path
import sublime_plugin


class OpenKeyBindings(sublime_plugin.WindowCommand):

    def run(self):
        self.window.run_command('open_file', {
            'file': os.path.join(
                packages_path(),
                'User',
                'Default.sublime-keymap'
            )
        })


class OpenPreferences(sublime_plugin.WindowCommand):

    def run(self, split: bool = True):
        if split:
            self.window.run_command('edit_settings', {
                "base_file": "${packages}/Default/Preferences.sublime-settings",
                "default": "{\n\t$0\n}\n",
                "user_file": "${packages}/User/Preferences.sublime-settings"
            })
        else:
            self.window.run_command('open_file', {
                'file': os.path.join(
                    packages_path(),
                    'User',
                    'Preferences.sublime-settings'
                )
            })
