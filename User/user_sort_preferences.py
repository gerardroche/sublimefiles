import sublime_plugin

from User import sublime_ext


class UserSortPreferences(sublime_plugin.WindowCommand):

    def run(self):
        with sublime_ext.save_preferences() as preferences:
            self.sort_added_words(preferences)
            self.sort_ignored_packages(preferences)
            self.sort_ignored_words(preferences)
            self.sort_index_exclude_patterns(preferences)
            self.sort_file_exclude_patterns(preferences)

    def sort_added_words(self, preferences):
        added_words = preferences.get('added_words', [])
        added_words = list(set(added_words))
        added_words.sort()
        if added_words:
            preferences.set('added_words', added_words)

    def sort_ignored_packages(self, preferences):
        ignored_packages = preferences.get('ignored_packages', [])
        ignored_packages = list(set(ignored_packages))
        ignored_packages.sort()
        if ignored_packages:
            preferences.set('ignored_packages', ignored_packages)

    def sort_ignored_words(self, preferences):
        ignored_words = preferences.get('ignored_words', [])
        ignored_words = list(set(ignored_words))
        ignored_words.sort()
        if ignored_words:
            preferences.set('ignored_words', ignored_words)

    def sort_index_exclude_patterns(self, preferences):
        index_exclude_patterns = preferences.get('index_exclude_patterns', [])
        index_exclude_patterns = list(set(index_exclude_patterns))
        index_exclude_patterns.sort()
        if index_exclude_patterns:
            preferences.set('index_exclude_patterns', index_exclude_patterns)

    def sort_file_exclude_patterns(self, preferences):
        file_exclude_patterns = preferences.get('file_exclude_patterns', [])
        file_exclude_patterns = list(set(file_exclude_patterns))
        file_exclude_patterns.sort()
        if file_exclude_patterns:
            preferences.set('file_exclude_patterns', file_exclude_patterns)

    def sort_folder_exclude_patters(self, preferences):
        folder_exclude_patterns = preferences.get('folder_exclude_patterns', [])
        folder_exclude_patterns = list(set(folder_exclude_patterns))
        folder_exclude_patterns.sort()
        if folder_exclude_patterns:
            preferences.set('folder_exclude_patterns', folder_exclude_patterns)
