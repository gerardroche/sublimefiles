from contextlib import contextmanager

import sublime
import sublime_plugin


@contextmanager
def save_preferences():
    yield sublime.load_settings('Preferences.sublime-settings')
    sublime.save_settings('Preferences.sublime-settings')


class ExcludePatternsCommand(sublime_plugin.WindowCommand):

    def run(self, action):
        if action == 'disable':
            with save_preferences() as preferences:
                preferences.set('file_exclude_patterns', [])
                preferences.set('folder_exclude_patterns', [])
        elif action == 'reset':
            view = self.window.active_view()
            if not view:
                raise ValueError('view is requied')

            with save_preferences() as preferences:
                file_exclude_patterns = view.settings().get('file_exclude_patterns_default')
                if file_exclude_patterns:
                    preferences.set('file_exclude_patterns', file_exclude_patterns)

                folder_exclude_patterns = view.settings().get('folder_exclude_patterns_default')
                if folder_exclude_patterns:
                    preferences.set('folder_exclude_patterns', folder_exclude_patterns)
