# ==============================================================================
# 3. Jumping to diffs                                     jumpto-diffs
#
# Two commands can be used to jump to diffs:
#                                                                 [c
#         [c              Jump backwards to the previous start of a change.
#                         When a count is used, do it that many times.
#                                                                 ]c
#         ]c              Jump forwards to the next start of a change.
#                         When a count is used, do it that many times.
#
# It is an error if there is no change for the cursor to move to.
#
# See https://neovim.io/doc/user/diff.html#jumpto-diffs

from NeoVintageous.lib.api import plugin
from NeoVintageous.lib.vi.cmd_base import ViOperatorDef


@plugin.register(seq=']c', modes=(plugin.modes.NORMAL,))
class NeoVintageousGitGutterJumpBackwards(ViOperatorDef):
    def translate(self, state):
        return {
            'action': 'git_gutter_next_change',
            'action_args': {}
        }


@plugin.register(seq='[c', modes=(plugin.modes.NORMAL,))
class NeoVintageousGitGutterJumpForwards(ViOperatorDef):
    def translate(self, state):
        return {
            'action': 'git_gutter_prev_change',
            'action_args': {}
        }
