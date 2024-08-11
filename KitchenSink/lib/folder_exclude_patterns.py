# Copyright (C) 2023 Gerard Roche
#
# This file is part of Limitless.
#
# Limitless is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Limitless is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Limitless.  If not, see <https://www.gnu.org/licenses/>.

import sublime
import sublime_plugin

from KitchenSink.lib.utils import save_preferences


class FolderExcludePatterns(sublime_plugin.WindowCommand):

    def input(self, args):
        return FolderExcludePatternInputHandler()

    def run(self, folder_exclude_pattern):
        with save_preferences() as preferences:
            folder_exclude_patterns = preferences.get('folder_exclude_patterns', [])

            if folder_exclude_pattern in folder_exclude_patterns:
                folder_exclude_patterns.remove(folder_exclude_pattern)
            else:
                folder_exclude_patterns.append(folder_exclude_pattern)

            folder_exclude_patterns.sort()
            preferences.set('folder_exclude_patterns', folder_exclude_patterns)


class FolderExcludePatternInputHandler(sublime_plugin.ListInputHandler):

    def list_items(self):
        preferences = sublime.load_settings('Preferences.sublime-settings')

        folder_exclude_patterns = preferences.get('folder_exclude_patterns', [])
        folder_exclude_patterns_default = preferences.get('folder_exclude_patterns_default', [])

        items = []

        for item in folder_exclude_patterns_default:
            if item in folder_exclude_patterns:
                kind = (sublime.KIND_ID_COLOR_GREENISH, "✓", "Exists")
            else:
                kind = sublime.KIND_AMBIGUOUS

            items.append(sublime.ListInputItem(item, item, kind=kind))

        return (items, -1)
