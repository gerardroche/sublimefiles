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
