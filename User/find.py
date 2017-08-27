from sublime_plugin import WindowCommand


def _find_in_open_folders(window):
    view = window.active_view()
    region = view.sel()[0]
    word = view.word(region)
    view.sel().clear()
    view.sel().add(word)

    window.run_command('show_panel', {
        'panel': 'find_in_files',
        'where': '<open folders>'
    })

    view.sel().clear()
    view.sel().add(region)


class FindInOpenFoldersCommand(WindowCommand):
    def run(self):
        _find_in_open_folders(self.window)


class FindAllInOpenFoldersCommand(WindowCommand):

    def run(self):
        _find_in_open_folders(self.window)

        self.window.run_command('find_all', {
            'close_panel': True
        })
