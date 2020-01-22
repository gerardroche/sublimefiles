from contextlib import contextmanager

from sublime import load_settings
from sublime import save_settings
import sublime_plugin


@contextmanager
def save_preferences():
    yield load_settings('Preferences.sublime-settings')
    save_settings('Preferences.sublime-settings')


class ClearWindowCommand(sublime_plugin.WindowCommand):

    def run(self):
        if self.window.is_sidebar_visible():
            self.window.set_sidebar_visible(False)

        if self.window.is_minimap_visible():
            self.window.set_minimap_visible(False)

        if self.window.is_menu_visible():
            self.window.set_menu_visible(False)

        if self.window.is_status_bar_visible():
            self.window.set_status_bar_visible(False)

        _resize_groups_almost_equally(self.window)

        with save_preferences() as preferences:
            preferences.set('indent_guide_options', [])
            preferences.set('line_numbers', False)
            preferences.set('draw_white_space', 'selection')
            preferences.set('rulers', [])

        self.window.run_command('sort_user_settings')


class ResetWindowCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.run_command('reset_font_size')

        view = self.window.active_view()

        font_size = view.settings().get('font_size_default') if view else None
        if font_size:
            with save_preferences() as preferences:
                preferences.set('font_size', font_size)

        if not self.window.is_sidebar_visible():
            self.window.set_sidebar_visible(True)

        if not self.window.is_minimap_visible():
            self.window.set_minimap_visible(True)

        if not self.window.is_menu_visible():
            self.window.set_menu_visible(True)

        if not self.window.is_status_bar_visible():
            self.window.set_status_bar_visible(True)

        _resize_groups_almost_equally(self.window)


def _resize_groups_almost_equally(window):
    layout = window.layout()
    col_count = len(layout['cols'])
    row_count = len(layout['rows'])

    def equalise(count):
        size = round(1.0 / (count - 1), 2)
        vals = [0.0]
        for i in range(1, count - 1):
            vals.append(round(size * i, 2))
        vals.append(1.0)
        return vals

    if col_count > 2:
        layout['cols'] = equalise(col_count)

    if row_count > 2:
        layout['rows'] = equalise(row_count)

    if col_count > 2 or row_count > 2:
        window.set_layout(layout)
