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
import configparser
from pathlib import Path
from types import SimpleNamespace
from typing import List, Optional

from toolboks.modifiers import filter_abs_path
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
    return getenv(
        'XDG_CACHE_HOME',
        fallback=f"{user_home() / '.cache'}",
        mod=filter_abs_path
    )


def config_dirs() -> List[str]:
    """
    Return value of $XDG_CONFIG_DIRS or default value ['/etc/xdg/']
    """
    return getenv(
        'XDG_CONFIG_DIRS',
        fallback='/etc/xdg',
        mod=filter_abs_path
    ).split(':')


def config_home() -> str:
    """
    Return value of $XDG_CONFIG_HOME or default value '$HOME/.config'
    """
    return getenv(
        'XDG_CONFIG_HOME',
        fallback=f"{user_home() / '.config'}",
        mod=filter_abs_path
    )


def data_dirs() -> List[str]:
    """
    Return value of $XDG_DATA_DIRS or default value ['/usr/local/share','/usr/share']
    """
    return getenv(
        'XDG_DATA_DIRS',
        fallback='/usr/local/share:/usr/share',
        mod=filter_abs_path
    ).split(':')


def data_home() -> str:
    """
    Return value of $XDG_DATA_HOME or default value '$HOME/.local/share'
    """
    return getenv(
        'XDG_DATA_HOME',
        fallback=f"{user_home() / '.local' / 'share'}",
        mod=filter_abs_path
    )


def runtime_dir() -> Optional[str]:
    """
    Return value of $XDG_RUNTIME_DIR. No default value specified.
    Application utilising this library should handle absence of value.
    """
    return getenv(
        'XDG_RUNTIME_DIR',
        mod=filter_abs_path
    )


def state_home() -> str:
    """
    Return value of $XDG_STATE_HOME or default value '$HOME/.local/state'
    """
    return getenv(
        'XDG_STATE_HOME',
        fallback=f"{user_home() / '.local' / 'state'}",
        mod=filter_abs_path
    )


def user_dirs() -> Optional[SimpleNamespace]:
    """
    Read $XDG_CONFIG_HOME/user-dirs.dirs if it exists.
    Return SimpleNamespace object with all directories specified.
    $HOME will be expanded.
    """
    xdg_dirs = SimpleNamespace()
    user_dirs_path = config_home() + '/user-dirs.dirs'

    if Path(user_dirs_path).is_file():
        config = configparser.ConfigParser()
        contents = '[user_dirs]\n'

        with open(user_dirs_path, 'r', encoding='utf-8') as user_dirs_file:
            contents += user_dirs_file.read()

        config.read_string(contents)

        section = config['user_dirs']

        for key in section:
            value = section[key]

            key = key.replace('xdg_', '')
            value = value.replace('$HOME', str(user_home()))
            value = value.replace('"', '')

            setattr(xdg_dirs, key, value)

        return xdg_dirs

    return None


def user_home() -> Path:
    """
    Return path to home directory for current user
    """
    return Path.home()
