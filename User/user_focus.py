from contextlib import contextmanager

import sublime
import sublime_plugin


class Focus(sublime_plugin.WindowCommand):

    def run(self):
        with save_preferences() as preferences:
            files = preferences.get('file_exclude_patterns_focus')
            _update(preferences, 'file_exclude_patterns', files)
            folders = preferences.get('folder_exclude_patterns_focus')
            _update(preferences, 'folder_exclude_patterns', folders)


@contextmanager
def save_preferences():
    yield sublime.load_settings('Preferences.sublime-settings')
    sublime.save_settings('Preferences.sublime-settings')


def _update(preferences, name: str, items: list) -> None:
    exclude_patterns = preferences.get(name)
    if not isinstance(exclude_patterns, list):
        return

    for item in items:
        if item in exclude_patterns:
            exclude_patterns.remove(item)
        else:
            exclude_patterns.append(item)

        exclude_patterns = list(set(exclude_patterns))
        exclude_patterns.sort()

        if exclude_patterns:
            preferences.set(name, exclude_patterns)
