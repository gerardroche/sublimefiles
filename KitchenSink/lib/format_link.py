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

import re

import sublime_plugin


class KitchenSinkFormatLink(sublime_plugin.TextCommand):

    def run(self, edit):
        line = self.view.line(self.view.sel()[0].b)
        line_string = self.view.substr(line)
        link = _format_link(line_string)
        if link:
            self.view.replace(edit, line, link)


def _format_link(line_string: str):
    match = re.match('^([^`]+)(.*)', line_string)
    if match:
        label = match.group(1)
        anchor = match.group(1) + match.group(2)

        ws_count = 0
        ws = re.match('\\s*[#]+', label)
        if ws:
            ws_count = len(ws.group(0))
            if ws_count == 3:
                ws_count = 2
            elif ws_count == 4:
                ws_count = 4

        label = label.strip()
        label = re.sub('^[^a-zA-Z0-9\\.]*', '', label)
        label = label.strip()

        anchor = anchor.lower()
        anchor = anchor.replace('.', '')
        anchor = re.sub('[^a-z0-9-]', '-', anchor)
        anchor = re.sub('--+', '-', anchor)
        anchor = anchor.strip('-')

        link = '[%s](#%s)' % (label, anchor)
        link = (' ' * (ws_count - 1)) + ' - ' + link

        return link
