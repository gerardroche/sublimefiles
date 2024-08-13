import os

import sublime_plugin


class FinderInFiles(sublime_plugin.WindowCommand):

    def run(self, **kwargs):
        _find_in_files(self.window, **kwargs)


class FinderUnderCursor(sublime_plugin.TextCommand):

    def run(self, edit):
        self.view.window().run_command('show_overlay', {
            'overlay': 'goto',
            'show_files': True,
            'text': self.getText(),
        })

    def getText(self) -> str:
        sel = self.view.sel()[0]
        point = sel.b - 1 if sel.b > sel.a else sel.a
        region = self.view.word(point)
        word = self.view.substr(region)

        return word


def _find_in_files(window, interactive: bool = True, where: str = None):
    view = window.active_view()

    # Populate FIND field.
    find_text = view.sel()[0]
    if find_text.empty():
        find_text = view.word(find_text)
    view.sel().clear()
    view.sel().add(find_text)

    # Build WHERE field.
    if where == 'default':
        where = ['<open folders>'] + _get_user_where()
    elif where == 'project':
        where = [_find_project_folder(view, '<open folders>')] + _get_user_where()
    elif where is None:
        where = []

    window.run_command('show_panel', {
        'panel': 'find_in_files',
        'use_gitignore': False,
        'where': ','.join(where),
        'whole_word': False,
        'case_sensitive': False,
        'regex': False,
        'use_buffer': True,
        'show_context': True
    })

    if not interactive:
        window.run_command('find_all', {'close_panel': True})


def _find_project_folder(view, default=None):
    for folder in view.window().folders():
        file_name = view.file_name()
        if file_name and file_name.startswith(folder):
            return folder

    return default


def _get_user_where() -> str:
    return [
        '-//.p*/',
        '-Sandbox*',
        '-build/',
        '-mode_modules/',
        '-storage/',
        '-tmp/',
        '-tools/',
        '-vendor/'
    ]
