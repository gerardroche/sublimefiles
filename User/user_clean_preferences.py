import sublime
import sublime_plugin


class UserCleanPreferences(sublime_plugin.WindowCommand):

    def run(self):
        defaults = _load_preferences('Packages/Default/Preferences.sublime-settings')
        user = _load_preferences('Packages/User/Preferences.sublime-settings')

        for name, value in defaults.items():
            if user.get(name) == value:
                print('Found redundant setting:', name, value)

            if name in ('file_exclude_patterns', 'folder_exclude_patterns'):
                for exclude_pattern in value:
                    if exclude_pattern not in user.get(name):
                        print('Found exclude pattern missing from ' + name + ':', exclude_pattern)


def _load_preferences(path: str):
    return sublime.decode_value(sublime.load_resource(path))
