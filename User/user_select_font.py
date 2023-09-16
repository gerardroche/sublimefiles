import sublime
import sublime_plugin


class UserSelectFont(sublime_plugin.WindowCommand):

    def run(self):
        fonts = self.window.active_view().settings().get('fonts')
        self.window.show_quick_panel(fonts, self.on_done)

    def on_done(self, index: int) -> None:
        if index >= 0:
            fonts = self.window.active_view().settings().get('fonts')
            settings = sublime.load_settings('Preferences.sublime-settings')
            settings.set('font_face', fonts[index])
            sublime.save_settings('Preferences.sublime-settings')
