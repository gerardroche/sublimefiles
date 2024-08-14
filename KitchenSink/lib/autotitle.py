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

import sublime
import sublime_plugin


class Autotitle(sublime_plugin.TextCommand):

    def run(self, edit):
        for sel in reversed(self.view.sel()):
            _autotitle(self.view, edit, sel.b)


def _autotitle(view, edit, point: int) -> None:
    classes = sublime.CLASS_WORD_START | sublime.CLASS_WORD_END
    region = view.expand_by_class(point, classes, ' ')
    if not region:
        return

    link = view.substr(region)
    if not link:
        return

    reusable = re.match('^reusables\\.([a-z\\.-]+)$', link)
    if reusable:
        region.a -= 8
        region.b += 3
        replacement = '<!--@include:@data/{}.md-->'.format(reusable.group(0).replace('.', '/'))
        view.replace(edit, region, replacement)
        return

    markdown_link = get_params(link)
    if markdown_link:
        prefix, text, href, suffix = markdown_link
        href = _filter_href(href)
        text = _filter_text(href)
        replacement = '{}[{}]({}){}'.format(prefix, text, href, suffix)
        view.replace(edit, region, replacement)
        return


def _filter_href(href: str) -> str:
    href = href.replace('github', 'appx')

    return href


def _filter_text(href: str) -> str:
    parts = href.split('/')
    text = parts[-1]
    text = _spacecase(text).lower()

    text = text.replace('appxs', 'Appx\'s')

    text = text.replace('appx', 'Appx')

    text = text.replace('cloud', 'Cloud')
    text = text.replace('docs', 'Docs')
    text = text.replace('enterprise', 'Enterprise')
    text = text.replace('git', 'Git')
    text = text.replace('team', 'Team')

    text = text[0].upper() + text[1:]

    return text


def get_params(link: str):
    pattern = '^(?P<prefix>")?\\[(?P<text>AUTOTITLE)\\]\\((?P<href>[a-z0-9@#\\/-]+)\\)(?P<suffix>(?:[\\.,]+)?")?$'
    match = re.match(pattern, link)
    if match:
        prefix = match.group('prefix') if match.group('prefix') else ''
        suffix = match.group('suffix') if match.group('suffix') else ''
        text = match.group('text')
        href = match.group('href')
        return (prefix, text, href, suffix)

    match = re.match('^(?P<href>[a-z\\/-]+)$', link)
    if match:
        return ('', '', match.group('href'), '')

    return None


def _spacecase(text: str) -> str:
    # https://stackoverflow.com/a/1176023
    # https://github.com/jpvanhal/inflection
    text = re.sub(r"([A-Z]+)([A-Z][a-z])", r'\1_\2', text)
    text = re.sub(r"([a-z\d])([A-Z])", r'\1_\2', text)
    text = text.replace("-", "_")

    text = text.replace('_', ' ')

    return text
