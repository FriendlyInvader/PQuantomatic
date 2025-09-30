"""Tests for PQuantomatic library."""

import pytest
from pquantomatic import __version__
from pquantomatic.example import hello, add


def test_version():
    """Test that version is defined."""
    assert __version__ == "0.1.0"


def test_hello():
    """Test hello function."""
    assert hello() == "Hello from PQuantomatic!"


def test_add():
    """Test add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
