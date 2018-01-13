import sublime_plugin


# When you see something you like and would like to use it, open an issue about
# abstracting it out into a reusable package, possibly installable via Package
# Control.


def _is_at_close_param(view):
    for s in view.sel():
        if view.substr(s.end()) != ')':
            return False

    return True


class Initiative(sublime_plugin.EventListener):
    def on_query_context(self, view, key, operator, operand, match_all):
        if key == 'initiative':
            return _is_at_close_param(view)


class InitiativeCommand(sublime_plugin.TextCommand):
    def run(self, edit, key):
        if key in (')', 'backspace') and _is_at_close_param(self.view):
            for s in self.view.sel():
                self.view.erase(edit, s)

            self.view.run_command('move', {
                'by': 'characters',
                'forward': True
            })
