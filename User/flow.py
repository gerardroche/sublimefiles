import sublime
import sublime_plugin


class FlowCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.run_command('toggle_distraction_free')

        if self.window.is_sidebar_visible():
            self.window.set_sidebar_visible(False)

        self.window.run_command('resize_groups_almost_equally')


class ClearWindowCommand(sublime_plugin.WindowCommand):

    def run(self):

        if self.window.is_sidebar_visible():
            self.window.set_sidebar_visible(False)

        if self.window.is_minimap_visible():
            self.window.set_minimap_visible(False)

        if self.window.is_menu_visible():
            self.window.set_menu_visible(False)

        if self.window.is_status_bar_visible():
            self.window.set_status_bar_visible(False)

        self.window.run_command('resize_groups_almost_equally')

        settings = sublime.load_settings('Preferences.sublime-settings')
        settings.set('indent_guide_options', [])
        settings.set('line_numbers', False)
        settings.set('draw_white_space', 'selection')
        settings.set('rulers', [])
        sublime.save_settings('Preferences.sublime-settings')

        self.window.run_command('sort_user_settings')


class ResetWindowCommand(sublime_plugin.WindowCommand):

    def run(self):

        if not self.window.is_sidebar_visible():
            self.window.set_sidebar_visible(True)

        if not self.window.is_minimap_visible():
            self.window.set_minimap_visible(True)

        if not self.window.is_menu_visible():
            self.window.set_menu_visible(True)

        if not self.window.is_status_bar_visible():
            self.window.set_status_bar_visible(True)

        self.window.run_command('resize_groups_almost_equally')
