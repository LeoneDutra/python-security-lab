import importlib
import json
import os

import pytest

d = importlib.import_module(
    "gabaritos.diagnostico" if os.getenv("GABARITO") else "diagnostico.diagnostico"
)


# Bloco A ------------------------------------------------------------------

@pytest.mark.parametrize(
    ("porta", "esperado"),
    [(0, "well-known"), (22, "well-known"), (1023, "well-known"), (1024, "registrada"),
     (3389, "registrada"), (49151, "registrada"), (49152, "dinamica"), (65535, "dinamica")],
)
def test_q01_classificar_porta(porta, esperado):
    assert d.classificar_porta(porta) == esperado


@pytest.mark.parametrize("porta", [-1, 65536, 100000])
def test_q01_porta_invalida(porta):
    with pytest.raises(ValueError):
        d.classificar_porta(porta)


def test_q02_mascarar_email():
    assert d.mascarar_email("leone@exemplo.com") == "l****@exemplo.com"
    assert d.mascarar_email("a@b.com") == "a@b.com"
    assert d.mascarar_email("soc.team@empresa.com.br") == "s*******@empresa.com.br"


def test_q03_contar_falhas():
    linhas = [
        "Nov 24 10:00:01 srv sshd[1]: Failed password for root from 1.2.3.4",
        "Nov 24 10:00:02 srv sshd[1]: Accepted password for bob from 5.6.7.8",
        "Nov 24 10:00:03 srv sshd[1]: Failed password for invalid user test from 1.2.3.4",
    ]
    assert d.contar_falhas(linhas) == 2
    assert d.contar_falhas([]) == 0


@pytest.mark.parametrize(
    ("senha", "esperado"),
    [("Fiap@PosTech2027", True), ("curta@1A", False), ("semsimbolo2027AB", False),
     ("SEMMINUSCULA@2027", False), ("semmaiuscula@2027", False), ("SemDigito@@@@abc", False)],
)
def test_q04_senha_forte(senha, esperado):
    assert d.senha_forte(senha) is esperado


# Bloco B ------------------------------------------------------------------

def test_q05_ips_unicos():
    assert d.ips_unicos(["10.0.0.2", "10.0.0.1", "10.0.0.2"]) == ["10.0.0.1", "10.0.0.2"]
    assert d.ips_unicos([]) == []


def test_q06_top_ips():
    ips = ["1.1.1.1", "2.2.2.2", "1.1.1.1", "3.3.3.3", "2.2.2.2", "9.9.9.9", "9.9.9.9", "9.9.9.9"]
    assert d.top_ips(ips, 1) == [("9.9.9.9", 3)]
    assert d.top_ips(ips, 3) == [("9.9.9.9", 3), ("1.1.1.1", 2), ("2.2.2.2", 2)]


def test_q07_portas_do_servico():
    mapa = {8080: "HTTP", 80: "http", 443: "https", 22: "ssh"}
    assert d.portas_do_servico(mapa, "http") == [80, 8080]
    assert d.portas_do_servico(mapa, "SSH") == [22]
    assert d.portas_do_servico(mapa, "ftp") == []


def test_q08_media_tamanho():
    assert d.media_tamanho(["abc", "abcde"]) == 4.0
    assert d.media_tamanho([]) == 0.0


def test_q09_agrupar_por_usuario():
    eventos = [
        {"usuario": "ana", "evento": "login"},
        {"usuario": "bob", "evento": "login"},
        {"usuario": "ana", "evento": "logout"},
    ]
    assert d.agrupar_por_usuario(eventos) == {"ana": ["login", "logout"], "bob": ["login"]}
    assert d.agrupar_por_usuario([]) == {}


# Bloco C ------------------------------------------------------------------

def test_q10_parse_linha_log():
    linha = "2026-11-24T10:00:00 192.168.0.10 LOGIN_FAIL user=admin"
    assert d.parse_linha_log(linha) == {
        "timestamp": "2026-11-24T10:00:00",
        "ip": "192.168.0.10",
        "evento": "LOGIN_FAIL",
        "usuario": "admin",
    }


def test_q11_dominios_normalizados():
    urls = [
        "https://WWW.Exemplo.com/login",
        "http://exemplo.com:8080/x",
        "https://phishing-banco.xyz/?a=1",
        "https://sub.dominio.org",
    ]
    assert d.dominios_normalizados(urls) == {"exemplo.com", "phishing-banco.xyz", "sub.dominio.org"}


def test_q12_extrair_ips():
    texto = "Conexão de 10.0.0.5 para 8.8.8.8; depois 10.0.0.5 de novo. Versão 1.2 não é IP."
    assert d.extrair_ips(texto) == ["10.0.0.5", "8.8.8.8"]
    assert d.extrair_ips("nenhum ip aqui") == []


def test_q13_sha256_texto():
    assert d.sha256_texto("abc") == (
        "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    )
    assert len(d.sha256_texto("")) == 64


def test_q14_alertas_graves(tmp_path):
    arquivo = tmp_path / "alertas.json"
    arquivo.write_text(json.dumps([
        {"regra": "Port scan", "severidade": 5},
        {"regra": "Brute force SSH", "severidade": 9},
        {"regra": "Malware detectado", "severidade": 7},
    ]), encoding="utf-8")
    assert d.alertas_graves(str(arquivo)) == ["Brute force SSH", "Malware detectado"]


def test_q14_arquivo_inexistente(tmp_path):
    assert d.alertas_graves(str(tmp_path / "nao_existe.json")) == []


# Bloco D ------------------------------------------------------------------

def test_q15_alerta():
    a = d.Alerta("Brute force SSH", 9)
    assert a.regra == "Brute force SSH"
    assert a.severidade == 9
    assert a.eh_critico() is True
    assert str(a) == "[SEV 9] Brute force SSH"
    assert d.Alerta("Port scan", 4).eh_critico() is False


@pytest.mark.parametrize("sev", [0, 11])
def test_q15_alerta_severidade_invalida(sev):
    with pytest.raises(ValueError):
        d.Alerta("x", sev)
