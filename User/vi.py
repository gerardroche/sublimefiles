import os
import re


import sublime


from Vintageous import plugins
from Vintageous.vi import keys
from Vintageous.vi.cmd_base import ViMotionDef
from Vintageous.vi.cmd_base import ViOperatorDef
from Vintageous.vi.core import ViWindowCommandBase
from Vintageous.vi.utils import modes


def plugin_loaded():
    init_vimrc()


def init_vimrc():

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


    vimrc_file = os.path.expanduser('~/.vimrc')
    if not os.path.isfile(vimrc_file):
        return

    implemented_vim_settings = [
        'scrolloff',
        'sidescrolloff',
        'sidescroll',
        'splitright',
        'splitbelow',
    ]

    settings = sublime.load_settings('Preferences.sublime-settings')
    with open(vimrc_file, 'r') as f:
        for line in f:
            setting = parse_vimrc_file_line(line)
            if setting:
                if setting['key'] in implemented_vim_settings:
                    settings.set(setting['key'], setting['value'])


@plugins.register(seq=']c', modes=(modes.NORMAL,))
class _vi_def_right_bracket_c(ViOperatorDef):
    def translate(self, state):
        return {
            'action': 'git_gutter_next_change',
            'action_args': {}
        }


@plugins.register(seq='[c', modes=(modes.NORMAL,))
class _vi_def_left_bracket_c(ViOperatorDef):
    def translate(self, state):
        return {
            'action': 'git_gutter_prev_change',
            'action_args': {}
        }
