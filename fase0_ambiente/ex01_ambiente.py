"""Fase 0 · Exercício 1 — Seu ambiente está certo?

Objetivo: escrever as primeiras funções e ver os testes ficarem verdes.

Rode:  uv run pytest fase0_ambiente -v
"""

import sys


def saudacao(nome: str) -> str:
    """Retorna uma saudação com o nome em formato de título.

    >>> saudacao("leone")
    'Olá, Leone! Bem-vindo ao Python Lab.'

    Dica: procure o método de string que deixa a primeira letra maiúscula.
    """
    raise NotImplementedError


def versao_python() -> tuple[int, int]:
    """Retorna (major, minor) da versão do Python em execução, ex.: (3, 12).

    Dica: o módulo `sys` tem um atributo `version_info`.
    """
    raise NotImplementedError


def em_ambiente_virtual() -> bool:
    """Retorna True se o código está rodando dentro de um ambiente virtual (.venv).

    Dica: dentro de um venv, `sys.prefix` é diferente de `sys.base_prefix`.
    """
    raise NotImplementedError


if __name__ == "__main__":
    # Rode também diretamente:  uv run python fase0_ambiente/ex01_ambiente.py
    print(saudacao("seu nome"))
    print("Python", versao_python(), "| venv:", em_ambiente_virtual(), "|", sys.executable)
