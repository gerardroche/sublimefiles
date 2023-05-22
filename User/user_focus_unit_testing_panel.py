import sublime_plugin


class UserFocusUnitTestingPanel(sublime_plugin.WindowCommand):

    def run(self):
        self.window.run_command('show_panel', {'panel': 'output.UnitTesting'})
        self.window.focus_view(self.window.find_output_panel('UnitTesting'))
