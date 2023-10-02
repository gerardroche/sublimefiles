import os

import sublime
import sublime_plugin


class UserEvents(sublime_plugin.EventListener):

    def on_activated_async(self, view):
        if view.settings().get('show_build'):
            view.set_status('sublime_text_build', 'Build ' + sublime.version())

        if view.settings().get('show_file_name'):
            file_name = _get_file_name(view)
            if file_name:
                view.set_status('file_name', file_name)

    def on_selection_modified_async(self, view):
        if view.settings().get('show_point'):
            view.set_status('point', 'Point ' + ','.join([str(s.b) for s in view.sel()]))

        if view.settings().get('show_spell'):
            _handle_show_spell(view)


def _get_file_name(view):
    file_name = view.file_name()
    if file_name:
        if 'HOME' in os.environ:
            home = os.environ['HOME']
            if file_name.startswith(home):
                file_name = file_name.replace(home, '~')

        return file_name


def _handle_show_spell(view):
    if view.settings().get('spell_check'):
        dictionary = view.settings().get('dictionary')
        dictionary = dictionary.replace('Packages/Language - ', '').replace('.dic', '')
        view.set_status('spell', 'SPELL [%s]' % dictionary)
    else:
        view.erase_status('spell')
