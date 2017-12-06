from Default.fold import FoldCommand as DefaultFoldCommand
from Default.fold import UnfoldCommand as DefaultUnfoldCommand


def _fixup_selections(view):
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
        _fixup_selections(self.view)


class UnfoldCommand(DefaultUnfoldCommand):

    def run(self, edit):
        super().run(edit)
        _fixup_selections(self.view)
