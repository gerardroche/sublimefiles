import sublime
import sublime_plugin
import os

DEBUG=bool(os.getenv('SUBLIME_DEBUG'))
DEBUG_INPUT=bool(os.getenv('SUBLIME_DEBUG_INPUT'))

if DEBUG:
    def debug_message(message):
        print('DEBUG %s' % str(message))
else:
    def debug_message(message):
        pass

def plugin_loaded():
    sublime.log_commands(DEBUG)
    sublime.log_result_regex(DEBUG)
    sublime.log_indexing(DEBUG)
    sublime.log_build_systems(DEBUG)
    sublime.log_input(DEBUG_INPUT)
