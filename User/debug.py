import os


import sublime

DEBUG_SCREAM = False
DEBUG = bool(os.getenv('SUBLIME_DEBUG'))
DEBUG_COMMAND = bool(os.getenv('SUBLIME_COMMAND_DEBUG'))
DEBUG_RESULT_REGEX = bool(os.getenv('SUBLIME_RESULT_REGEX_DEBUG'))
DEBUG_INDEXING = bool(os.getenv('SUBLIME_INDEXING_DEBUG'))
DEBUG_BUILD_SYSTEMS = bool(os.getenv('SUBLIME_BUILD_SYSTEMS_DEBUG'))
DEBUG_INPUT = bool(os.getenv('SUBLIME_INPUT_DEBUG'))


def plugin_loaded():
    sublime.log_commands(DEBUG_SCREAM or (DEBUG and DEBUG_COMMAND))
    sublime.log_result_regex(DEBUG_SCREAM or (DEBUG and DEBUG_RESULT_REGEX))
    sublime.log_indexing(DEBUG_SCREAM or (DEBUG and DEBUG_INDEXING))
    sublime.log_build_systems(DEBUG_SCREAM or (DEBUG and DEBUG_BUILD_SYSTEMS))
    sublime.log_input(DEBUG_SCREAM or (DEBUG and DEBUG_INPUT))


def message(*args):
    print(*args)


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
