from contextlib import contextmanager

import sublime
import sublime_plugin


@contextmanager
def save_preferences():
    yield sublime.load_settings('Preferences.sublime-settings')
    sublime.save_settings('Preferences.sublime-settings')


class SortUserSettingsCommand(sublime_plugin.WindowCommand):

    def run(self):
        with save_preferences() as preferences:
            # added_words
            added_words = preferences.get('added_words', [])
            added_words = list(set(added_words))
            added_words.sort()
            preferences.set('added_words', added_words)

            # ignored_packages
            ignored_packages = preferences.get('ignored_packages', [])
            ignored_packages = list(set(ignored_packages))
            ignored_packages.sort()
            preferences.set('ignored_packages', ignored_packages)

            # ignored_words
            ignored_words = preferences.get('ignored_words', [])
            ignored_words = list(set(ignored_words))
            ignored_words.sort()
            preferences.set('ignored_words', ignored_words)

            # index_exclude_patterns
            index_exclude_patterns = preferences.get('index_exclude_patterns', [])
            index_exclude_patterns = list(set(index_exclude_patterns))
            index_exclude_patterns.sort()
            preferences.set('index_exclude_patterns', index_exclude_patterns)

            # file_exclude_patterns
            file_exclude_patterns = preferences.get('file_exclude_patterns', [])
            file_exclude_patterns = list(set(file_exclude_patterns))
            file_exclude_patterns.sort()
            preferences.set('file_exclude_patterns', file_exclude_patterns)

            # folder_exclude_patterns
            folder_exclude_patterns = preferences.get('folder_exclude_patterns', [])
            folder_exclude_patterns = list(set(folder_exclude_patterns))
            folder_exclude_patterns.sort()
            preferences.set('folder_exclude_patterns', folder_exclude_patterns)
