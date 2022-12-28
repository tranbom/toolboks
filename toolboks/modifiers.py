"""
toolboks - Lightweight library & utility tools

Copyright (C) 2022 Mikael Tranbom

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import os


def filter_abs_path(path_str: str) -> str:
    """
    Return absolute paths present in string `path`. Any relative paths are removed.
    `path` should use the Linux/Unix format for paths: 'path1' or 'path1:path2:path3'

    If `path` only contains relative paths a blank str is returned.
    """
    paths = path_str.split(':')

    for path in paths:
        if not os.path.isabs(path):
            paths.remove(path)

    return ':'.join(paths)
