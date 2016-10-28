import sublime_plugin


class ResizeGroupsAlmostEquallyCommand(sublime_plugin.WindowCommand):

    """
    Make all groups (almost) equally high and wide, but use 'winheight' and
    'winwidth' for the current window.  Windows with 'winfixheight' set keep
    their height and windows with 'winfixwidth' set keep their width.
    @xxx winheight option
    @xxx winwidth option
    @xxx winfixheight option
    @xxx winfixwidth option
    """

    def run(self):

        layout = self.window.layout()
        col_count = len(layout['cols'])
        row_count = len(layout['rows'])

        def equalise(count):
            size = round(1.0 / (count - 1), 2)
            vals = [0.0]
            for i in range(1, count - 1):
                vals.append(round(size * i, 2))
            vals.append(1.0)
            return vals

        if col_count > 2:
            layout['cols'] = equalise(col_count)

        if row_count > 2:
            layout['rows'] = equalise(row_count)

        if col_count > 2 or row_count > 2:
            self.window.set_layout(layout)
