import importlib
import os

ex = importlib.import_module(
    "gabaritos.fase0_ambiente" if os.getenv("GABARITO") else "fase0_ambiente.ex01_ambiente"
)


def test_saudacao():
    assert ex.saudacao("leone") == "Olá, Leone! Bem-vindo ao Python Lab."
    assert ex.saudacao("ANA") == "Olá, Ana! Bem-vindo ao Python Lab."


def test_versao_python_e_312_ou_mais():
    versao = ex.versao_python()
    assert isinstance(versao, tuple) and len(versao) == 2
    assert versao >= (3, 12), f"Você está usando Python {versao}; instale 3.12+ com o uv"


def test_rodando_no_venv():
    assert ex.em_ambiente_virtual() is True, "Rode com `uv run pytest` para usar o .venv"
