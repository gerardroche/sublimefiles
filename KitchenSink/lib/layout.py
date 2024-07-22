import sublime_plugin


class KitchenSinkLayout(sublime_plugin.WindowCommand):

    def run(self, name):
        layout = _NAMED_LAYOUTS.get(name)
        if layout:
            # num_groups_before = self.window.num_groups()
            # active_group_before = self.window.active_group()

            self.window.run_command('set_layout', layout)

            # if num_groups_before == self.window.num_groups():
            #     # Fix issue where group focus moves when it probably shouldn't.
            #     #
            #     # When the layout is not changed then the focus shouldn't change
            #     # either.
            #     #
            #     # Previously, if the active view before the layout change
            #     # is transient ST would move the cursor focus to a group with a
            #     # non-transient view. This can be disorienting and interrupt flow
            #     # because where the cursor focus has moved to is not always clear.
            #     self.window.focus_group(active_group_before)
            #     return
            # if len(self.window.views_in_group(active_group_before)) < 2:
            #     # Only move the active view before layout change to the new group
            #     # if it doesn't leave the previous group without any views.
            #     return
            # view = self.window.active_view_in_group(active_group_before)
            # self.window.set_view_index(view, self.window.active_group(), 0)

_NAMED_LAYOUTS = {
    "single": {
        "cols": [0.0, 1.0],
        "rows": [0.0, 1.0],
        "cells": [[0, 0, 1, 1]]
    },
    "cols:2": {
        "cols": [0.0, 0.5, 1.0],
        "rows": [0.0, 1.0],
        "cells": [[0, 0, 1, 1], [1, 0, 2, 1]]
    },
    "cols:3": {
        "cols": [0.0, 0.33, 0.66, 1.0],
        "rows": [0.0, 1.0],
        "cells": [[0, 0, 1, 1], [1, 0, 2, 1], [2, 0, 3, 1]]
    },
    "cols:4": {
        "cols": [0.0, 0.25, 0.5, 0.75, 1.0],
        "rows": [0.0, 1.0],
        "cells": [[0, 0, 1, 1], [1, 0, 2, 1], [2, 0, 3, 1], [3, 0, 4, 1]]
    },
    "rows:2": {
        "cols": [0.0, 1.0],
        "rows": [0.0, 0.5, 1.0],
        "cells": [[0, 0, 1, 1], [0, 1, 1, 2]]
    },
    "rows:3": {
        "cols": [0.0, 1.0],
        "rows": [0.0, 0.33, 0.66, 1.0],
        "cells": [[0, 0, 1, 1], [0, 1, 1, 2], [0, 2, 1, 3]]
    },
    "grid:4": {
        "cols": [0.0, 0.5, 1.0],
        "rows": [0.0, 0.5, 1.0],
        "cells": [
            [0, 0, 1, 1], [1, 0, 2, 1],
            [0, 1, 1, 2], [1, 1, 2, 2]
        ]
    }
}
