import os

from sublime import packages_path
from sublime import status_message
from sublime_plugin import WindowCommand


class PythonTestSwitchCommand(WindowCommand):

    def run(self):
        view = self.window.active_view()
        if not view:
            return status_message('view not found')

        file_name = view.file_name()
        if not file_name:
            return status_message('file name not found')

        for package in os.listdir(packages_path()):
            if package[0] == '.':
                continue

            file_path = os.path.join(packages_path(), package)
            if not os.path.isdir(file_path):
                continue

            package_pos = file_name.find('/' + package + '/')
            if package_pos >= 0:
                sp = file_name.split('/' + package + '/')
                if sp:
                    head, tail = os.path.split(sp[1])
                    file = os.path.join(sp[0], package, 'tests', head, 'test_' + tail)
                    if os.path.isfile(file):
                        self.window.open_file(file)
