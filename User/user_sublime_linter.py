# When you see something you like and would like to use it, open an issue about
# abstracting it out into a reusable package, possibly installable via Package
# Control.

from sublime import load_settings
from sublime import save_settings
import sublime_plugin


class LintersCommand(sublime_plugin.WindowCommand):

    def run(self, action):
        settings = load_settings('SublimeLinter.sublime-settings')

        if action == 'toggle_mode':
            lint_mode = settings.get('lint_mode')
            if lint_mode:
                if lint_mode != 'load_save':
                    lint_mode = 'load_save'
                else:
                    lint_mode = 'background'

            settings.set('lint_mode', lint_mode)
            save_settings('SublimeLinter.sublime-settings')

            return

        # TODO How to get a real list of installed linters?
        linters = settings.get('linters')

        items = []
        for linter, linter_settings in linters.items():
            is_disabled = linter_settings.get('disable', False)

            if action == 'disable':
                if not is_disabled:
                    items.append(linter)
            elif action == 'enable':
                if is_disabled:
                    items.append(linter)
            elif action == 'toggle':
                items.append(linter)
            else:
                raise RuntimeError('unknown action')

        def on_done(index):
            if index >= 0:
                linter = items[index]

                if action == 'disable':
                    disable = True
                elif action == 'enable':
                    disable = False
                elif action == 'toggle':
                    if 'disable' in linters[linter]:
                        disable = not linters[linter]['disable']
                    else:
                        disable = True

                linters[linter]['disable'] = disable
                settings.set('linters', linters)
                save_settings('SublimeLinter.sublime-settings')

        self.window.show_quick_panel(items, on_done)
