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

import re

import sublime_plugin


class GitFormatGithubUrlCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        line = self.view.line(self.view.sel()[0].b)

        # Try convert https://github.com/x/y/issues/42 to trackback x/y#42.
        url_region = self.view.find(
            'https:\\/\\/github.com'
            '\\/[a-zA-Z0-9_-]+'
            '\\/[a-zA-Z0-9_-]+'
            '\\/issues\\/[0-9]+',
            line.begin())

        if url_region:
            url = self.view.substr(url_region)
            url = url.replace('https://github.com/', '')
            url = url.replace('/issues/', '#')

            self.view.replace(edit, url_region, url)
        else:
            # Try convert x/y#42 -> GitHub url.

            url_region = self.view.find(
                '[a-zA-Z0-9_-]+'
                '\\/[a-zA-Z0-9_-]+'
                '#[0-9]+',
                line.begin())

            if url_region:
                url = self.view.substr(url_region)
                url = 'https://github.com/' + url
                url = url.replace('#', '/issues/')

                self.view.replace(edit, url_region, url)


def _create_github_url(*args):
    return 'https://github.com/%s' % ('/'.join(args))


def _extract_github_url(view):
    line = view.line(view.sel()[0].b)
    line = view.substr(line)

    # Format: <githubdomain>/x/y, <githubdomain>/x/y/issues/#<number>

    match = re.match(
        '^.*'
        '(?P<url>https:\\/\\/github\\.com'
        '\\/[a-zA-Z0-9_-]+\\/[a-zA-Z0-9_-]+'
        '(?:\\/issues\\/[0-9]+)?'
        ')',
        line
    )

    if match:
        return match.group('url')

    # Format: x/y, x/y#<number>

    match = re.findall(
        '[a-zA-Z0-9_-]+\\/[a-zA-Z0-9_-]+(?:#[0-9]+)?',
        line
    )

    if match:
        return _create_github_url(match[0].replace('#', '/issues/'))

    match = re.findall('[a-f0-9]{40}', line)
    if match:
        return _create_github_url('NeoVintageous/NeoVintageous/commits', match[0])

    match = re.findall('#[0-9]+', line)
    if match:
        return _create_github_url('NeoVintageous/NeoVintageous/issues', match[0].replace('#', ''))
