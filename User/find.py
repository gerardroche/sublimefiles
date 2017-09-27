from sublime_plugin import WindowCommand


def _find_in_open_folders(window, interactive=True):
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

    if not interactive:
        window.run_command('find_all', {
            'close_panel': True
        })


class FindInOpenFoldersCommand(WindowCommand):
    def run(self):
        _find_in_open_folders(self.window)


class FindAllInOpenFoldersCommand(WindowCommand):
    def run(self):
        _find_in_open_folders(self.window, interactive=False)


class ShowFindInFilesCommand(WindowCommand):
    def run(self):
        self.window.run_command('show_panel', {
            'panel': 'find_in_files'
        })


class ShowFindResultsCommand(WindowCommand):
    def run(self):
        for view in self.window.views():
            if view.name() == 'Find Results':
                # Clear any visual selection.
                sel = view.sel()[0].begin()
                view.sel().clear()
                view.sel().add(sel)

                return self.window.focus_view(view)


class HidePhantoms(WindowCommand):

    def run(self):
        self.window.run_command('exec', {
            'hide_phantoms_only': True
        })
