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


import logging
import os

import sublime
import sublime_plugin


class Lumber(sublime_plugin.WindowCommand):

    def run(self):
        self.packages = _packages()
        self.window.show_quick_panel(self.packages, self.on_done_package)

    def on_done_package(self, index: int) -> None:
        if index == -1:
            return

        self.package = self.packages[index]
        self.window.show_quick_panel(_LOG_LEVELS, self.on_done_level)

    def on_done_level(self, index: int) -> None:
        if index == -1:
            return

        logger = self.package
        level_name = _LOG_LEVELS[index]
        level = getattr(logging, level_name, logging.DEBUG)
        logging.getLogger(logger).setLevel(level)

        print('Log level for {} is now {}:{}'.format(logger, level_name, level))


_LOG_LEVELS = [
    'CRITICAL',  # 50
    'ERROR',     # 40
    'WARNING',   # 30
    'INFO',      # 20
    'DEBUG',     # 10
    'NOTSET',    # 0
]


def _packages() -> list:
    packages = []

    packages_path = sublime.packages_path()
    for item in os.listdir(packages_path):
        if not item:
            continue
        if item.startswith('.'):
            continue
        if not os.path.isdir(os.path.join(packages_path, item)):
            continue
        packages.append(item)

    installed_packages = sublime.installed_packages_path()
    for item in os.listdir(installed_packages):
        if not item:
            continue
        if item.startswith('.'):
            continue
        if not os.path.isfile(os.path.join(packages_path, item)):
            continue
        packages.append(item.replace('.sublime-package', ''))

    return packages
