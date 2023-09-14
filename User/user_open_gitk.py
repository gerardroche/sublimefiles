# Copyright (C) 2023 Gerard Roche
#
# This file is part of GitOpen.
#
# GitOpen is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GitOpen is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GitOpen.  If not, see <https://www.gnu.org/licenses/>.

import os
import subprocess
import sys

import sublime_plugin


class Gitk(sublime_plugin.WindowCommand):

    def run(self, **kwargs) -> None:
        view = self.window.active_view()
        if not view:
            return

        working_dir = _get_working_dir(view)
        if not working_dir:
            return

        cmd, shell = _build_cmd(view, ['gitk'], kwargs)
        subprocess.Popen(cmd, shell=shell, cwd=working_dir)


def _get_working_dir(view):
    file_name = view.file_name()
    if not file_name:
        return

    cwd = os.path.dirname(view.file_name())
    if not os.path.isdir(cwd):
        return

    return cwd


def _build_cmd(view, cmd: list, options: dict) -> tuple:
    shell_cmd = ' '.join(_build_cmd_options(options, cmd))
    if sys.platform == "win32":
        shell = True
        cmd = shell_cmd
    elif sys.platform == "darwin":
        cmd = ["/usr/bin/env", "bash", "-l", "-c", shell_cmd]
        shell = False
    elif sys.platform == "linux":
        cmd = ["/usr/bin/env", "bash", "-c", shell_cmd]
        shell = False

    return (cmd, shell)


def _build_cmd_options(options: dict, cmd: list) -> list:
    for k, v in options.items():
        if not v:
            continue

        if len(k) == 1:
            cmd.append('-' + k + ('' if v is True else str(v)))
            continue

        cmd.append('--' + k + ('' if v is True else '=' + str(v)))

    return cmd
