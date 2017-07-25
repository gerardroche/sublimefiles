import os
import logging

import sublime
from sublime_plugin import ApplicationCommand
from sublime_plugin import EventListener
from sublime_plugin import TextCommand


_DEBUG = bool(os.getenv('SUBLIME_DEBUG'))

_AUTO_SHOW_CONSOLE_ON_LOAD = True


def _set_sublime_log(flag):
    sublime.log_commands(flag)
    sublime.log_input(flag)
    sublime.log_result_regex(flag)
    sublime.log_indexing(flag)
    sublime.log_build_systems(flag)


class ToggleDebugModeCommand(ApplicationCommand):

    def run(self):
        global _DEBUG
        _DEBUG = not _DEBUG
        _set_sublime_log(_DEBUG)


class DebugViewToScopeCommand(TextCommand):
    def run(self, edit):
        scopes = []
        for point in range(self.view.size()):
            scopes.append(self.view.scope_name(point).strip())

        print('>>>')
        print("\n".join(scopes))
        print('<<<')


class UserReloadPackageEventListener(EventListener):
    def on_post_save(self, view):
        file = view.file_name()
        if not file.endswith('.py'):
            return

        package_name = None
        candidates = sublime.find_resources('*.reload-package')
        for candidate in candidates:
            candidate_package = os.path.basename(os.path.dirname(candidate))
            if '/' + candidate_package + '/' in file and 'tests' not in file:
                package_name = candidate_package
                # print('')
                # print('ReloadPackageListener: file=', file)
                # print('ReloadPackageListener: package=', package_name)
                # print('ReloadPackageListener: candidates=', candidates)
                break

        if package_name:

            # Try to reset loggers
            logger = logging.getLogger()
            for handler in list(logger.handlers):
                del logger.handlers[0]
            logger = logging.getLogger(package_name)
            for handler in list(logger.handlers):
                del logger.handlers[0]

            sublime.active_window().run_command('unit_testing_reload_current_project', {
                'pkg_name': package_name,
                'show_console': False
            })

            def reload_user_package():
                sublime.active_window().run_command('unit_testing_reload_current_project', {
                    'pkg_name': 'User',
                    'show_console': False
                })

            def cleanup_loggers():
                logger = logging.getLogger('NeoVintageous')
                if len(logger.handlers) >= 3:
                    del logger.handlers[2]

            sublime.set_timeout_async(cleanup_loggers, 1500)


def _is_debug():
    if _DEBUG:
        return True

    packages_debug_flag_file = os.path.join(sublime.packages_path(), '.debug')
    if os.path.isfile(packages_debug_flag_file):
        return True

    user_debug_flag_file = os.path.join(sublime.packages_path(), 'User', '.debug')
    if os.path.isfile(user_debug_flag_file):
        return True

    return False


def plugin_loaded():

    is_debug = _is_debug()

    if is_debug:
        print('DEBUG User: debug is enabled')

    if is_debug or _AUTO_SHOW_CONSOLE_ON_LOAD:
        sublime.active_window().run_command('show_panel', {'panel': 'console'})

    if is_debug:
        _set_sublime_log(True)

        import sys
        print('DEBUG User: abiflags = {}'.format(sys.abiflags))
        print('DEBUG User: paths = {}'.format(sys.path))
        print('DEBUG User: flags = {}'.format(sys.flags))
        print("""
            attribute             flag
            debug                 -d
            inspect               -i
            interactive           -i
            optimize              -O or -OO
            dont_write_bytecode   -B
            no_user_site          -s
            no_site               -S
            ignore_environment    -E
            verbose               -v
            bytes_warning         -b
            quiet                 -q
            hash_randomization    -R
        """)
        print('DEBUG User: platform = {}'.format(sys.platform))
        print("""
            Linux           'linux'
            Windows         'win32'
            Windows/Cygwin  'cygwin'
            Mac OS X        'darwin'
        """)
        print('DEBUG User: version = {}.{}.{} ({})'.format(
            sys.version_info[0],
            sys.version_info[1],
            sys.version_info[2],
            sys.version_info
        ))

        window = sublime.active_window()
        if not window:
            return

        view = window.active_view()
        if not view:
            return

        settings = view.settings()
        if not settings:
            return

        # Experimental plugin debugging configuration
        if not settings.get('user.debug'):
            return

        if settings.get('user.debug.neovintageous'):
            neovintageous_debug_settings = settings.get('user.debug.neovintageous')
            print('DEBUG User: Neovintageous debug settings: ', neovintageous_debug_settings)
            if isinstance(neovintageous_debug_settings, dict):
                import logging
                if 'level' in neovintageous_debug_settings:
                    neovontageous_debug_level = neovintageous_debug_settings['level'].strip().upper()
                    print('DEBUG User: set Neovintageous level to ' + str(neovontageous_debug_level))
                    logging.getLogger('NeoVintageous').setLevel(getattr(
                        logging,
                        neovontageous_debug_level,
                        logging.DEBUG
                    ))
