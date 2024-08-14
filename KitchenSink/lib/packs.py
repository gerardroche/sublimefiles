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

import os

import sublime
import sublime_plugin

from KitchenSink.lib.utils import save_preferences


class Packs(sublime_plugin.WindowCommand):

    def input(self, args):
        return PackageInputHandler()

    def run(self, package):
        with save_preferences() as preferences:
            ignored_packages = preferences.get('ignored_packages', [])

            if package in ignored_packages:
                ignored_packages.remove(package)
            else:
                ignored_packages.append(package)

            ignored_packages.sort()
            preferences.set('ignored_packages', ignored_packages)


class PackageInputHandler(sublime_plugin.ListInputHandler):

    def list_items(self):
        preferences = sublime.load_settings('Preferences.sublime-settings')

        ignored_packages = preferences.get('ignored_packages', [])

        items = []

        for pack in _packs():
            if pack in ignored_packages:
                kind = sublime.KIND_AMBIGUOUS
            else:
                kind = (sublime.KIND_ID_COLOR_GREENISH, "✓", "Exists")

            items.append(sublime.ListInputItem(pack, pack, kind=kind))

        return (items, -1)


def _packs():
    for item in _listdir(sublime.packages_path()):
        yield item

    for item in _listdir(sublime.installed_packages_path()):
        yield item

    # lib_path = os.path.join(os.path.dirname(sublime.packages_path()), 'Lib', 'python38')
    # for item in _listdir(lib_path):
    #     yield item


def _listdir(path: str):
    for name in os.listdir(path):
        if name.startswith('.'):
            continue

        hidden_marker_file = os.path.join(path, name, '.hidden-sublime-package')
        if os.path.exists(hidden_marker_file):
            continue

        yield name
