"""Solution — Phase 0 · Exercise 1. Só abra depois de tentar!"""

import sys


def greeting(name: str) -> str:
    return f"Hello, {name.capitalize()}! Welcome to Python Security Lab."


def python_version() -> tuple[int, int]:
    return (sys.version_info.major, sys.version_info.minor)


def in_virtualenv() -> bool:
    return sys.prefix != sys.base_prefix
