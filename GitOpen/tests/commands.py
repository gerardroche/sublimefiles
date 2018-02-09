from sublime import Region
from sublime_plugin import TextCommand


class _git_open_test_setup_fixture(TextCommand):
    def run(self, edit, text):
        self.view.replace(edit, Region(0, self.view.size()), text)
