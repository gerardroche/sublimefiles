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

from sublime import decode_value
from sublime import load_resource
import sublime_plugin


def decode_resource(name: str):
    return decode_value(load_resource(name))


class KitchenSinkAuditPreferences(sublime_plugin.WindowCommand):

    def run(self):
        defaults = decode_resource('Packages/Default/Preferences.sublime-settings')
        user = decode_resource('Packages/User/Preferences.sublime-settings')

        for name, value in defaults.items():
            if user.get(name) == value:
                print('Found redundant setting: {}={}'.format(name, value))

            if name in ('file_exclude_patterns', 'folder_exclude_patterns'):
                for exclude_pattern in value:
                    if exclude_pattern not in user.get(name):
                        print('Found exclude pattern missing from ' + name + ':', exclude_pattern)
