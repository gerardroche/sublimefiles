import os

from sublime import set_clipboard
import sublime_plugin


class CopyRelativeFilePathCommand(sublime_plugin.WindowCommand):

    def run(self):
        rel_file_name = self.get_relative_file_name()
        if rel_file_name:
            set_clipboard(rel_file_name)

    def get_relative_file_name(self):
        view = self.window.active_view()

        file_name = view.file_name()
        if not file_name:
            return

        # If the file path starts with any of the open folders then the file is
        # relative to that folder, otherwise it's relative to the use home dir.
        folders = self.window.folders()
        folders.sort()
        for folder in folders:
            if file_name.startswith(folder):
                return file_name.replace(folder + '/', '')

        return file_name.replace(os.path.expanduser('~') + '/', '')
