# Copyright (C) 2024 Gerard Roche
#
# This file is part of KitchenSink.
#
# KitchenSink is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# KitchenSink is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with KitchenSink.  If not, see <https://www.gnu.org/licenses/>.


import sublime_plugin


class Tiler(sublime_plugin.WindowCommand):

    def run(self, name):
        layout = _LAYOUTS.get(name)
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


_LAYOUTS = {
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
    },
    "grid:6": {
        "cols": [0.0, 0.33, 0.66, 1.0],
        "rows": [0.0, 0.5, 1.0],
        "cells": [
            [0, 0, 1, 1], [1, 0, 2, 1], [2, 0, 3, 1],
            [0, 1, 1, 2], [1, 1, 2, 2], [2, 1, 3, 2]
        ]
    }
}
