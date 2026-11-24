"""Gabarito — Fase 0 · Exercício 1. Só abra depois de tentar!"""

import sys


def saudacao(nome: str) -> str:
    return f"Olá, {nome.capitalize()}! Bem-vindo ao Python Lab."


def versao_python() -> tuple[int, int]:
    return (sys.version_info.major, sys.version_info.minor)


def em_ambiente_virtual() -> bool:
    return sys.prefix != sys.base_prefix
