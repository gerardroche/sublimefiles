import sublime
import sublime_plugin


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
