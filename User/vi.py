import sublime
import os
import re

def plugin_loaded():
    load_vimrc()

def load_vimrc():

    vimrc_file = os.path.expanduser('~/.vimrc')

    if not os.path.isfile(vimrc_file):
        return

    settings = sublime.load_settings('Preferences.sublime-settings')

    vim_settings = [
        'scrolloff',
        'sidescrolloff',
        'sidescroll',
        'splitright',
        'splitbelow',
    ]

    def parse_vimrc_file_line(line):
        line = line.strip()

        res = re.search('^set ([a-z]+)(?:=([a-zA-Z0-9-]+))?\s*(?:\".*)?$', line)
        if res:

            key = res.group(1)
            value = res.group(2)

            if value == None:
                if key[:2] == 'no':
                    value = False
                else:
                    value = True

            return {'key': key, 'value': value}

        return None

    with open(vimrc_file, 'r') as f:
        for line in f:
            setting = parse_vimrc_file_line(line)
            if setting:
                if setting['key'] in vim_settings:
                    settings.set(setting['key'], setting['value'])

# from Vintageous import plugins
# from Vintageous.vi import keys
# from Vintageous.vi.cmd_base import ViMotionDef
# from Vintageous.vi.cmd_base import ViOperatorDef
# from Vintageous.vi.core import ViWindowCommandBase
# from Vintageous.vi.utils import modes
# import sublime

# # { "keys": ["ctrl+shift+alt+j"], "command": "git_gutter_next_change" },
# # { "keys": ["ctrl+shift+alt+k"], "command": "git_gutter_prev_change" },

# @plugins.register('c]', (modes.NORMAL,))
# class _vi_def_right_bracket_c(ViOperatorDef):

#     def __init__(self, *args, **kwargs):
#         ViOperatorDef.__init__(self, *args, **kwargs)

#     def translate(self, state):
#         cmd = {}
#         cmd['action'] = '_vi_right_bracket_c'
#         cmd['action_args'] = {}
#         return cmd

# class _vi_right_bracket_c(ViWindowCommandBase):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     def run(self):
#         self.window.run_command('git_gutter_next_change')
