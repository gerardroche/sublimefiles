# When you see something you like and would like to use it, open an issue about
# abstracting it out into a reusable package, possibly installable via Package
# Control.

import sublime_plugin


class TasksCommand(sublime_plugin.WindowCommand):

    def run(self, interactive=True):
        self.window.run_command('show_panel', {
            'panel': 'find_in_files',
            'where': '<open folders>,-.srcpath/,-.buildpath/,-vendor/,-res/doc/',
            'whole_word': False,
            'case_sensitive': False,
            'preserve_case': False,
            'regex': True,
            'use_buffer': False,
            'show_context': False,
        })

        self.window.run_command('insert', {
            'characters': '(#|//)\\s*(TODO|FIXME|XXX|IMPORTANT|DEPRECATED)'
        })

        if not interactive:
            self.window.run_command('find_all', {'close_panel': True})
