from sublime import Region
import sublime_plugin


class _user_setup_test_fixture(sublime_plugin.TextCommand):

    def run(self, edit, text):
        self.view.replace(edit, Region(0, self.view.size()), text)
