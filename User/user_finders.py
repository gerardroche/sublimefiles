import os

import sublime_plugin


def _find_in_open_folders(window, interactive=True, filter=False, include_vendor=False):
    view = window.active_view()
    region = view.sel()[0]
    word = view.word(region)
    view.sel().clear()
    view.sel().add(word)

    def _get_filter():
        include_filters = []

        include_filters.append('-storage/')
        include_filters.append('-tmp/')
        include_filters.append('-.phan/')
        include_filters.append('-phan/stubs')

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

    if filter:
        if isinstance(filter, bool):
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
    view.sel().add(region)

    if not interactive:
        window.run_command('find_all', {
            'close_panel': True
        })


class FindInOpenFoldersCommand(sublime_plugin.WindowCommand):

    def run(self, **kwargs):
        _find_in_open_folders(self.window, **kwargs)


class FocusUnitTestingPanelCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.run_command('show_panel', {'panel': 'output.UnitTesting'})
        self.window.focus_view(self.window.find_output_panel('UnitTesting'))


class ShowFindResultsCommand(sublime_plugin.WindowCommand):

    def run(self):
        for view in self.window.views():
            if view.name() == 'Find Results':
                # Clear any visual selection.
                sel = view.sel()[0].begin()
                view.sel().clear()
                view.sel().add(sel)

                return self.window.focus_view(view)
