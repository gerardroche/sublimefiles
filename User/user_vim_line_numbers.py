# Relative line numbers is only supported in builds versions >= 4074.
import sublime
import sublime_plugin


if int(sublime.version()) >= 4050:
    def is_normal_view(view) -> bool:
        return view and view.element() is None
else:
    def is_normal_view(view) -> bool:
        if not view:
            return False

        settings = view.settings()

        return settings and not settings.get('is_widget', False)


def is_command_mode(view) -> bool:
    return is_normal_view(view) and view.settings().get('command_mode')


class LineNumbersEvents(sublime_plugin.EventListener):

    def on_post_text_command(self, view, command_name, args):
        if view.settings().get('line_numbers'):
            if is_command_mode(view):
                view.settings().set('relative_line_numbers', True)
            else:
                view.settings().set('relative_line_numbers', False)
