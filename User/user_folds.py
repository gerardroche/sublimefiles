# When you see something you like and would like to use it, open an issue about
# abstracting it out into a reusable package, possibly installable via Package
# Control.

from Default.fold import FoldCommand as DefaultFoldCommand
from Default.fold import UnfoldCommand as DefaultUnfoldCommand


def _post_fold_command_fixes(view):
    # Reset cursors to begining and start of
    # lines and clear any visual selections.
    sels = []
    for sel in view.sel():
        sels.append(view.text_point(view.rowcol(sel.begin())[0], 0))

    if sels:
        view.sel().clear()
        view.sel().add_all(sels)


class FoldCommand(DefaultFoldCommand):
    def run(self, edit):
        super().run(edit)
        _post_fold_command_fixes(self.view)


class UnfoldCommand(DefaultUnfoldCommand):
    def run(self, edit):
        super().run(edit)
        _post_fold_command_fixes(self.view)
