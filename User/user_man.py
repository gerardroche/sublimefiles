import glob
import os
import re
import webbrowser

import sublime_plugin

from GotoPhpManual.plugin import _get_path  # type: ignore


class ManCommand(sublime_plugin.WindowCommand):

    def run(self):
        view = self.window.active_view()
        if not view:
            return

        path = _get_path(view)
        if not path:
            return

        manual_paths = []
        manual_names = []
        for manual_path in glob.glob(path + '/*/index.html'):
            re_match_res = re.match('^.*\\/([a-zA-Z0-9-_.]+)\\/index.html$', manual_path)
            if re_match_res:
                manual_paths.append(manual_path)
                manual_names.append(re_match_res.group(1))

        self.manuals = (manual_paths, manual_names)

        self.window.show_quick_panel(self.manuals[1], self.on_done)

    def on_done(self, index):
        if index == -1:
            return

        manual = self.manuals[0][index]

        if os.path.isfile(manual):
            webbrowser.open_new_tab('file://%s' % (manual))
