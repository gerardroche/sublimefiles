import os

import sublime
import sublime_plugin


class KitchenSinkStatusEventListener(sublime_plugin.EventListener):

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

        if view.settings().get('show_x_preview'):
            _show_x_preview(view)

        if view.settings().get('show_word_count'):
            _show_word_count(view)


class ToggleShowXpreview(sublime_plugin.WindowCommand):

    def run(self):
        settings = self.window.active_view().settings()
        flag = settings.get('show_x_preview')
        settings.set('show_x_preview', not flag)


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


def _show_spell(view) -> None:
    if view.settings().get('spell_check'):
        dictionary = view.settings().get('dictionary')
        dictionary = dictionary.replace('Packages/Language - ', '').replace('.dic', '')
        view.set_status('spell', 'SPELL [%s]' % dictionary)
    else:
        view.erase_status('spell')


def _show_x_preview(view) -> None:
    view.add_regions(
        'x_preview',
        [sublime.Region(280, view.size())],
        scope='string',
        flags=sublime.DRAW_NO_FILL)


def _show_word_count(view) -> None:
    word_count = len(view.find_all('\\w+'))
    paragraph_count = len(view.find_all('\n\n+')) + 1
    view.set_status('word_count', '%d words, %d paragraphs' % (word_count, paragraph_count))
