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


import sublime
import sublime_plugin

from KitchenSink.lib.utils import save_preferences


class FileExcludePatterns(sublime_plugin.WindowCommand):

    def input(self, args):
        return FileExcludePatternInputHandler()

    def run(self, file_exclude_pattern):
        _run('file_exclude_patterns', file_exclude_pattern)


class FileExcludePatternInputHandler(sublime_plugin.ListInputHandler):

    def list_items(self):
        return _list_items('file_exclude_patterns')


class FolderExcludePatterns(sublime_plugin.WindowCommand):

    def input(self, args):
        return FolderExcludePatternInputHandler()

    def run(self, folder_exclude_pattern):
        _run('folder_exclude_patterns', folder_exclude_pattern)


class FolderExcludePatternInputHandler(sublime_plugin.ListInputHandler):

    def list_items(self):
        return _list_items('folder_exclude_patterns')


def _list_items(key: str):
    preferences = sublime.load_settings('Preferences.sublime-settings')

    exclude_patterns = preferences.get(key, [])
    exclude_patterns_default = preferences.get(key + '_default', [])

    items = []

    for item in exclude_patterns_default:  # type: ignore
        if item in exclude_patterns:  # type: ignore
            kind = (sublime.KIND_ID_COLOR_GREENISH, "✓", "Exists")
        else:
            kind = sublime.KIND_AMBIGUOUS

        items.append(sublime.ListInputItem(item, item, kind=kind))

    return (items, -1)


def _run(key: str, exclude_pattern: str) -> None:
    with save_preferences() as preferences:
        exclude_patterns = preferences.get(key, [])

        if exclude_pattern in exclude_patterns:
            exclude_patterns.remove(exclude_pattern)
        else:
            exclude_patterns.append(exclude_pattern)

        exclude_patterns.sort()
        preferences.set(key, exclude_patterns)
