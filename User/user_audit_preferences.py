import sublime
import sublime_plugin


class UserAuditPreferences(sublime_plugin.WindowCommand):

    def run(self):
        defaults = _decode_resource('Packages/Default/Preferences.sublime-settings')
        user = _decode_resource('Packages/User/Preferences.sublime-settings')

        for name, value in defaults.items():
            if user.get(name) == value:
                print('Found redundant setting: {}={}'.format(name, value))

            if name in ('file_exclude_patterns', 'folder_exclude_patterns'):
                for exclude_pattern in value:
                    if exclude_pattern not in user.get(name):
                        print('Found exclude pattern missing from ' + name + ':', exclude_pattern)


def _decode_resource(path: str):
    return sublime.decode_value(sublime.load_resource(path))
