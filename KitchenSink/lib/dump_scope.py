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


class KitchenSinkDumpScope(sublime_plugin.WindowCommand):

    def run(self):
        view = self.window.active_view()
        scopes = []
        for point in range(view.size()):
            scopes.append(view.scope_name(point).strip())

        print(">>>\n".join(scopes) + '<<<')
