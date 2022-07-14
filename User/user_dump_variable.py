import re

import sublime_plugin


class DumpVariableCommand(sublime_plugin.TextCommand):

    def run(self, edit, **kwargs):
        line, pt, scope = self.get_variables()

        if 'php' in scope:
            pt += 1

        word = self.get_word_under_caret(pt)

        if 'php' in scope:
            dump_str = self.get_php_dump(word, **kwargs)
        elif 'python' in scope:
            dump_str = self.get_python_dump(word, **kwargs)

        if dump_str:
            self.view.insert(edit, line.end(), '\n' + dump_str)
            self.view.run_command('move', {'by': 'lines', 'forward': True})
            self.view.run_command('reindent', {'single_line': True})
            self.view.run_command('save')

    def get_php_dump(self, word, **kwargs):
        dump_func = kwargs.get('phpfunc', 'var_dump')
        dump_content = kwargs.get('content', '$' + str(word))

        return dump_func + '(' + dump_content + ');'

    def get_python_dump(self, word, **kwargs):
        if kwargs.get('sublime_region_view_string') or kwargs.get('sublime_region_self_view_string'):
            obj = 'view' if kwargs.get('sublime_region_view_string') else 'self.view'
            dump_stmt = 'print(\'' + word + ' =\', ' + word + ', \'>>>\' + ' + obj + '.substr(' + word + ').replace(\'\\n\', \'\\\\n\').replace(\'\\x00\', \'EOF\') + \'<<<\')  # noqa: E501'  # noqa
        elif kwargs.get('sublime_region_view_regions'):
            dump_stmt = 'print(\'{0}\', len({0}), \'->\', \'\'.join([str(s) + \' >>>\' + view.substr(s).replace(\'\\n\', \'\\\\n\').replace(\'\\x00\', \'EOF\') + \'<<< \' for s in list({0})]))  # noqa: E501'.format(word)
        else:
            if kwargs.get('type'):
                dump_stmt = 'print(\'{0} =\', {0}, type({0}))'.format(word)
            else:
                dump_stmt = 'print(\'{0} =\', {0})'.format(word)

        return dump_stmt

    def get_word_under_caret(self, pt: int):
        word_region = self.view.word(pt)
        word = self.view.substr(word_region)
        if re.match('^[a-zA-Z_][a-zA-Z0-9_]*$', word):
            return word

    def get_variables(self) -> tuple:
        pt = self.view.sel()[0].b
        line = self.view.line(pt)
        if line.empty():
            row, col = self.view.rowcol(pt)
            prev_row = max(row - 1, 0)
            if prev_row != row:
                pt = self.view.text_point(prev_row, 0)

        if self.view.substr(pt) == ' ':
            f = self.view.find('\\s*', pt)
            pt = f.end()

        scope = self.view.scope_name(pt)

        return line, pt, scope
