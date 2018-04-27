import os

from sublime import load_settings

from User.tests import unittest

from User.user_syntastic import _build_cmd


class TestSyntastic(unittest.ViewTestCase):

    def setUp(self):
        # Erase any user settings so that they don't impact tests.
        self._settings = {}
        self._preferences = load_settings('Preferences.sublime-settings')

        keys = [
            'syntastic_php_php_exec',
            'syntastic_php_php_args',
            'syntastic_python_flake8_exec',
            'syntastic_python_flake8_args'
        ]

        for key in keys:
            if self._preferences.has(key):
                self._settings[key] = self._preferences.get(key)
                self._preferences.erase(key)

        super().setUp()

    def tearDown(self):
        super().tearDown()
        for key, value in self._settings.items():
            self._preferences.set(key, value)

    def test_build_cmd_defaults(self):
        # python/flake8
        self.view.file_name = unittest.mock.Mock(return_value='/tmp/mock.py')
        self.assertEqual([
            'flake8',
            '/tmp/mock.py'
        ], _build_cmd(self.view, 'python', 'flake8'))

        # php/php
        self.view.file_name = unittest.mock.Mock(return_value='/tmp/mock.php')
        self.assertEqual([
            'php',
            '-d', 'error_reporting=E_ALL',
            '-l',
            '-d', 'error_logs=',
            '-d', 'display_errors=1',
            '-d', 'log_errors=0',
            '-d', 'xdebug.cli_color=0',
            '/tmp/mock.php'
        ], _build_cmd(self.view, 'php', 'php'))

    def test_build_cmd_user_can_set_executable(self):
        # python/flake8
        self.view.file_name = unittest.mock.Mock(return_value='/tmp/mock.py')
        self.view.settings().set('syntastic_python_flake8_exec', '~/.local/bin/flake8')
        self.assertEqual([
            os.path.expanduser('~/.local/bin/flake8'),
            '/tmp/mock.py'
        ], _build_cmd(self.view, 'python', 'flake8'))

        # php/php
        self.view.file_name = unittest.mock.Mock(return_value='/tmp/mock.php')
        self.view.settings().set('syntastic_php_php_exec', '~/.phpenv/versions/7.x/bin/php')
        self.assertEqual([
            os.path.expanduser('~/.phpenv/versions/7.x/bin/php'),
            '-d', 'error_reporting=E_ALL',
            '-l',
            '-d', 'error_logs=',
            '-d', 'display_errors=1',
            '-d', 'log_errors=0',
            '-d', 'xdebug.cli_color=0',
            '/tmp/mock.php'
        ], _build_cmd(self.view, 'php', 'php'))

    def test_build_cmd_user_can_set_args(self):
        # python/flake8
        self.view.file_name = unittest.mock.Mock(return_value='/tmp/mock.py')
        self.view.settings().set('syntastic_python_flake8_args', ['--max-complexity=15', '--ignore=E121'])
        self.assertEqual([
            'flake8',
            '--max-complexity=15',
            '--ignore=E121',
            '/tmp/mock.py'
        ], _build_cmd(self.view, 'python', 'flake8'))

        # php/php
        self.view.file_name = unittest.mock.Mock(return_value='/tmp/mock.php')
        self.view.settings().set('syntastic_php_php_args', ['-d', 'xdebug.scream=0'])
        self.assertEqual([
            'php',
            '-d', 'xdebug.scream=0',
            '-l',
            '-d', 'error_logs=',
            '-d', 'display_errors=1',
            '-d', 'log_errors=0',
            '-d', 'xdebug.cli_color=0',
            '/tmp/mock.php'
        ], _build_cmd(self.view, 'php', 'php'))

    def test_build_cmd_user_can_set_post_args(self):
        # python/flake8
        self.view.file_name = unittest.mock.Mock(return_value='/tmp/mock.py')
        self.view.settings().set('syntastic_python_flake8_post_args', ['--max-complexity=15', '--ignore=D100,D101'])
        self.assertEqual([
            'flake8',
            '/tmp/mock.py',
            '--max-complexity=15',
            '--ignore=D100,D101',
        ], _build_cmd(self.view, 'python', 'flake8'))

        # php/php
        self.view.file_name = unittest.mock.Mock(return_value='/tmp/mock.php')
        self.view.settings().set('syntastic_php_php_post_args', ['-d', 'xdebug.scream=0'])
        self.assertEqual([
            'php',
            '-d', 'error_reporting=E_ALL',
            '-l',
            '-d', 'error_logs=',
            '-d', 'display_errors=1',
            '-d', 'log_errors=0',
            '-d', 'xdebug.cli_color=0',
            '/tmp/mock.php',
            '-d', 'xdebug.scream=0',
        ], _build_cmd(self.view, 'php', 'php'))
