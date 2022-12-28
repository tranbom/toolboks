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
from typing import List


def expand(nested_list: List, depth: int = -1) -> List:
    """
    Expand lists in `nested_list` and return a flat list without sublists.
    All nested sublists will be expanded when no `depth` is given.

    When `depth` is set, expand will only recurse n times (n=depth).
    Any remaining nested lists at a "higher" depth will remain as nested lists.

    Example:
    > list_of_lists = [1,2,3,4,[5,6,[7,8]]]
    > expand(list_of_lists)
    [1, 2, 3, 4, 5, 6, 7, 8]

    > expand(list_of_lists, depth=1)
    [1, 2, 3, 4, 5, 6, [7, 8]]
    """
    if depth < -1:
        raise ValueError("Invalid depth")

    expanded_list = []

    for entry in nested_list:
        if isinstance(entry, list):
            if depth == -1:
                expanded_list.extend(expand(entry))
            elif depth > 0:
                expanded_list.extend(expand(entry, depth-1))
            else:
                expanded_list.append(entry)
        else:
            expanded_list.append(entry)

    return expanded_list


def flatten(*args) -> List:
    """
    Flatten any number of lists, nested lists, or objects, into one list.
    """
    flattened_list = []

    for arg in args:
        if isinstance(arg, list):
            flattened_list.extend(expand(arg))
        else:
            flattened_list.append(arg)

    return flattened_list
