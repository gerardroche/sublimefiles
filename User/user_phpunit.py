import re
import sys

import sublime
import sublime_plugin


class GenerateUnitTestCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        self.candidates = [
            'Unit',
            'Integration'
        ]

        self.view.window().show_quick_panel(self.candidates, self.on_done)

    def on_done(self, index):
        if index == -1:
            return

        picked = self.candidates[index]

        test_case = self.view.file_name()
        test_case = test_case.replace('app/', 'tests/' + str(picked) + '/')
        test_case = test_case.replace('.php', 'Test.php')

        self.view.window().open_file(test_case)
