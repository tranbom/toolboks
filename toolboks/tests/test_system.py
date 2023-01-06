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
import sys
import platform

from toolboks.system import context, getenv


def test_context():
    """Test system.context function"""
    system_context = context()

    assert system_context.cpu_count == os.cpu_count()
    assert system_context.hostname == platform.node()
    assert system_context.machine == platform.machine()
    assert system_context.os == sys.platform
    assert system_context.platform == platform.platform()
    assert system_context.python_binary == sys.executable
    assert system_context.python_binary_real == os.path.realpath(sys.executable)
    assert system_context.python_implementation == platform.python_implementation()
    assert system_context.python_version == platform.python_version()
    assert system_context.system == platform.system()

    assert system_context.shell == os.getenv('SHELL')
    assert system_context.user == os.getenv('USER')
    assert system_context.virtual_environment == os.getenv('VIRTUAL_ENV')


def test_context_missing_env_vars(monkeypatch):
    """Test system.context with missing environment variables"""
    monkeypatch.delenv('SHELL', raising=False)
    monkeypatch.delenv('USER', raising=False)
    monkeypatch.delenv('VIRTUAL_ENV', raising=False)

    system_context = context()

    assert system_context.shell == os.getenv('SHELL')
    assert system_context.user == os.getenv('USER')
    assert system_context.virtual_environment == os.getenv('VIRTUAL_ENV')


def test_getenv(monkeypatch):
    """Test system.getenv function with an existing environment variable"""
    monkeypatch.setenv('TB_TEST1', '/home/toolboks/test')

    # environment variable with blank value
    monkeypatch.setenv('TB_TEST2', '')

    assert getenv('TB_TEST1') == '/home/toolboks/test'
    assert getenv('TB_TEST2') == ''


def test_getenv_with_fallback(monkeypatch):
    """Test system.getenv function with fallback value"""
    monkeypatch.setenv('TB_TEST1', '/home/toolboks/test')

    # environment variable with blank value
    monkeypatch.setenv('TB_TEST2', '')

    assert getenv('TB_TEST1', fallback='/home/toolboks/test2') == '/home/toolboks/test'
    assert getenv('TB_TEST2', fallback='/home/toolboks/test2') == '/home/toolboks/test2'
    assert getenv('TB_TEST2', fallback='/home/toolboks/test2') != \
        os.getenv('TB_TEST2', default='/home/toolboks/test2')


def test_getenv_no_env_vars(monkeypatch):
    """Test system.getenv function with a non-existing environment variable"""
    monkeypatch.delenv('TB_TEST1', raising=False)

    assert getenv('TB_TEST1') is None
