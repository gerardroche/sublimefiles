from contextlib import contextmanager

from sublime import load_settings
from sublime import save_settings
import sublime_plugin


@contextmanager
def save_preferences():
    yield load_settings('Preferences.sublime-settings')
    save_settings('Preferences.sublime-settings')


def set_default_preference(preferences, name, default=None):
    set_preference(preferences, name, 'default', default)


def clear_preference(preferences, name, default=None):
    set_preference(preferences, name, 'clear', default)


def set_preference(preferences, name, suffix, default=None):
    value = preferences.get(name + '_' + suffix, default)
    if value is not None:
        preferences.set(name, value)


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
            clear_preference(preferences, 'draw_white_space')
            clear_preference(preferences, 'indent_guide_options', [])
            clear_preference(preferences, 'line_numbers', False)
            clear_preference(preferences, 'rulers', [])

        self.window.run_command('sort_user_settings')


class ResetWindowCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.run_command('reset_font_size')

        with save_preferences() as preferences:
            set_default_preference(preferences, 'draw_white_space')
            set_default_preference(preferences, 'indent_guide_options', [
                "draw_normal",
                "solid",
                "draw_active",
            ])
            clear_preference(preferences, 'line_numbers', True)
            set_default_preference(preferences, 'font_size')

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
