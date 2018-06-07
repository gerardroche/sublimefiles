# When you see something you like and would like to use it, open an issue about
# abstracting it out into a reusable package, possibly installable via Package
# Control.

import sublime
import sublime_plugin


def _load_preferences():
    return sublime.load_settings('Preferences.sublime-settings')


def _save_preferences():
    sublime.save_settings('Preferences.sublime-settings')


class ExcludePatternsCommand(sublime_plugin.WindowCommand):

    def run(self, action):
        if action == 'disable':
            preferences = _load_preferences()
            preferences.set('file_exclude_patterns', [])
            preferences.set('folder_exclude_patterns', [])
            _save_preferences()
        elif action == 'reset':
            view = self.window.active_view()
            if not view:
                raise ValueError('view is requied')

            preferences = _load_preferences()
            do_save = False

            file_exclude_patterns = view.settings().get('file_exclude_patterns_default')
            if file_exclude_patterns:
                preferences.set('file_exclude_patterns', file_exclude_patterns)
                do_save = True

            folder_exclude_patterns = view.settings().get('folder_exclude_patterns_default')
            if folder_exclude_patterns:
                preferences.set('folder_exclude_patterns', folder_exclude_patterns)
                do_save = True

            if do_save:
                _save_preferences()
        else:
            raise ValueError('unknown action {}'.format(action))
