from sublime import decode_value
from sublime import load_resource
import sublime_plugin


def decode_resource(name: str):
    return decode_value(load_resource(name))


class KitchenSinkAuditPreferences(sublime_plugin.WindowCommand):

    def run(self):
        defaults = decode_resource('Packages/Default/Preferences.sublime-settings')
        user = decode_resource('Packages/User/Preferences.sublime-settings')

        for name, value in defaults.items():
            if user.get(name) == value:
                print('Found redundant setting: {}={}'.format(name, value))

            if name in ('file_exclude_patterns', 'folder_exclude_patterns'):
                for exclude_pattern in value:
                    if exclude_pattern not in user.get(name):
                        print('Found exclude pattern missing from ' + name + ':', exclude_pattern)
