import os

import sublime
import sublime_plugin


class UserEventListener(sublime_plugin.EventListener):

    def on_activated_async(self, view):
        _show_on_activated_async(view)

    def on_selection_modified_async(self, view):
        _show_on_selection_modified_async(view)


def _show_on_activated_async(view):
    if view.settings().get('show_build'):
        view.set_status('sublime_text_build', 'Build ' + sublime.version())

    if view.settings().get('show_file_name'):
        file_name = _get_file_name(view)
        if file_name:
            view.set_status('file_name', file_name)


def _show_on_selection_modified_async(view):
    if view.settings().get('show_point'):
        view.set_status('point', 'Point ' + ','.join([str(s.b) for s in view.sel()]))

    if view.settings().get('show_spell'):
        if view.settings().get('spell_check'):
            dictionary = view.settings().get('dictionary')
            dictionary = dictionary.replace('Packages/Language - ', '').replace('.dic', '')
            view.set_status('spell', 'SPELL [%s]' % dictionary)
        else:
            view.erase_status('spell')


def _get_file_name(view):
    file_name = view.file_name()
    if file_name:
        if 'HOME' in os.environ:
            home = os.environ['HOME']
            if file_name.startswith(home):
                file_name = file_name.replace(home, '~')

        return file_name
