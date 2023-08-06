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
