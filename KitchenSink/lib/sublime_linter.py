# Copyright (C) 2024 Gerard Roche
#
# This file is part of KitchenSink.
#
# KitchenSink is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# KitchenSink is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with KitchenSink.  If not, see <https://www.gnu.org/licenses/>.


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
