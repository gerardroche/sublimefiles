import sublime
import sublime_plugin


class LspSymbolDefinitionSplit(sublime_plugin.WindowCommand):

    def run(self):
        self.window.run_command('lsp_symbol_definition', {
            'side_by_side': True
        })

        # Why is the cork on the fork?
        # side-by-side crap.
        sublime.set_timeout(self.fart, 30)

    def fart(self):
        self.window.run_command('carry_file_to_pane', {
            'direction': 'right'
        })
