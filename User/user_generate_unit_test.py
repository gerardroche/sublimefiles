import sublime_plugin


class GenerateUnitTest(sublime_plugin.WindowCommand):

    def run(self):
        self.candidates = [
            'Unit',
            'Integration'
        ]

        self.window.show_quick_panel(self.candidates, self.on_done)

    def on_done(self, index):
        if index == -1:
            return

        picked = self.candidates[index]

        test_case = self.window().active_view().file_name()
        test_case = test_case.replace('app/', 'tests/' + str(picked) + '/')
        test_case = test_case.replace('.php', 'Test.php')

        self.window().open_file(test_case)
