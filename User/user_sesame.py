# When you see something you like and would like to use it, open an issue about
# abstracting it out into a reusable package, possibly installable via Package
# Control.

import os

from sublime import packages_path
import sublime_plugin


class OpenKeyBindingsCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.run_command('open_file', {
            'file': os.path.join(
                packages_path(),
                'User',
                'Default (Linux).sublime-keymap'
            )
        })


class OpenPreferencesCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.run_command('open_file', {
            'file': os.path.join(
                packages_path(),
                'User',
                'Preferences.sublime-settings'
            )
        })
