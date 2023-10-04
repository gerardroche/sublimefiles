import sublime_plugin

from User import sublime_ext


class UserAuditPreferences(sublime_plugin.WindowCommand):

    def run(self):
        defaults = sublime_ext.decode_resource('Packages/Default/Preferences.sublime-settings')
        user = sublime_ext.decode_resource('Packages/User/Preferences.sublime-settings')

        for name, value in defaults.items():
            if user.get(name) == value:
                print('Found redundant setting: {}={}'.format(name, value))

            if name in ('file_exclude_patterns', 'folder_exclude_patterns'):
                for exclude_pattern in value:
                    if exclude_pattern not in user.get(name):
                        print('Found exclude pattern missing from ' + name + ':', exclude_pattern)
