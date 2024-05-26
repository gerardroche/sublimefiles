import sublime_plugin


class UserDumpScope(sublime_plugin.WindowCommand):

    def run(self):
        view = self.window.active_view()
        scopes = []
        for point in range(view.size()):
            scopes.append(view.scope_name(point).strip())

        print(">>>\n".join(scopes) + '<<<')
