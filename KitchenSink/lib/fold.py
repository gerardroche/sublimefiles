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


class FoldAllCssClasses(sublime_plugin.TextCommand):

    def run(self, edit):
        selector = "text.html meta.tag meta.attribute-with-value.class.html meta.string.html string.quoted.double.html - punctuation"  # noqa: E501
        selectors = self.view.find_by_selector(selector)
        self.view.fold(selectors)
