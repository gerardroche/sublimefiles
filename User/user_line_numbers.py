# Relative line numbers is only supported in builds versions >= 4074.

import sublime_plugin


def is_normal_view(view) -> bool:
    return view and view.element() is None


def is_command_mode(view) -> bool:
    return is_normal_view(view) and view.settings().get('command_mode')


class LineNumbersEvents(sublime_plugin.EventListener):

    def on_post_text_command(self, view, command_name, args):
        settings = view.settings()
        if settings.get('line_numbers'):
            if is_command_mode(view):
                settings.set('relative_line_numbers', True)
            else:
                settings.set('relative_line_numbers', False)
