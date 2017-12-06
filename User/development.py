import functools
import os

from sublime import load_resource
from sublime import load_settings
from sublime import packages_path
from sublime import save_settings
from sublime import set_timeout_async
import sublime_plugin


class NeovintageousDevCommand(sublime_plugin.WindowCommand):

    def run(self, action):
        if action == 'toggle_use_ctrl_keys':
            self.toggle_use_ctrl_keys()
        elif action == 'fixup_docs':
            self.fixup_docs()
        elif action == 'assign_help_syntax':
            self.assign_help_syntax()
        else:
            raise Exception('action not found')

    def toggle_use_ctrl_keys(self):
        preferences = load_settings('Preferences.sublime-settings')
        use_ctrl_keys = preferences.get('vintageous_use_ctrl_keys')
        preferences.set('vintageous_use_ctrl_keys', not use_ctrl_keys)
        save_settings('Preferences.sublime-settings')

    def assign_help_syntax(self):
        view = self.window.active_view()
        if not view:
            raise Exception('view not found')

        view.assign_syntax('Packages/NeoVintageous/res/Help.sublime-syntax')

    def fixup_docs(self):
        print('NeoVintageousDev: Fixing docs..')

        docs_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'NeoVintageous/res/doc')

        for f in os.listdir(docs_path):
            if f.endswith('.txt'):
                resource = 'Packages/NeoVintageous/res/doc/%s' % f

                exception = False
                try:
                    load_resource(resource)
                except Exception as e:
                    exception = e

                if exception:
                    print('  Error: ' + resource + ' ' + str(exception))

                    file = packages_path() + '/NeoVintageous/res/doc/%s' % f
                    print('    Fixing resource encoding for \'{}\''.format(file))

                    view = self.window.open_file(file)

                    def f(view):
                        view.run_command('set_encoding', {'encoding': 'utf-8'})
                        view.run_command('save')
                        view.close()

                    set_timeout_async(functools.partial(f, view), 200)
