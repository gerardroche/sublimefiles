import os
import re
import subprocess
import webbrowser

from sublime import status_message
import sublime_plugin


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
        return 'https://github.com/' + match[0].replace('#', '/issues/')

    match = re.findall('#[0-9]+', line)
    if match:
        # TODO remove hardcoded package name.
        return 'https://github.com/' + match[0].replace('#', 'NeoVintageous/NeoVintageous/issues/')


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


class GitOpenCommand(sublime_plugin.TextCommand):

    def run(self, edit, event=None):
        url = _extract_github_url(self.view)
        if url:
            webbrowser.open_new_tab(url)
        else:
            file_name = self.view.file_name()
            if not file_name:
                raise ValueError('expected file name')

            cwd = os.path.dirname(self.view.file_name())
            if not os.path.isdir(cwd):
                raise ValueError('cwd is not a valid directory')

            subprocess.Popen(
                ["/usr/bin/env", "bash", "-c", "git-open"],
                cwd=cwd,
                shell=False
            )


class GitCommand(sublime_plugin.WindowCommand):

    def run(self, action):
        if action == 'open_modified':
            working_dir = _find_working_dir(self.window)
            print('Git: working directory is', working_dir)
            if not working_dir:
                return status_message('Git: working directory not found')

            output = subprocess.check_output(
                ["/usr/bin/env", "bash", "-c", "git status --short"],
                cwd=working_dir,
                shell=False
            ).decode('utf8')

            matches = re.findall('\\sM\\s(.+)\n', output)
            print('Git: opening {} modified files...'.format(len(matches)))
            for match in matches:
                match = match.strip('"')
                abs_path = os.path.join(working_dir, match)
                if not os.path.isdir(abs_path):
                    print('Git: opening', match, '...')
                    self.window.open_file(abs_path)


def _find_working_dir(window):
    if not window:
        return None

    folders = window.folders()
    if not folders:
        return None

    view = window.active_view()
    file_name = view.file_name() if view else None

    if not file_name and len(folders) == 1:
        return folders[0]

    if not file_name:
        return

    ancestor_folders = []
    common_prefix = os.path.commonprefix(folders)
    parent = os.path.dirname(file_name)
    while parent not in ancestor_folders and parent.startswith(common_prefix):
        ancestor_folders.append(parent)
        parent = os.path.dirname(parent)

    ancestor_folders.sort(reverse=True)

    for folder in ancestor_folders:
        if os.path.exists(os.path.join(folder, '.git')):
            return folder

    return None
