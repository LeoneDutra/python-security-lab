"""Phase 0 · Exercise 1 — Is your environment set up correctly?

Objetivo: escrever as primeiras funções e ver os testes ficarem verdes.

Rode:  uv run pytest phase0_setup -v
"""

import sys


def greeting(name: str) -> str:
    """Retorna uma saudação com o nome capitalizado.

    >>> greeting("leone")
    'Hello, Leone! Welcome to Python Security Lab.'

    Dica: procure o método de string que deixa só a primeira letra maiúscula.
    """
    raise NotImplementedError


def python_version() -> tuple[int, int]:
    """Retorna (major, minor) da versão do Python em execução, ex.: (3, 12).

    Dica: o módulo `sys` tem um atributo `version_info`.
    """
    raise NotImplementedError


def in_virtualenv() -> bool:
    """Retorna True se o código está rodando dentro de um ambiente virtual (.venv).

    Dica: dentro de um venv, `sys.prefix` é diferente de `sys.base_prefix`.
    """
    raise NotImplementedError


if __name__ == "__main__":
    # Rode também diretamente:  uv run python phase0_setup/ex01_setup.py
    print(greeting("your name"))
    print("Python", python_version(), "| venv:", in_virtualenv(), "|", sys.executable)
