import os

import sublime
import sublime_plugin


class UserStatusEventListener(sublime_plugin.EventListener):

    def on_activated_async(self, view):
        if view.settings().get('show_build'):
            _show_build(view)

        if view.settings().get('show_file'):
            _show_file(view)

    def on_selection_modified_async(self, view):
        if view.settings().get('show_point'):
            _show_point(view)

        if view.settings().get('show_spell'):
            _show_spell(view)


def _show_build(view) -> None:
    view.set_status('build', 'Build ' + sublime.version())


def _show_file(view) -> None:
    file_name = view.file_name()
    if file_name:
        if 'HOME' in os.environ and file_name.startswith(os.environ['HOME']):
            file_name = file_name.replace(os.environ['HOME'], '~')

        view.set_status('file', file_name)


def _show_point(view) -> None:
    view.set_status('point', 'Point ' + ','.join([str(s.b) for s in view.sel()]))


def _show_spell(view):
    if view.settings().get('spell_check'):
        dictionary = view.settings().get('dictionary')
        dictionary = dictionary.replace('Packages/Language - ', '').replace('.dic', '')
        view.set_status('spell', 'SPELL [%s]' % dictionary)
    else:
        view.erase_status('spell')
