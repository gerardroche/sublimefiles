# When you see something you like and would like to use it, open an issue about
# abstracting it out into a reusable package, possibly installable via Package
# Control.

import os

import sublime_plugin


def _find_in_open_folders(window, interactive=True, default_filter=False):
    view = window.active_view()
    region = view.sel()[0]
    word = view.word(region)
    view.sel().clear()
    view.sel().add(word)

    def get_default_filter():
        include_filters = []

        include_filters.append('-tmp/')
        include_filters.append('-.srcpath/')
        include_filters.append('-storage/framework/views')

        file_name = view.file_name()
        if file_name:
            include_filters.append('*' + os.path.splitext(file_name)[1])

        if include_filters:
            return ',' + ','.join(include_filters)
        else:
            return ''

    window.run_command('show_panel', {
        'panel': 'find_in_files',
        'where': '<open folders>' + get_default_filter() if default_filter else '',
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
    def run(self, interactive=True, default_filter=False):
        _find_in_open_folders(self.window, interactive, default_filter)


class FocusUnitTestingPanelCommand(sublime_plugin.WindowCommand):
    def run(self):
        name = 'output.UnitTesting'
        self.window.run_command('show_panel', {'panel': name})

        name = 'UnitTesting'
        self.window.focus_view(self.window.find_output_panel(name))


class ShowFindResultsCommand(sublime_plugin.WindowCommand):
    def run(self):
        for view in self.window.views():
            if view.name() == 'Find Results':
                # Clear any visual selection.
                sel = view.sel()[0].begin()
                view.sel().clear()
                view.sel().add(sel)

                return self.window.focus_view(view)
