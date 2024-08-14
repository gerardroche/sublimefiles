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

import sys

import sublime
import sublime_plugin


class KitchenSinkDumpInfo(sublime_plugin.WindowCommand):

    def run(self):
        print('+-------------------')
        print('| Sublime Text version               ', sublime.version())
        print('| Python version                      {}.{}.{} {}{}'.format(
            sys.version_info[0],
            sys.version_info[1],
            sys.version_info[2],
            sys.version_info[3],
            sys.version_info[4]))
        print('| %-35s %s' % ('sys.flags', sys.flags))
        print('| %-35s %s' % ('sys.abiflags', sys.abiflags))
        print('| %-35s %s' % ('sys.path', sys.path))
        print('| %-35s %s' % ('__debug__', __debug__))
        print('| sublime.platform()                 ', sublime.platform())
        print('| sublime.arch()                     ', sublime.arch())
        print('| sublime.channel()                  ', sublime.channel())
        print('| sublime.executable_path()          ', sublime.executable_path())
        print('| sublime.packages_path()            ', sublime.packages_path())
        print('| sublime.installed_packages_path()  ', sublime.installed_packages_path())
        print('| sublime.cache_path():              ', sublime.cache_path())
        print(sublime.ui_info())
        print(sublime.get_macro())
        print('+')
