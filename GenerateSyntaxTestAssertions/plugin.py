# Copyright (C) 2023 Gerard Roche
#
# This file is part of GenerateSyntaxTestAssertions.
#
# GenerateSyntaxTestAssertions is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GenerateSyntaxTestAssertions is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GenerateSyntaxTestAssertions.  If not, see <https://www.gnu.org/licenses/>.
import sublime_plugin


class GenerateSyntaxTestAssertions(sublime_plugin.TextCommand):

    def run(self, edit):
        point = self.view.sel()[0].begin()
        line = self.view.line(point)
        assertions = _generate_syntax_assertions(self.view, point)
        self.view.insert(edit, line.end(), '\n' + assertions)


def _generate_syntax_assertions(view, pt):
    line = view.line(pt)

    scopes = []
    for i in range(line.begin(), line.end()):
        scopes.append(view.scope_name(i).rstrip(' '))

    return _generate_assertions(scopes, view, pt)


def _generate_assertions(items, view, pt):
    comment_start, comment_end = _get_comment_markers(view, pt)

    return _build_assertions(items, comment_start, comment_end)


def _build_assertions(styles, comment_start, comment_end):
    line_styles_count = len(styles)
    repeat_count = 0
    indent_count = 0
    prev_style = None
    assertions = []
    for i, style in enumerate(styles):
        if style == prev_style:
            repeat_count += 1
        else:
            if prev_style is not None:
                assertions.append((indent_count * ' ') + ('^' * repeat_count) + ' ' + prev_style)
                indent_count += repeat_count
                repeat_count = 1
            else:
                repeat_count += 1

        prev_style = style

        if line_styles_count == i + 1:
            assertions.append((indent_count * ' ') + ('^' * repeat_count) + ' ' + prev_style)

    assertions_str = ''
    for assertion in assertions:
        assertion = assertion[len(comment_start):]
        if assertion.lstrip(' ').startswith('^') and assertion.strip(' ^') != '':
            assertions_str += comment_start + assertion + comment_end + '\n'

    return assertions_str.rstrip('\n')


def _get_comment_markers(view, pt):
    comment_start = ''
    comment_end = ''
    for v in view.meta_info('shellVariables', pt):
        if v['name'] == 'TM_COMMENT_START':
            comment_start = v['value']
            if not comment_start.endswith(' '):
                comment_start = comment_start + ' '

        if v['name'] == 'TM_COMMENT_END':
            comment_end = v['value']
            if not comment_end.startswith(' '):
                comment_end = ' ' + comment_end

    return (comment_start, comment_end)
