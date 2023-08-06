import re

import sublime_plugin


class UserFormatLink(sublime_plugin.TextCommand):

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
        print('ws =', ws)
        if ws:
            print(len(ws.group(0)))
            ws_count = len(ws.group(0)) - 2

        label = label.strip()
        label = re.sub('^[^a-zA-Z0-9\\.]*', '', label)
        label = label.strip()

        anchor = anchor.lower()
        anchor = anchor.replace('.', '')
        anchor = re.sub('[^a-z0-9-]', '-', anchor)
        anchor = re.sub('--+', '-', anchor)
        anchor = anchor.strip('-')

        link = '[%s](#%s)' % (label, anchor)
        link = (' ' * ws_count) + ' - ' + link

        return link
