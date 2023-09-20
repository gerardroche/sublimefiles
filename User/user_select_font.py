import sublime
import sublime_plugin

PREFS_FILE = 'Preferences.sublime-settings'

CURRENT_KIND = (sublime.KIND_ID_COLOR_GREENISH, "✓", "Current")


class FontInputHandler(sublime_plugin.ListInputHandler):

    def __init__(self):
        super().__init__()
        self.prefs = sublime.load_settings(PREFS_FILE)
        self.original = self.prefs.get("font_face", "")

    def placeholder(self):
        return "Select Font"

    def cancel(self):
        self.prefs.set('font_face', self.original)
        sublime.save_settings(PREFS_FILE)

    def confirm(self):
        sublime.save_settings(PREFS_FILE)

    def preview(self, font_face):
        if font_face is None:
            return

        self.last_previewed = font_face

        def update():
            # The color scheme to preview has been updated since
            # the timeout was created
            if font_face != self.last_previewed:
                return
            if self.prefs.get('font_face') == font_face:
                return
            self.prefs.set('font_face', font_face)

        sublime.set_timeout(update, 250)

    def list_items(self):
        fonts = self.prefs.get('fonts')
        fonts = set(fonts) if isinstance(fonts, list) else set()
        fonts.add(self.prefs.get("font_face"))

        items = []
        selected = -1
        for font in sorted(fonts):
            kind_info = sublime.KIND_AMBIGUOUS
            if self.original and self.original == font:
                kind_info = CURRENT_KIND
                selected = len(items)

            items.append(sublime.ListInputItem(font, font, kind=kind_info))

        return (items, selected)


class SelectFontCommand(sublime_plugin.WindowCommand):

    def input_description(self):
        return "Font:"

    def input(self, args):
        return FontInputHandler()

    def run(self, font_face):
        settings = sublime.load_settings(PREFS_FILE)
        settings.set('font_face', font_face)
        sublime.save_settings(PREFS_FILE)
