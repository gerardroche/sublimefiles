from sublime_plugin import WindowCommand


class FindCommand(WindowCommand):

    def run(self):

        view = self.window.active_view()
        region = view.sel()[0]
        word = view.word(region)
        view.sel().clear()
        view.sel().add(word)

        where = ','.join(self.window.folders())

        self.window.run_command('show_panel', {
            'panel': 'find_in_files',
            'where': where
        })

        view.sel().clear()
        view.sel().add(region)

        self.window.run_command('find_all', {
            'close_panel': True
        })
