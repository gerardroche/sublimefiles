import os

import sublime
import sublime_plugin


_DEBUG = bool(os.getenv('SUBLIME_DEBUG'))
_AUTO_SHOW_PANEL = bool(os.getenv('SUBLIME_DEBUG'))


def var_dump(value):
    if isinstance(value, sublime.View):
        print('>>>' + str(dir(value)))
        print('  id = ' + str(value.id()))
        print('  buffer_id = ' + str(value.buffer_id()))
        print('  is_valid = ' + str(value.is_valid()))
        print('  is_primary = ' + str(value.is_primary()))
        print('  name = ' + str(value.name()))
        print('  is_loading = ' + str(value.is_loading()))
        print('  is_dirty = ' + str(value.is_dirty()))
        print('  is_read_only = ' + str(value.is_read_only()))
        print('  encoding = ' + str(value.encoding()))
        print('  line_endings = ' + str(value.line_endings()))
        print('  size = ' + str(value.size()))
        print('  is_in_edit = ' + str(value.is_in_edit()))
        print('  change_count = ' + str(value.change_count()))
        print('  sel = ' + str(value.sel()))
        print('  viewport_position = ' + str(value.viewport_position()))
        print('  layout_extent = ' + str(value.layout_extent()))
        print('  line_height = ' + str(value.line_height()))
        print('  em_width = ' + str(value.em_width()))
        print('  folded_regions = ' + str(value.folded_regions()))
        print('  symbols = ' + str(value.symbols()))
        print('  indexed_symbols = ' + str(value.indexed_symbols()))
        print('  find_all_results = ' + str(value.find_all_results()))
        print('  overwrite_status = ' + str(value.overwrite_status()))
        print('  is_auto_complete_visible = ' + str(value.is_auto_complete_visible()))
        print('<<<')
    else:
        print('  Unknown type: ' + str(value))


class ToggleDebugMode(sublime_plugin.ApplicationCommand):

    def run(self):
        global _DEBUG
        _DEBUG = not _DEBUG
        sublime.log_commands(_DEBUG)
        sublime.log_result_regex(_DEBUG)
        sublime.log_indexing(_DEBUG)
        sublime.log_build_systems(_DEBUG)
        sublime.log_input(_DEBUG)


class DebugViewToScopeCommand(sublime_plugin.TextCommand):
    """
    Dump view scope name representation.

    Each point in the view is converted to a scope name.  A newline is appended
    to each scope name.
    """

    def run(self, edit):
        scopes = []
        for point in range(self.view.size()):
            scopes.append(self.view.scope_name(point).strip())

        print('>>>')
        print("\n".join(scopes))
        print('<<<')


def plugin_loaded():
    if _AUTO_SHOW_PANEL:
        sublime.active_window().run_command('show_panel', {'panel': 'console'})

    sublime.log_commands(_DEBUG)
    sublime.log_result_regex(_DEBUG)
    sublime.log_indexing(_DEBUG)
    sublime.log_build_systems(_DEBUG)
    sublime.log_input(_DEBUG)
