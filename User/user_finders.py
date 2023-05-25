import os

import sublime_plugin


class TestCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        print('1kwargs =', kwargs)


class TestAgainCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        print('2kwargs =', kwargs)


class TestChainCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        print('chain..')

        commands = [
            ('test', {'k': 'x'}),
            ('test_again', {'y': 'z'})
        ]

        for command, args in commands:
            self.window.run_command(command, args)


class FindInOpenFoldersCommand(sublime_plugin.WindowCommand):

    def run(self, **kwargs):
        _find_in_open_folders(self.window, **kwargs)


class FindFileUnderCursorCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        self.view.window().run_command('show_overlay', {
            'overlay': 'goto',
            'show_files': True,
            'text': self.getWordUnderCursor(),
        })

    def getWordUnderCursor(self) -> str:
        sel = self.view.sel()[0]
        pt = sel.b - 1 if sel.b > sel.a else sel.a
        region = self.view.word(pt)
        word = self.view.substr(region)

        return word


def _find_in_open_folders(window, interactive=True, filter=False, include_vendor=False):
    view = window.active_view()
    word = view.sel()[0]
    if word.empty():
        word = view.word(word)

    view.sel().clear()
    view.sel().add(word)

    def _get_filter():
        include_filters = []

        include_filters.append('-storage/')
        include_filters.append('-tmp/')
        include_filters.append('-.phan/')
        include_filters.append('-.psalm/')
        include_filters.append('-Sandbox*')

        file_name = view.file_name()
        if file_name:
            include_filters.append('*' + os.path.splitext(file_name)[1])

        if include_vendor:
            include_filters.append('-vendor/')
        else:
            include_filters.append('-vendor/composer/')

        if include_filters:
            return ',' + ','.join(include_filters)
        else:
            return ''

    where = '<open folders>'
    if filter and isinstance(filter, bool):
        where += _get_filter()

    window.run_command('show_panel', {
        'panel': 'find_in_files',
        'where': where,
        'whole_word': False,
        'case_sensitive': False,
        'regex': False,
        'use_buffer': True,
        'show_context': True
    })

    view.sel().clear()
    view.sel().add(word)

    if not interactive:
        window.run_command('find_all', {
            'close_panel': True
        })
