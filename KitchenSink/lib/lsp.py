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

import functools
import os
import re

import sublime
import sublime_plugin


class LspSourceActions(sublime_plugin.WindowCommand):

    def run(self, action):
        self.window.run_command('lsp_code_actions', {
            'only_kinds': ['source']
        })


class LspSymbolDefinitionSplit(sublime_plugin.WindowCommand):

    def run(self):
        self.window.run_command('lsp_symbol_definition', {
            'side_by_side': True
        })

        sublime.set_timeout(self.fix_side_by_side_issue, 30)

    def fix_side_by_side_issue(self):
        self.window.run_command('carry_file_to_pane', {
            'direction': 'right'
        })
