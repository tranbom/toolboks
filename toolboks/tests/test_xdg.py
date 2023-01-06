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
from pathlib import Path

import pytest  # noqa: F401 pylint: disable=unused-import

from toolboks.xdg import (
    base_dirs,
    cache_home,
    config_dirs,
    config_home,
    data_dirs,
    data_home,
    runtime_dir,
    state_home,
    user_dirs,
    user_home
)


def test_base_dirs_env(monkeypatch):
    """Test the xdg.base_dirs function with environment variables set"""
    fake_path = str(Path.cwd() / 'toolboks/tests/testdata/fakepath')

    monkeypatch.setenv('XDG_CACHE_HOME', fake_path)
    monkeypatch.setenv('XDG_CONFIG_DIRS', fake_path)
    monkeypatch.setenv('XDG_CONFIG_HOME', fake_path)
    monkeypatch.setenv('XDG_DATA_DIRS', fake_path)
    monkeypatch.setenv('XDG_DATA_HOME', fake_path)
    monkeypatch.setenv('XDG_RUNTIME_DIR', fake_path)
    monkeypatch.setenv('XDG_STATE_HOME', fake_path)

    base_dirs_nsp = base_dirs()

    assert base_dirs_nsp.cache_home == fake_path
    assert base_dirs_nsp.config_dirs == [fake_path]
    assert base_dirs_nsp.config_home == fake_path
    assert base_dirs_nsp.data_dirs == [fake_path]
    assert base_dirs_nsp.data_home == fake_path
    assert base_dirs_nsp.runtime_dir == fake_path
    assert base_dirs_nsp.state_home == fake_path


def test_base_dirs_default(monkeypatch):
    """Test the xdg.base_dirs function with environment variables unset"""
    monkeypatch.delenv('XDG_CACHE_HOME', raising=False)
    monkeypatch.delenv('XDG_CONFIG_DIRS', raising=False)
    monkeypatch.delenv('XDG_CONFIG_HOME', raising=False)
    monkeypatch.delenv('XDG_DATA_DIRS', raising=False)
    monkeypatch.delenv('XDG_DATA_HOME', raising=False)
    monkeypatch.delenv('XDG_RUNTIME_DIR', raising=False)
    monkeypatch.delenv('XDG_STATE_HOME', raising=False)

    base_dirs_nsp = base_dirs()

    assert base_dirs_nsp.cache_home == str(Path.home() / '.cache')
    assert base_dirs_nsp.config_dirs == ['/etc/xdg']
    assert base_dirs_nsp.config_home == str(Path.home() / '.config')
    assert base_dirs_nsp.data_dirs == ['/usr/local/share', '/usr/share']
    assert base_dirs_nsp.data_home == str(Path.home() / '.local/share')
    assert base_dirs_nsp.runtime_dir is None
    assert base_dirs_nsp.state_home == str(Path.home() / '.local/state')


def test_cache_home_env(monkeypatch):
    """Test the xdg.cache_home function with the env var XDG_CACHE_HOME set"""
    fake_path = str(Path.cwd() / 'toolboks/tests/testdata/fakepath')
    monkeypatch.setenv('XDG_CACHE_HOME', fake_path)

    assert cache_home() == fake_path


def test_cache_home_default(monkeypatch):
    """Test the xdg.cache_home function with the env var XDG_CACHE_HOME unset"""
    monkeypatch.delenv('XDG_CACHE_HOME', raising=False)

    expected_cache_home = str(Path.home() / '.cache')

    assert cache_home() == expected_cache_home


def test_config_dirs_env(monkeypatch):
    """Test the xdg.config_dirs function with the env var XDG_CONFIG_DIRS set"""
    fake_path = str(Path.cwd() / 'toolboks/tests/testdata/fakepath')
    monkeypatch.setenv('XDG_CONFIG_DIRS', fake_path)

    assert config_dirs() == [fake_path]


def test_config_dirs_default(monkeypatch):
    """Test the xdg.config_dirs function with the env var XDG_CONFIG_DIRS unset"""
    monkeypatch.delenv('XDG_CONFIG_DIRS', raising=False)

    assert config_dirs() == ['/etc/xdg']


def test_config_home_env(monkeypatch):
    """Test the xdg.config_home function with the env var XDG_CONFIG_HOME set"""
    fake_path = str(Path.cwd() / 'toolboks/tests/testdata/fakepath')
    monkeypatch.setenv('XDG_CONFIG_HOME', fake_path)

    assert config_home() == fake_path


def test_config_home_default(monkeypatch):
    """Test the xdg.config_home function with the env var XDG_CONFIG_HOME unset"""
    monkeypatch.delenv('XDG_CONFIG_HOME', raising=False)

    expected_config_home = str(Path.home() / '.config')

    assert config_home() == expected_config_home


def test_data_dirs_env(monkeypatch):
    """Test the xdg.data_dirs function with the env var XDG_DATA_DIRS set"""
    fake_path = str(Path.cwd() / 'toolboks/tests/testdata/fakepath')
    monkeypatch.setenv('XDG_DATA_DIRS', fake_path)

    assert data_dirs() == [fake_path]


def test_data_dirs_default(monkeypatch):
    """Test the xdg.data_dirs function with the env var XDG_DATA_DIRS unset"""
    monkeypatch.delenv('XDG_DATA_DIRS', raising=False)

    expected_data_dirs = ['/usr/local/share', '/usr/share']

    assert data_dirs() == expected_data_dirs


def test_data_home_env(monkeypatch):
    """Test the xdg.data_home function with the env var XDG_DATA_HOME set"""
    fake_path = str(Path.cwd() / 'toolboks/tests/testdata/fakepath')
    monkeypatch.setenv('XDG_DATA_HOME', fake_path)

    assert data_home() == fake_path


def test_data_home_default(monkeypatch):
    """Test the xdg.data_home function with the env var XDG_DATA_HOME unset"""
    monkeypatch.delenv('XDG_DATA_HOME', raising=False)

    expected_data_home = str(Path.home() / '.local/share')

    assert data_home() == expected_data_home


def test_runtime_dir_env(monkeypatch):
    """Test the xdg.runtime_dir function with the env var XDG_RUNTIME_DIR set"""
    fake_path = str(Path.cwd() / 'toolboks/tests/testdata/fakepath')
    monkeypatch.setenv('XDG_RUNTIME_DIR', fake_path)

    assert runtime_dir() == fake_path


def test_runtime_dir_default(monkeypatch):
    """Test the xdg.runtime_dir function with the env var XDG_RUNTIME_DIR unset"""
    monkeypatch.delenv('XDG_RUNTIME_DIR', raising=False)

    assert runtime_dir() is None


def test_state_home_env(monkeypatch):
    """Test the xdg.state_home function with the env var XDG_STATE_HOME set"""
    fake_path = str(Path.cwd() / 'toolboks/tests/testdata/fakepath')
    monkeypatch.setenv('XDG_STATE_HOME', fake_path)

    assert state_home() == fake_path


def test_state_home_default(monkeypatch):
    """Test the xdg.state_home function with the env var XDG_STATE_HOME unset"""
    monkeypatch.delenv('XDG_STATE_HOME', raising=False)

    expected_state_home = str(Path.home() / '.local/state')

    assert state_home() == expected_state_home


def test_user_dirs(monkeypatch):
    """Test the xdg.user_dirs function with a bundled test file"""
    # monkeypatcha en file path ?
    fake_config_path = str(Path.cwd() / 'toolboks/tests/testdata')
    monkeypatch.setenv('XDG_CONFIG_HOME', fake_config_path)

    user_dirs_nsp = user_dirs()

    assert user_dirs_nsp.desktop_dir == str(Path.home() / 'Desktop')
    assert user_dirs_nsp.download_dir == str(Path.home() / 'Downloads')
    assert user_dirs_nsp.templates_dir == str(Path.home() / 'Templates')
    assert user_dirs_nsp.publicshare_dir == str(Path.home() / 'Public')
    assert user_dirs_nsp.documents_dir == str(Path.home() / 'Documents')
    assert user_dirs_nsp.music_dir == str(Path.home() / 'Music')
    assert user_dirs_nsp.pictures_dir == str(Path.home() / 'Pictures')
    assert user_dirs_nsp.videos_dir == str(Path.home() / 'Videos')


def test_user_dirs_no_file(monkeypatch):
    """Test the xdg.user_dirs function with a non-existing user-dirs.dirs"""
    fake_config_path = str(
        Path.cwd() / '/toolboks/tests/testdata/nonexisting-directory/'
    )
    monkeypatch.setenv('XDG_CONFIG_HOME', fake_config_path)

    assert user_dirs() is None


def test_user_home():
    """Test the xdg.user_home function"""
    assert user_home() == Path.home()
