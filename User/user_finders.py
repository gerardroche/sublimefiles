import os

import sublime_plugin


class UserFindInFilesCommand(sublime_plugin.WindowCommand):

    def run(self, **kwargs):
        _find_in_files(self.window, **kwargs)


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


def _find_in_files(window, interactive: bool = True, use_filter: bool = True):
    view = window.active_view()

    # Set word under cursor.
    word = view.sel()[0]
    if word.empty():
        word = view.word(word)
    view.sel().clear()
    view.sel().add(word)

    # Build where field.
    where = '<open folders>'
    if use_filter and isinstance(use_filter, bool):
        where += _get_where(view)

    window.run_command('show_panel', {
        'panel': 'find_in_files',
        'use_gitignore': use_filter,
        'where': where,
        'whole_word': False,
        'case_sensitive': False,
        'regex': False,
        'use_buffer': True,
        'show_context': True
    })

    if not interactive:
        window.run_command('find_all', {
            'close_panel': True
        })


def _get_where(view, vendor: bool = True) -> str:
    where = []

    where.append('-.phan/')
    where.append('-.psalm/')
    where.append('-Sandbox*')
    where.append('-storage/')
    where.append('-tmp/')
    where.append('-vendor/composer/')

    if not vendor:
        where.append('-vendor/')

    file_name = view.file_name()
    if file_name:
        where.append('*' + os.path.splitext(file_name)[1])

    if where:
        return ',' + ','.join(where)

    return ''
