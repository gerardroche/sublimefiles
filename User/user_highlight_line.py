import sublime_plugin


def is_normal(view) -> bool:
    return view and getattr(view, 'element', None) and view.element() is None


class LineHighlightEvents(sublime_plugin.EventListener):

    def on_deactivated(self, view):
        if is_normal(view):
            view.settings().set('highlight_line', False)

    def on_activated(self, view):
        if is_normal(view):
            view.settings().set('highlight_line', True)

    def on_selection_modified(self, view):
        if is_normal(view):
            settings = view.settings()
            highlight_line = settings.get('highlight_line')
            if settings.get('command_mode'):
                if highlight_line is False:
                    settings.set('highlight_line', True)
            else:
                if highlight_line is True:
                    settings.set('highlight_line', False)
