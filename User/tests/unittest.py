import unittest

from unittest import mock  # noqa: F401

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
        self.view.run_command('_user_setup_test_fixture', {'text': text.replace('|', '')})
        sels = [i for i, c in enumerate(text) if c == '|']
        if sels:
            self.view.sel().clear()
            for i, x in enumerate(sels):
                self.view.sel().add(x - i)

    def content(self):
        return self.view.substr(Region(0, self.view.size()))
