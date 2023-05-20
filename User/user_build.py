import sublime
import sublime_plugin


class SublimeTextBuildEvents(sublime_plugin.EventListener):

    def on_activated_async(self, view):
        view.set_status('sublime_text_build', 'Build ' + sublime.version())
