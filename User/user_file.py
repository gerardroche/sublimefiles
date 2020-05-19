import os

from sublime import set_clipboard
import sublime_plugin


class CopyRelativeFilePathCommand(sublime_plugin.WindowCommand):

    def run(self):
        value = self.get_relative_file_name()
        set_clipboard(value)

    def get_relative_file_name(self):
        view = self.window.active_view()

        fn = view.file_name()

        # If the file path starts with any of the open folders then the file is
        # relative to that folder, otherwise it's relative to the use home dir.

        folders = self.window.folders()
        folders.sort()
        for folder in folders:
            if fn.startswith(folder):
                return fn.replace(folder + '/', '')

        return fn.replace(os.path.expanduser('~') + '/', '')
