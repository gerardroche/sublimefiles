import sublime
import sublime_plugin


class UserShowBuild(sublime_plugin.EventListener):

    def on_activated_async(self, view):
        if view.settings().get('show_build'):
            view.set_status('sublime_text_build', 'Build ' + sublime.version())
