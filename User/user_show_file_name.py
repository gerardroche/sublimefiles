import os

import sublime_plugin


class UserShowFileName(sublime_plugin.EventListener):

    def on_activated_async(self, view):
        file_name = _get_file_name(view)
        if file_name:
            view.set_status('file_name', file_name)


def _get_file_name(view):
    file_name = view.file_name()
    if file_name:
        if 'HOME' in os.environ:
            home = os.environ['HOME']
            if file_name.startswith(home):
                file_name = file_name.replace(home, '~')

        return file_name
