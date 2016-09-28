import os
import sublime

def plugin_loaded():
    sublime.log_commands(bool(os.getenv('SUBLIME_DEBUG')))
    sublime.log_result_regex(bool(os.getenv('SUBLIME_DEBUG')))
    sublime.log_indexing(bool(os.getenv('SUBLIME_DEBUG')))
    sublime.log_build_systems(bool(os.getenv('SUBLIME_DEBUG')))
    sublime.log_input(bool(os.getenv('SUBLIME_DEBUG')) and bool(os.getenv('SUBLIME_INPUT_DEBUG')))
