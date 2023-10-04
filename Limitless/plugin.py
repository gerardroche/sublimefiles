# Copyright (C) 2023 Gerard Roche
#
# This file is part of Limitless.
#
# Limitless is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Limitless is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Limitless.  If not, see <https://www.gnu.org/licenses/>.

import sublime_plugin

from User import sublime_ext


class LimitlessClear(sublime_plugin.WindowCommand):

    def run(self):
        if self.window.is_sidebar_visible():
            self.window.set_sidebar_visible(False)

        if self.window.is_minimap_visible():
            self.window.set_minimap_visible(False)

        if self.window.is_menu_visible():
            self.window.set_menu_visible(False)

        _resize_groups_equally(self.window)

        with sublime_ext.save_preferences() as preferences:
            _set_clear_preference(preferences, 'draw_white_space')
            _set_clear_preference(preferences, 'indent_guide_options', [])
            _set_clear_preference(preferences, 'line_numbers', False)
            _set_clear_preference(preferences, 'rulers', [])

        self.window.run_command('sort_user_settings')


class LimitlessFocus(sublime_plugin.WindowCommand):

    def run(self):
        with sublime_ext.save_preferences() as preferences:
            files = preferences.get('file_exclude_patterns_focus')
            _update_patterns(preferences, 'file_exclude_patterns', files)
            folders = preferences.get('folder_exclude_patterns_focus')
            _update_patterns(preferences, 'folder_exclude_patterns', folders)


class LimitlessReset(sublime_plugin.WindowCommand):

    def run(self):
        print('reset')
        with sublime_ext.save_preferences() as preferences:
            _set_default_preference(preferences, 'draw_white_space')
            _set_default_preference(preferences, 'indent_guide_options', [
                "draw_normal",
                "solid",
                "draw_active",
            ])
            _set_clear_preference(preferences, 'line_numbers', True)

        if not self.window.is_sidebar_visible():
            self.window.set_sidebar_visible(True)

        if not self.window.is_minimap_visible():
            self.window.set_minimap_visible(True)

        if not self.window.is_menu_visible():
            self.window.set_menu_visible(True)

        if not self.window.is_status_bar_visible():
            self.window.set_status_bar_visible(True)

        _resize_groups_equally(self.window)


def _resize_groups_equally(window) -> None:
    layout = window.layout()
    col_count = len(layout['cols'])
    row_count = len(layout['rows'])

    if col_count > 2:
        layout['cols'] = _equalise_count(col_count)

    if row_count > 2:
        layout['rows'] = _equalise_count(row_count)

    if col_count > 2 or row_count > 2:
        window.set_layout(layout)


def _equalise_count(count: int) -> list:
    size = round(1.0 / (count - 1), 2)
    vals = [0.0]
    for i in range(1, count - 1):
        vals.append(round(size * i, 2))
    vals.append(1.0)
    return vals


def _set_preference(preferences, name, suffix, default=None):
    value = preferences.get(name + '_' + suffix, default)
    if value is not None:
        preferences.set(name, value)


def _set_clear_preference(preferences, name, default=None):
    _set_preference(preferences, name, 'clear', default)


def _set_default_preference(preferences, name, default=None):
    _set_preference(preferences, name, 'default', default)


def _update_patterns(preferences, name: str, items: list) -> None:
    exclude_patterns = preferences.get(name)
    if not isinstance(exclude_patterns, list):
        return

    for item in items:
        if item in exclude_patterns:
            exclude_patterns.remove(item)
        else:
            exclude_patterns.append(item)

        exclude_patterns = list(set(exclude_patterns))
        exclude_patterns.sort()

        if exclude_patterns:
            preferences.set(name, exclude_patterns)
