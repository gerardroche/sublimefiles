# When you see something you like and would like to use it, open an issue about
# abstracting it out into a reusable package, possibly installable via Package
# Control.

from sublime import load_settings
from sublime import save_settings
import sublime_plugin


_toggle_hidden_folders = [
    'tmp'
]


_toggle_hidden_files = [
    '.gitignore',
    '.gitattributes',
    '.travis.yml',
    '.coveragerc',
    '.flake8',
    '*.sublime-project'
]


class ToggleHiddenFilesAndFoldersCommand(sublime_plugin.WindowCommand):

    def run(self):
        settings = load_settings('Preferences.sublime-settings')

        file_exclude_patterns = sorted(settings.get('file_exclude_patterns', []))
        files = sorted(list(set(file_exclude_patterns + _toggle_hidden_files)))

        folder_exclude_patterns = sorted(settings.get('folder_exclude_patterns', []))
        folders = sorted(list(set(folder_exclude_patterns + _toggle_hidden_folders)))

        if files == file_exclude_patterns and folders == folder_exclude_patterns:
            files = [p for p in file_exclude_patterns if p not in _toggle_hidden_files]
            folders = [p for p in folder_exclude_patterns if p not in _toggle_hidden_folders]

        settings.set('file_exclude_patterns', sorted(files))
        settings.set('folder_exclude_patterns', sorted(folders))

        save_settings('Preferences.sublime-settings')


class ToggleProjectHiddenFilesAndFoldersCommand(sublime_plugin.WindowCommand):

    def run(self):
        project_file_name = self.window.project_file_name()
        if not project_file_name:
            return

        project_data = self.window.project_data()
        if not project_data:
            return

        hide = True
        for folder in project_data['folders']:
            if 'file_exclude_patterns' in folder:
                if '.gitignore' in folder['file_exclude_patterns']:
                    hide = False
                    break

        for folder in project_data['folders']:
            if 'file_exclude_patterns' in folder:
                file_exclude_patterns = folder['file_exclude_patterns']
            else:
                file_exclude_patterns = []

            if 'folder_exclude_patterns' in folder:
                folder_exclude_patterns = folder['folder_exclude_patterns']
            else:
                folder_exclude_patterns = []

            if hide:
                file_exclude_patterns += _toggle_hidden_files
                folder_exclude_patterns += _toggle_hidden_folders
            else:
                for hidden_file in _toggle_hidden_files:
                    if hidden_file in folder['file_exclude_patterns']:
                        file_exclude_patterns.remove(hidden_file)

                for hidden_folder in _toggle_hidden_folders:
                    if hidden_folder in folder['folder_exclude_patterns']:
                        folder_exclude_patterns.remove(hidden_folder)

            file_exclude_patterns = sorted(set(file_exclude_patterns))
            folder_exclude_patterns = sorted(set(folder_exclude_patterns))

            if file_exclude_patterns:
                folder['file_exclude_patterns'] = file_exclude_patterns
            else:
                del folder['file_exclude_patterns']

            if folder_exclude_patterns:
                folder['folder_exclude_patterns'] = folder_exclude_patterns
            else:
                del folder['folder_exclude_patterns']

        self.window.set_project_data(project_data)


class ToggleFolderExcludePatternCommand(sublime_plugin.WindowCommand):

    def run(self, pattern):
        preferences = load_settings('Preferences.sublime-settings')

        folder_exclude_patterns = preferences.get('folder_exclude_patterns', [])

        if pattern not in folder_exclude_patterns:
            folder_exclude_patterns.append(pattern)
        else:
            folder_exclude_patterns.remove(pattern)

        folder_exclude_patterns.sort()
        preferences.set('folder_exclude_patterns', folder_exclude_patterns)

        save_settings('Preferences.sublime-settings')
