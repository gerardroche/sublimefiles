# Copyright (C) 2024 Gerard Roche
#
# This file is part of KitchenSink.
#
# KitchenSink is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# KitchenSink is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with KitchenSink.  If not, see <https://www.gnu.org/licenses/>.


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
