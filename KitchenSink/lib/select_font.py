# Copyright (C) 2024 Gerard Roche
#
# This file is part of KitchenSink.
#
# KitchenSink is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# KitchenSink is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with KitchenSink.  If not, see <https://www.gnu.org/licenses/>.


import sublime
import sublime_plugin


class SelectFont(sublime_plugin.WindowCommand):

    def input_description(self):
        return "Font:"

    def input(self, args):
        return FontFaceInputHandler()

    def run(self, font_face):
        settings = sublime.load_settings('Preferences.sublime-settings')
        settings.set('font_face', font_face)
        sublime.save_settings('Preferences.sublime-settings')


class FontFaceInputHandler(sublime_plugin.ListInputHandler):

    def __init__(self):
        super().__init__()
        self.prefs = sublime.load_settings('Preferences.sublime-settings')
        self.original = self.prefs.get("font_face", "")

    def placeholder(self):
        return "Select Font"

    def cancel(self):
        self.prefs.set('font_face', self.original)
        sublime.save_settings('Preferences.sublime-settings')

    def confirm(self, font_face):
        sublime.save_settings('Preferences.sublime-settings')

    def preview(self, font_face):
        if font_face is None:
            return

        self.last_previewed = font_face

        def update():
            # The color scheme to preview has been updated since
            # the timeout was created
            if font_face != self.last_previewed:
                return
            if self.prefs.get('font_face') == font_face:
                return
            self.prefs.set('font_face', font_face)

        sublime.set_timeout(update, 250)

    def list_items(self):
        font_faces = self.prefs.get('font_faces')
        font_faces = set(font_faces) if isinstance(font_faces, list) else set()
        font_faces.add(self.prefs.get("font_face"))

        items = []
        selected = -1
        for font in sorted(font_faces):
            kind_info = sublime.KIND_AMBIGUOUS
            if self.original and self.original == font:
                kind_info = (sublime.KIND_ID_COLOR_GREENISH, "✓", "Current")
                selected = len(items)

            items.append(sublime.ListInputItem(font, font, kind=kind_info))

        return (items, selected)
