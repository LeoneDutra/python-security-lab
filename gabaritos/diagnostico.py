"""Gabarito do diagnóstico. Só abra depois de tentar!

Repare que há mais de uma solução correta para quase todas as questões.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from urllib.parse import urlparse


def classificar_porta(porta: int) -> str:
    if 0 <= porta <= 1023:
        return "well-known"
    if 1024 <= porta <= 49151:
        return "registrada"
    if 49152 <= porta <= 65535:
        return "dinamica"
    raise ValueError(f"Porta inválida: {porta}")


def mascarar_email(email: str) -> str:
    usuario, dominio = email.split("@", 1)
    return usuario[0] + "*" * (len(usuario) - 1) + "@" + dominio


def contar_falhas(linhas: list[str]) -> int:
    return sum(1 for linha in linhas if "Failed password" in linha)


def senha_forte(senha: str) -> bool:
    return (
        len(senha) >= 12
        and any(c.isupper() for c in senha)
        and any(c.islower() for c in senha)
        and any(c.isdigit() for c in senha)
        and any(not c.isalnum() for c in senha)
    )


def ips_unicos(ips: list[str]) -> list[str]:
    return sorted(set(ips))


def top_ips(ips: list[str], n: int) -> list[tuple[str, int]]:
    contagem = Counter(ips)
    return sorted(contagem.items(), key=lambda item: (-item[1], item[0]))[:n]


def portas_do_servico(mapa: dict[int, str], servico: str) -> list[int]:
    alvo = servico.lower()
    return sorted(porta for porta, nome in mapa.items() if nome.lower() == alvo)


def media_tamanho(senhas: list[str]) -> float:
    if not senhas:
        return 0.0
    return sum(len(s) for s in senhas) / len(senhas)


def agrupar_por_usuario(eventos: list[dict]) -> dict[str, list[str]]:
    grupos: defaultdict[str, list[str]] = defaultdict(list)
    for e in eventos:
        grupos[e["usuario"]].append(e["evento"])
    return dict(grupos)


def parse_linha_log(linha: str) -> dict[str, str]:
    timestamp, ip, evento, user = linha.split()
    return {
        "timestamp": timestamp,
        "ip": ip,
        "evento": evento,
        "usuario": user.removeprefix("user="),
    }


def dominios_normalizados(urls: list[str]) -> set[str]:
    resultado = set()
    for url in urls:
        host = (urlparse(url).hostname or "").lower()  # hostname já remove a porta
        resultado.add(host.removeprefix("www."))
    return resultado


IPV4 = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")


def extrair_ips(texto: str) -> list[str]:
    # dict.fromkeys remove duplicados mantendo a ordem
    return list(dict.fromkeys(IPV4.findall(texto)))


def sha256_texto(texto: str) -> str:
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def alertas_graves(caminho: str) -> list[str]:
    try:
        with open(caminho, encoding="utf-8") as f:
            alertas = json.load(f)
    except FileNotFoundError:
        return []
    return [a["regra"] for a in alertas if a["severidade"] >= 7]


class Alerta:
    def __init__(self, regra: str, severidade: int) -> None:
        if not 1 <= severidade <= 10:
            raise ValueError("severidade deve estar entre 1 e 10")
        self.regra = regra
        self.severidade = severidade

    def eh_critico(self) -> bool:
        return self.severidade >= 9

    def __str__(self) -> str:
        return f"[SEV {self.severidade}] {self.regra}"
