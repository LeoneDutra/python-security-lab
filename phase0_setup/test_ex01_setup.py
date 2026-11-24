import importlib
import os

ex = importlib.import_module(
    "solutions.phase0_setup" if os.getenv("SOLUTIONS") else "phase0_setup.ex01_setup"
)


def test_greeting():
    assert ex.greeting("leone") == "Hello, Leone! Welcome to Python Security Lab."
    assert ex.greeting("ANA") == "Hello, Ana! Welcome to Python Security Lab."


def test_python_version_is_312_or_newer():
    version = ex.python_version()
    assert isinstance(version, tuple) and len(version) == 2
    assert version >= (3, 12), f"You are on Python {version}; install 3.12+ with uv"


def test_running_inside_virtualenv():
    assert ex.in_virtualenv() is True, "Run with `uv run pytest` so the .venv is used"
