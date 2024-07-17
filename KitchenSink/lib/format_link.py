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
