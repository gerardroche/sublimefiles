# When you see something you like and would like to use it, open an issue about
# abstracting it out into a reusable package, possibly installable via Package
# Control.


import sublime_plugin


class RulersCommand(sublime_plugin.TextCommand):

    def run(self, edit, action):
        col = self.view.rowcol(self.view.sel()[0].begin())[1]
        if col > 0:
            queue_save = False
            settings = self.view.settings()
            rulers = settings.get('rulers')

            if action == 'add':
                if col not in rulers:
                    rulers.append(col)
                    queue_save = True
            elif action == 'remove':
                if col in rulers:
                    rulers.remove(col)
                    queue_save = True
            elif action == 'clear':
                if rulers != []:
                    rulers = []
                    queue_save = True
            else:
                raise Exception('unknown action')

            if queue_save:
                rulers.sort()
                if rulers:
                    settings.set('rulers', rulers)
                else:
                    settings.erase('rulers')
