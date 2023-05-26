import sublime_plugin


class GeneratePhpunitTest(sublime_plugin.WindowCommand):

    def run(self):
        self.candidates = ['Unit', 'Integration']
        self.window.show_quick_panel(self.candidates, self.on_done)

    def on_done(self, index):
        if index == -1:
            return

        picked = self.candidates[index]

        file_name = self.window.active_view().file_name()
        if not file_name:
            return

        new_file = _get_new_file(file_name, picked)

        if new_file != file_name:
            view = self.window.new_file()
            view.retarget(new_file)


def _get_new_file(file_name: str, picked: str) -> str:
    file_name = file_name.replace('/app/', '/tests/' + picked + '/')
    file_name = file_name.replace('/src/', '/tests/' + picked + '/')
    file_name = file_name.replace('.php', 'Test.php')

    return file_name
