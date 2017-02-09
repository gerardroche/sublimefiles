import sublime
import sublime_plugin


class FlowCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.run_command('toggle_distraction_free')

        if self.window.is_sidebar_visible():
            self.window.set_sidebar_visible(False)

        self.window.run_command('resize_groups_almost_equally')
