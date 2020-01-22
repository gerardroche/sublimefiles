import sublime_plugin


class UserSetLayoutCommand(sublime_plugin.WindowCommand):

    def run(self, cols, rows, cells):
        num_groups_before = self.window.num_groups()
        active_group_before = self.window.active_group()

        self.window.run_command('set_layout', {
            'cols': cols,
            'rows': rows,
            'cells': cells
        })

        if num_groups_before == self.window.num_groups():
            # Fix issue where group focus moves when it probably shouldn't.
            # When the layout is not changed then the focus shouldn't change
            # either. Previously, if the active view before the layout change
            # is transient ST would move the cursor focus to a group with a
            # non-transient view. This can be disorienting and interrupt flow
            # because where the cursor focus has moved to is not always clear.
            self.window.focus_group(active_group_before)
            return

        if len(self.window.views_in_group(active_group_before)) < 2:
            # Only move the active view before layout change to the new group
            # if it doesn't leave the previous group without any views.
            return

        view = self.window.active_view_in_group(active_group_before)

        self.window.set_view_index(view, self.window.active_group(), 0)
