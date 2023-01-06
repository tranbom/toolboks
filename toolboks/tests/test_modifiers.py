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
from toolboks.modifiers import filter_abs_path


def test_filter_abs_path():
    """Test the modifiers.filter_abs_path function"""

    paths_1 = '/home/toolboks/test:/etc:/usr/bin'
    paths_2 = '.toolboks/test:/home/toolboks/test:/etc:/usr/bin'
    paths_3 = '/home/toolboks/test:/etc:/usr/bin:toolboks/test'

    assert filter_abs_path(paths_1) == paths_1
    assert filter_abs_path(paths_2) == paths_1
    assert filter_abs_path(paths_3) == paths_1
