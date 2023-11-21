import os

import sublime_plugin


class FindFileUnderCursorCommand(sublime_plugin.TextCommand):

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


class UserFindInFilesCommand(sublime_plugin.WindowCommand):

    def run(self, **kwargs):
        _find_in_files(self.window, **kwargs)


def _find_in_files(window, interactive: bool = True, where: str = None):
    view = window.active_view()

    # Add word under cursor to the Find field.
    find_text = view.sel()[0]
    if find_text.empty():
        find_text = view.word(find_text)
    view.sel().clear()
    view.sel().add(find_text)

    # Build where field.

    if where == 'default':
        where = '<open folders>'
        where += _get_project_filters(view)
    elif where == 'project':
        where = find_project_folder(view)
        if not where:
            where = '<open folders>'

        where += _get_project_filters(view)
    elif where is None:
        where = ''

    use_gitignore = False

    window.run_command('show_panel', {
        'panel': 'find_in_files',
        'use_gitignore': use_gitignore,
        'where': where,
        'whole_word': False,
        'case_sensitive': False,
        'regex': False,
        'use_buffer': True,
        'show_context': True
    })

    if not interactive:
        window.run_command('find_all', {'close_panel': True})


def find_project_folder(view):
    for folder in view.window().folders():
        if view.file_name().startswith(folder):
            return folder


def _get_project_filters(view) -> str:
    filters = []

    filters.append('-//.p*/')
    filters.append('-Sandbox*')
    filters.append('-build/')
    filters.append('-mode_modules/')
    filters.append('-storage/')
    filters.append('-tmp/')
    filters.append('-tools/')
    filters.append('-vendor/')

    # file_name = view.file_name()
    # if file_name:
    #     filters.append('*' + os.path.splitext(file_name)[1])

    if filters:
        return ',' + ','.join(filters)

    return ''
