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

from toolboks.config import read_config


def test_read_config():
    """Test the function config.read_config"""
    config = read_config('toolboks/tests/testdata/testconfig.ini')

    assert config.section_1.a_number == '115'
    assert config.section_1.environment == 'testing'
    assert config.section_1.test == 'True'

    assert config.toolboks.environment == 'dev'
    assert config.toolboks.timeout == '5'


def test_read_config_as_dict():
    """Test the function config.read_config with as_dict=True"""
    config = read_config('toolboks/tests/testdata/testconfig.ini', as_dict=True)

    assert config['section_1']['a_number'] == '115'
    assert config['section_1']['environment'] == 'testing'
    assert config['section_1']['test'] == 'True'

    assert config['toolboks']['environment'] == 'dev'
    assert config['toolboks']['timeout'] == '5'


def test_read_config_invalid_filename():
    """Test the function config.read_config with an invalid filename"""
    with pytest.raises(FileNotFoundError):
        read_config('toolboks/tests/testdata/invalid_filename_config.ini')
