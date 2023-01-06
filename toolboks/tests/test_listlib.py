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
import pytest

from toolboks.listlib import expand, flatten

# Module specific pylint instructions
# pylint: disable=redefined-outer-name


@pytest.fixture
def nested_lists():
    """Fixture for a list with many nested sublists"""
    nested_lists = [
        [10, 14, 15, [110, 123, 145, [245, 230, 210, [313, 333, 343],], 150],],
        ['Some text', ['More text', 'Even more text']],
        [11.33, 22.44, [33.11, [55.5, [55.5, [44.42, [123.321]]]]]],
    ]

    return nested_lists


def test_expand(nested_lists):
    """Test the listlib.expand function without parameters"""
    assert expand(nested_lists[0]) == \
        [10, 14, 15, 110, 123, 145, 245, 230, 210, 313, 333, 343, 150]

    assert expand(nested_lists) == [
        10, 14, 15, 110, 123, 145, 245, 230, 210, 313, 333, 343, 150,
        'Some text', 'More text', 'Even more text',
        11.33, 22.44, 33.11, 55.5, 55.5, 44.42, 123.321,
    ]


def test_expand_with_depth(nested_lists):
    """Test the listlib.expand function with depth parameter"""
    assert expand(nested_lists[0], depth=1) == \
        [10, 14, 15, 110, 123, 145, [245, 230, 210, [313, 333, 343],], 150]
    assert expand(nested_lists[0], depth=2) == \
        [10, 14, 15, 110, 123, 145, 245, 230, 210, [313, 333, 343], 150]
    assert expand(nested_lists[0], depth=3) == \
        [10, 14, 15, 110, 123, 145, 245, 230, 210, 313, 333, 343, 150]
    assert expand(nested_lists[0], depth=0) == \
        [10, 14, 15, [110, 123, 145, [245, 230, 210, [313, 333, 343],], 150],]


def test_expand_invalid_depth(nested_lists):
    """Test exception for invalid depth in the listlib.expand function"""
    with pytest.raises(ValueError):
        expand(nested_lists, depth=-5)


def test_flatten(nested_lists):
    """Test the listlib.flatten function"""
    assert flatten(11, 22, 33, 44, 55) == [11, 22, 33, 44, 55]

    assert flatten(nested_lists, nested_lists[1], 412, 500, 600) == [
        10, 14, 15, 110, 123, 145, 245, 230, 210, 313, 333, 343, 150,
        'Some text', 'More text', 'Even more text',
        11.33, 22.44, 33.11, 55.5, 55.5, 44.42, 123.321,
        'Some text', 'More text', 'Even more text',
        412, 500, 600,
    ]
