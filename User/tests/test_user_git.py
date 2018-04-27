from User.tests import unittest

from User.user_git import _extract_github_url


class TestUserGitFormatGithubUrl(unittest.ViewTestCase):

    def test_should_not_choke_on_empty_view(self):
        self.fixture('|')
        self.assertEqual(None, _extract_github_url(self.view))

    def test_non_urls_return_none(self):
        self.fixture('|foobar')
        self.assertEqual(None, _extract_github_url(self.view))

    def test_extract_url(self):
        self.fixture('|https://github.com/x/y')
        self.assertEqual('https://github.com/x/y', _extract_github_url(self.view))

        self.fixture('|https://github.com/x/y/issues/2')
        self.assertEqual('https://github.com/x/y/issues/2', _extract_github_url(self.view))

        self.fixture('|x/y')
        self.assertEqual('https://github.com/x/y', _extract_github_url(self.view))

        self.fixture('|x/y#2')
        self.assertEqual('https://github.com/x/y/issues/2', _extract_github_url(self.view))

        self.fixture('|#2')
        self.assertEqual('https://github.com/NeoVintageous/NeoVintageous/issues/2', _extract_github_url(self.view))

    def test_extract_url_with_cursor_in_middle_of_url_string(self):
        self.fixture('https://g|ithub.com/x/y')
        self.assertEqual('https://github.com/x/y', _extract_github_url(self.view))

        self.fixture('https://github.com/x/y/issue|s/2')
        self.assertEqual('https://github.com/x/y/issues/2', _extract_github_url(self.view))

        self.fixture('x|/y')
        self.assertEqual('https://github.com/x/y', _extract_github_url(self.view))

        self.fixture('x/y#|2')
        self.assertEqual('https://github.com/x/y/issues/2', _extract_github_url(self.view))

        self.fixture('#2|12')
        self.assertEqual('https://github.com/NeoVintageous/NeoVintageous/issues/212', _extract_github_url(self.view))
