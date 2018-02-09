import unittest

# Use aliases to indicate that they are not public testing APIs.
from sublime import active_window as _active_window

from sublime import Region


class ViewTestCase(unittest.TestCase):

    def setUp(self):
        self.view = _active_window().new_file()
        self.view.set_scratch(True)

    def tearDown(self):
        if self.view:
            self.view.close()

    def fixture(self, text):
        self.view.run_command('_git_open_test_setup_fixture', {'text': text.replace('|', '')})
        sels = [i for i, c in enumerate(text) if c == '|']
        if sels:
            self.view.sel().clear()
            for i, x in enumerate(sels):
                self.view.sel().add(x - i)

    def content(self):
        # type: () -> str
        return self.view.substr(Region(0, self.view.size()))
