import logging
import os
import sys

from sublime import active_window
from sublime import log_build_systems
from sublime import log_commands
from sublime import log_indexing
from sublime import log_input
from sublime import log_result_regex
from sublime import packages_path
from sublime_plugin import ApplicationCommand
from sublime_plugin import TextCommand


_DEBUG = bool(os.getenv('SUBLIME_DEBUG'))


class ToggleDebugModeCommand(ApplicationCommand):
    def run(self):
        global _DEBUG
        _DEBUG = not _DEBUG
        _sublime_log(_DEBUG)

        file = os.path.join(packages_path(), 'User', '.debug')
        if os.path.isfile(file):
            if not _DEBUG:
                os.remove(file)
        else:
            if _DEBUG:
                with open(file, 'w+', encoding='utf8') as f:
                    f.write('')


class DebugViewToScopeCommand(TextCommand):
    def run(self, edit):
        scopes = []
        for point in range(self.view.size()):
            scopes.append(self.view.scope_name(point).strip())

        print('>>>')
        print("\n".join(scopes))
        print('<<<')


def _sublime_log(flag):
    log_commands(flag)
    log_input(flag)
    log_result_regex(flag)
    # log_indexing(flag)
    log_build_systems(flag)


def plugin_loaded():
    global _DEBUG

    log_indexing(False)  # disable it by default

    file = os.path.join(packages_path(), 'User', '.debug')
    if os.path.isfile(file):
        _DEBUG = True

    if _DEBUG:
        print('DEBUG User: debug is enabled')
        active_window().run_command('show_panel', {'panel': 'console'})
        _sublime_log(True)

        print('DEBUG User: python v{}.{}.{} ({})'.format(
            sys.version_info[0],
            sys.version_info[1],
            sys.version_info[2],
            sys.version_info
        ))

        print('DEBUG User: paths = {}'.format(sys.path))
        print('DEBUG User: abiflags = {}, flags = {}'.format(sys.abiflags, sys.flags))
        print('                       Legend = attribute: flag, debug: -d, inspect: -i, interactive: -i, optimize: -O or -OO, dont_write_bytecode: -B, no_user_site: -s, no_site: -S, ignore_environment: -E, verbose: -v, bytes_warning: -b, quiet: -q, hash_randomization: -R')  # noqa: E501
        print('DEBUG User: platform = {} (Linux: \'linux\', Windows: \'win32\', Windows/Cygwin: \'cygwin\', Mac OS X: \'darwin\')'.format(sys.platform))  # noqa: E501

        window = active_window()
        if not window:
            return

        view = window.active_view()
        if not view:
            return

        settings = view.settings()
        if not settings:
            return

        if not settings.get('user.debug'):
            return

        print('DEBUG User: \'user.debug\' is enabled')

        if settings.get('user.debug.neovintageous'):
            neovintageous_debug_settings = settings.get('user.debug.neovintageous')
            print('DEBUG User: \'user.debug.neovintageous\' =', neovintageous_debug_settings)

            if isinstance(neovintageous_debug_settings, dict):
                if 'level' in neovintageous_debug_settings:
                    logging.getLogger('NeoVintageous').setLevel(getattr(
                        logging,
                        neovintageous_debug_settings['level'].strip().upper(),
                        logging.DEBUG
                    ))
