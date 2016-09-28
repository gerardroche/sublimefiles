import re
import glob
import re
import webbrowser
import os

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

# Re: https://akrabat.com/hide-the-st3-sidebar-automatically/
# class FlowListener(sublime_plugin.EventListener):

#     def on_activated(self, view):
#         if not view:
#             return

#         window = view.window()
#         if not window:
#             return

#         if len(window.views()) == 0:
#             window.set_sidebar_visible(True)
#             window.run_command('focus_side_bar')
#         elif window.is_sidebar_visible():
#             window.set_sidebar_visible(False)

def is_php_identifier(value):
    return re.match('^[a-zA-Z_][a-zA-Z0-9_]*$', value)

def man_path(window):
    view = window.active_view()

    if not view:
        return None

    path = view.settings().get('man.path')

    if not path:
        return None

    env_projects_path = os.getenv('PROJECTS_PATH')
    if env_projects_path:
        if not os.path.isdir(env_projects_path):
            raise RuntimeError('PROJECTS_PATH env is not a valid directory')

        path = path.replace('${PROJECTS_PATH}', env_projects_path)

    if not path:
        return None

    if not os.path.isdir(path):
        return None

    return path

class ManCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.items = self.manuals()
        self.window.show_quick_panel(self.items[1], self.on_select)

    def on_select(self, picked):
        if picked == -1:
            return

        selected_item = self.items[0][picked]
        if os.path.isfile(selected_item):
            webbrowser.open_new_tab('file://%s' % (selected_item))

    def manuals(self):
        manual_paths = []
        manual_names = []
        path = man_path(self.window)
        if path and os.path.isdir(path):
            for manual_path in glob.glob(path + '/*/index.html'):
                re_match_res = re.match('^.*\/([a-zA-Z0-9-_.]+)\/index.html$', manual_path)
                if re_match_res:
                    manual_paths.append(manual_path)
                    manual_names.append(re_match_res.group(1))

        return (manual_paths, manual_names)

class GotoPhpManCommand(sublime_plugin.WindowCommand):

    def run(self, remote = False):
        view = self.window.active_view()
        if not view:
            return

        symbol = view.substr(view.word(view.sel()[0]))
        if not is_php_identifier(symbol):
            return

        symbol = symbol.replace('_', '-').lower()

        if remote:
            self.goto_remote(symbol)
        else:
            self.goto_local(symbol)

    def goto_remote(self, symbol):
        webbrowser.open_new_tab('https://secure.php.net/%s' % symbol)

    def goto_local(self, symbol):
        path = man_path(self.window)
        if not path:
            return

        def open_file_in_browser(filename):
            if os.path.isfile(filename):
                webbrowser.open_new_tab('file://%s' % filename)
            else:
                sublime.status_message('goto_php_manual: file not found: %s' % filename)

        # https://secure.php.net/urlhowto.php
        open_file_in_browser('%s/php/language.types.%s.html' % (path, symbol))
        open_file_in_browser('%s/php/control-structures.%s.html' % (path, symbol))
        open_file_in_browser('%s/php/book.%s.html' % (path, symbol))
        open_file_in_browser('%s/php/class.%s.html' % (path, symbol))
        open_file_in_browser('%s/php/function.%s.html' % (path, symbol))

class SmarterInsertNewlineCommand(sublime_plugin.TextCommand):

    """
    Inserts a newline if the next line is not blank, otherwise
    moves down to the blank line.
    """

    def run(self, edit):

        if len(self.view.sel()) == 0: return
        if len(self.view.sel()) != 1: return # doesn't support multiple selections

        cursor_point = self.view.sel()[0].begin()
        cursor_line_region = self.view.full_line(cursor_point)
        cursor_line_as_string = self.view.substr(cursor_line_region)
        cursor_line_has_eol_punctutation = re.search('(\\{|\\[)s*$', cursor_line_as_string)

        if cursor_line_has_eol_punctutation:

            next_line_region = self.view.full_line(cursor_line_region.end())
            next_line_as_string = self.view.substr(next_line_region)
            next_line_is_blank = re.match('^\\s*$', next_line_as_string)

            self.view.run_command('move_to', {'to': 'hardeol'})

            if next_line_is_blank:
                self.view.run_command('move', {'by': 'lines', 'forward': True})
            else:
                self.view.run_command('insert', {'characters': '\n'})

            self.view.run_command('move_to', {'to': 'hardeol', 'extend': False})
            self.view.run_command('reindent', {'single_line': True})

class ResizeGroupsAlmostEquallyCommand(sublime_plugin.WindowCommand):

    """
    Make all groups (almost) equally high and wide, but use 'winheight' and
    'winwidth' for the current window.  Windows with 'winfixheight' set keep
    their height and windows with 'winfixwidth' set keep their width.
    @xxx winheight option
    @xxx winwidth option
    @xxx winfixheight option
    @xxx winfixwidth option
    """

    def run(self):

        layout = self.window.layout()
        col_count = len(layout['cols'])
        row_count = len(layout['rows'])

        def equalise(count):
            size = round(1.0 / (count - 1), 2)
            vals = [0.0]
            for i in range(1, count - 1):
                vals.append(round(size * i, 2))
            vals.append(1.0)
            return vals

        if col_count > 2:
            layout['cols'] = equalise(col_count)

        if row_count > 2:
            layout['rows'] = equalise(row_count)

        if col_count > 2 or row_count > 2:
            self.window.set_layout(layout)

class AsciiInfoCommand(sublime_plugin.TextCommand):

    """
    http://vimdoc.sourceforge.net/htmldoc/various.html#ga
    """

    def run(self, edit):

        def character_to_notation(character):

            """
            Convert a character to a key notation.
            Uses vim key notation.
            http://vimdoc.sourceforge.net/htmldoc/intro.html#key-notation
            """

            character_notation_map = {
                "\0": "Nul",
                " ": "Space",
                "\t": "Tab",
                "\n": "NL"
            }

            if character in character_notation_map:
                character = character_notation_map[character]

            return "<" + character + ">"

        for region in self.view.sel():

            c_str = self.view.substr(region.begin())
            c_ord = ord(c_str)
            c_hex = hex(c_ord)
            c_oct = oct(c_ord)
            c_not = self.character_to_notation(c_str)

            msg_template = "%7s %3s,  Hex %4s,  Octal %5s"

            return sublime.status_message(msg_template % (c_not, c_ord, c_hex, c_oct))

class EnableThemeCommand(sublime_plugin.ApplicationCommand):

    def run(self):

        self.themes = []

        for theme in sublime.find_resources('*.sublime-theme'):
            if "Addon" not in theme:
                self.themes.append(os.path.basename(theme))

        if len(self.themes) > 0:
            sublime.active_window().show_quick_panel(
                self.themes,
                self.on_done
            )

    def on_done(self, index):
        if index == -1:
            return

        theme = self.themes[index]

        settings = sublime.load_settings('Preferences.sublime-settings')
        settings.set('theme', theme)
        sublime.save_settings('Preferences.sublime-settings')

class EnableColorSchemeCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        self.color_schemes = []

        for color_scheme in sublime.find_resources('*.tmTheme'):
            if "(SL)" not in color_scheme:
                self.color_schemes.append(color_scheme)

        if len(self.color_schemes) > 1:

            color_scheme = sublime.load_settings('Preferences.sublime-settings').get('color_scheme')

            if color_scheme not in self.color_schemes:
                self.color_schemes.insert(0, color_scheme)

            sublime.active_window().show_quick_panel(
                self.color_schemes,
                self.on_done,
                0,
                self.color_schemes.index(color_scheme),
                self.on_select
            )

    def on_select(self, index):
        if index == -1:
            return

        color_scheme = self.color_schemes[index]
        window = sublime.active_window()
        for group in range(0, window.num_groups()):
            active_view_in_group = window.active_view_in_group(group)
            if active_view_in_group:
                active_view_in_group.settings().set('color_scheme', color_scheme)

    def on_done(self, index):
        for view in sublime.active_window().views():
            view.settings().erase('color_scheme')

        if index == -1:
            return

        color_scheme = self.color_schemes[index]

        settings = sublime.load_settings('Preferences.sublime-settings')
        settings.set('color_scheme', color_scheme)
        sublime.save_settings('Preferences.sublime-settings')
