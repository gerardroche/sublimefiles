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


def _set_highlight(view, flag: bool) -> None:
    view.settings().set('highlight_line', flag)
    view.settings().set('highlight_gutter', flag)


class LineHighlightEvents(sublime_plugin.EventListener):

    def on_deactivated(self, view):
        if is_normal_view(view):
            _set_highlight(view, False)

    def on_activated(self, view):
        if is_normal_view(view):
            _set_highlight(view, True)

    def on_post_text_command(self, view, command_name, args):
        if is_normal_view(view):
            highlight_line = view.settings().get('highlight_line')
            if view.settings().get('command_mode'):
                if highlight_line is False:
                    _set_highlight(view, True)
            elif highlight_line is True:
                _set_highlight(view, False)
