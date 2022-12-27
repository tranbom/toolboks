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
from types import SimpleNamespace
from typing import List, Optional

from toolboks.system import getenv

# Functions based on XDG Base Directory Specification:
# https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html


def base_dirs() -> SimpleNamespace:
    """
    Return SimpleNamespace object with base dirs according to the XDG base specification
    """
    xdg_dirs = SimpleNamespace()

    xdg_dirs.cache_home = cache_home()
    xdg_dirs.config_dirs = config_dirs()
    xdg_dirs.config_home = config_home()
    xdg_dirs.data_dirs = data_dirs()
    xdg_dirs.data_home = data_home()
    xdg_dirs.runtime_dir = runtime_dir()
    xdg_dirs.state_home = state_home()

    return xdg_dirs


def cache_home() -> str:
    """
    Return value of $XDG_CACHE_HOME or default value '$HOME/.cache'
    """
    return getenv('XDG_CACHE_HOME', f"{user_home() / '.cache'}")


def config_dirs() -> List[str]:
    """
    Return value of $XDG_CONFIG_DIRS or default value ['/etc/xdg/']
    """
    return getenv('XDG_CONFIG_DIRS', '/etc/xdg').split(':')


def config_home() -> str:
    """
    Return value of $XDG_CONFIG_HOME or default value '$HOME/.config'
    """
    return getenv('XDG_CONFIG_HOME', f"{user_home() / '.config'}")


def data_dirs() -> List[str]:
    """
    Return value of $XDG_DATA_DIRS or default value ['/usr/local/share','/usr/share']
    """
    return getenv('XDG_DATA_DIRS', '/usr/local/share:/usr/share').split(':')


def data_home() -> str:
    """
    Return value of $XDG_DATA_HOME or default value '$HOME/.local/share'
    """
    return getenv('XDG_DATA_HOME', f"{user_home() / '.local' / 'share'}")


def runtime_dir() -> Optional[str]:
    """
    Return value of $XDG_RUNTIME_DIR. No default value specified.
    Application utilising this library should handle absence of value.
    """
    return getenv('XDG_RUNTIME_DIR')


def state_home() -> str:
    """
    Return value of $XDG_STATE_HOME or default value '$HOME/.local/state'
    """
    return getenv('XDG_STATE_HOME', f"{user_home() / '.local' / 'state'}")


def user_home() -> Path:
    """
    Return path to home directory for current user
    """
    return Path.home()
