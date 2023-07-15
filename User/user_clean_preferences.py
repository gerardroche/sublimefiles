import sublime
import sublime_plugin


class UserCleanPreferences(sublime_plugin.WindowCommand):

    def run(self):
        preferences = _load_preferences('Packages/User/Preferences.sublime-settings')
        defaults = _load_preferences('Packages/Default/Preferences.sublime-settings')

        print('')
        print('Checking for redundant settings ...')
        print('')
        for x, y in defaults.items():
            if preferences.get(x) == y:
                print('  Found', x, y)


def _load_preferences(path: str):
    return sublime.decode_value(sublime.load_resource(path))
