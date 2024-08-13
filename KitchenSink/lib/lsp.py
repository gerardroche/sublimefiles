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
