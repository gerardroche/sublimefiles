from sublime import version
import sublime_plugin


if int(version()) >= 4050:
    def is_normal_view(view) -> bool:
        return view and view.element() is None
else:
    def is_normal_view(view) -> bool:
        if not view:
            return False

        settings = view.settings()

        return settings and not settings.get('is_widget', False)


class LineHighlightEvents(sublime_plugin.EventListener):

    def on_deactivated(self, view):
        if is_normal_view(view):
            view.settings().set('highlight_line', False)

    def on_activated(self, view):
        if is_normal_view(view):
            view.settings().set('highlight_line', True)

    def on_post_text_command(self, view, command_name, args):
        if is_normal_view(view):
            settings = view.settings()
            highlight_line = settings.get('highlight_line')
            if settings.get('command_mode'):
                if highlight_line is False:
                    settings.set('highlight_line', True)
            else:
                if highlight_line is True:
                    settings.set('highlight_line', False)
