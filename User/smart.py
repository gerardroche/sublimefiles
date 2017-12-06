import re

import sublime_plugin


class SmartInsertNewlineCommand(sublime_plugin.TextCommand):
    """
    Insert newline if the next line is not blank.

    Otherwise moves down to the blank line.
    """

    def run(self, edit):

        if len(self.view.sel()) == 0:
            return

        if len(self.view.sel()) != 1:
            # doesn't support multiple selections
            return

        cursor_point = self.view.sel()[0].begin()
        cursor_line_region = self.view.full_line(cursor_point)
        cursor_line_as_string = self.view.substr(cursor_line_region)
        cursor_line_has_eol_punctutation = re.search('(\\{|\\[)s*$', cursor_line_as_string)

        if cursor_line_has_eol_punctutation:

            next_line_region = self.view.full_line(cursor_line_region.end())
            next_line_as_string = self.view.substr(next_line_region)
            next_line_is_blank = re.match('^\\s*$', next_line_as_string)

            self.view.run_command('move_to', {'to': 'hardeol'})

            if next_line_is_blank:
                self.view.run_command('move', {'by': 'lines', 'forward': True})
            else:
                self.view.run_command('insert', {'characters': '\n'})

            self.view.run_command('move_to', {'to': 'hardeol', 'extend': False})
            self.view.run_command('reindent', {'single_line': True})
