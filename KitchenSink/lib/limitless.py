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

from KitchenSink.lib.utils import save_preferences


class LimitlessClear(sublime_plugin.WindowCommand):

    def run(self):
        _clear(self.window)


class LimitlessReset(sublime_plugin.WindowCommand):

    def run(self):
        _reset(self.window)


class LimitlessFocus(sublime_plugin.WindowCommand):

    def run(self):
        _focus(self.window)


def _set_preference(settings, name: str, suffix: str, default=None) -> None:
    value = settings.get("{}_{}".format(name, suffix), default)
    if value is not None:
        settings.set(name, value)


def _set_preference_on_clear(settings, name: str, default=None) -> None:
    _set_preference(settings, name, 'on_clear', default)


def _set_preference_on_reset(settings, name: str, default=None) -> None:
    _set_preference(settings, name, 'on_reset', default)


def _set_patterns_on_focus(settings, name: str) -> None:
    patterns = settings.get(name)
    if not isinstance(patterns, list):
        return

    on_focus_patterns = settings.get("{}_{}".format(name, 'on_focus'), [])
    if not isinstance(on_focus_patterns, list) or not on_focus_patterns:
        return

    should_remove_patterns = all(p in patterns for p in on_focus_patterns)
    for pattern in on_focus_patterns:
        if should_remove_patterns:
            patterns.remove(pattern)
        else:
            patterns.append(pattern)

    patterns = list(set(patterns))
    patterns.sort()
    if patterns:
        settings.set(name, patterns)


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


def _clear(window) -> None:
    with save_preferences() as preferences:
        _set_preference_on_clear(preferences, 'draw_indent_guides', False)
        _set_preference_on_clear(preferences, 'draw_white_space', ['selection'])
        _set_preference_on_clear(preferences, 'line_numbers', False)
        _set_preference_on_clear(preferences, 'rulers', [])

    if window.is_minimap_visible():
        window.set_minimap_visible(False)

    if window.is_menu_visible():
        window.set_menu_visible(False)

    _resize_groups_equally(window)
    window.run_command('sort_user_settings')


def _reset(window) -> None:
    with save_preferences() as preferences:
        _set_preference_on_clear(preferences, 'line_numbers', True)
        _set_preference_on_clear(preferences, 'rulers', [[80, "stippled"], [120, "solid"]])
        _set_preference_on_reset(preferences, 'draw_indent_guides', True)
        _set_preference_on_reset(preferences, 'draw_white_space')

    if not window.is_sidebar_visible():
        window.set_sidebar_visible(True)

    if not window.is_minimap_visible():
        window.set_minimap_visible(True)

    if not window.is_menu_visible():
        window.set_menu_visible(True)

    if not window.is_status_bar_visible():
        window.set_status_bar_visible(True)

    _resize_groups_equally(window)
    window.run_command('sort_user_settings')


def _focus(window) -> None:
    _clear(window)

    with save_preferences() as preferences:
        _set_patterns_on_focus(preferences, 'file_exclude_patterns')
        _set_patterns_on_focus(preferences, 'folder_exclude_patterns')
