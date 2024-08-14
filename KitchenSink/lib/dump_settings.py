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

import sublime_plugin


class KitchenSinkDumpSettings(sublime_plugin.WindowCommand):

    def run(self, prefixes=None):
        print('\n\n')
        print('----- Dump Settings -----')
        print('\n\n')

        view = self.window.active_view()
        settings = view.settings().to_dict()

        for name, value in settings.items():
            display = False if prefixes else True
            if not display:
                for prefix in prefixes:
                    if name.startswith(prefix):
                        display = True
                        continue

            if display:
                print('  ', name, '=>', value)

        print('\n\n')
