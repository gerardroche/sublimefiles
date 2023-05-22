import sublime_plugin


class UserDumpScope(sublime_plugin.WindowCommand):

    def run(self):
        view = self.window.active_view()
        scopes = []
        for point in range(view.size()):
            # scope_name() needs to striped due to a bug in ST:
            # See https://github.com/SublimeTextIssues/Core/issues/657.
            scopes.append(view.scope_name(point).strip())

        print(">>>\n".join(scopes) + '<<<')
