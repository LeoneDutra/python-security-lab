"""Teste diagnóstico — calibra a checklist do Notion.

Como fazer (tempo sugerido: 2 a 3 horas, pode dividir em dias):
- Resolva na ordem. Vale consultar a documentação, mas anote quando consultou.
- NÃO abra o gabarito antes de terminar ou de desistir de uma questão.
- Rode:  uv run pytest diagnostico -v
- Ao final, preencha a tabela de autoavaliação em diagnostico/README.md
  e atualize o "Nível" dos tópicos no Notion.

Cada função tem uma docstring com o que fazer e exemplos.
Troque `raise NotImplementedError` pela sua solução.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Bloco A — Fundamentos (tipos, condicionais, strings, laços)
# ---------------------------------------------------------------------------

def classificar_porta(porta: int) -> str:
    """Q1. Classifica uma porta TCP/UDP.

    - 0 a 1023       -> "well-known"
    - 1024 a 49151   -> "registrada"
    - 49152 a 65535  -> "dinamica"
    - fora disso     -> lança ValueError

    >>> classificar_porta(443)
    'well-known'
    """
    raise NotImplementedError


def mascarar_email(email: str) -> str:
    """Q2. Esconde o usuário de um e-mail, mantendo só a 1ª letra.

    O número de asteriscos é igual ao número de letras escondidas.

    >>> mascarar_email("leone@exemplo.com")
    'l****@exemplo.com'
    """
    raise NotImplementedError


def contar_falhas(linhas: list[str]) -> int:
    """Q3. Conta quantas linhas de log contêm "Failed password".

    >>> contar_falhas(["Failed password for root", "Accepted password for bob"])
    1
    """
    raise NotImplementedError


def senha_forte(senha: str) -> bool:
    """Q4. Retorna True se a senha tem TODOS os critérios:

    - 12 caracteres ou mais
    - pelo menos 1 letra maiúscula, 1 minúscula e 1 dígito
    - pelo menos 1 caractere que não seja letra nem dígito (símbolo)

    >>> senha_forte("Fiap@PosTech2027")
    True
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Bloco B — Coleções e funções (listas, sets, dicts)
# ---------------------------------------------------------------------------

def ips_unicos(ips: list[str]) -> list[str]:
    """Q5. Remove IPs repetidos e retorna a lista em ordem alfabética.

    >>> ips_unicos(["10.0.0.2", "10.0.0.1", "10.0.0.2"])
    ['10.0.0.1', '10.0.0.2']
    """
    raise NotImplementedError


def top_ips(ips: list[str], n: int) -> list[tuple[str, int]]:
    """Q6. Retorna os n IPs mais frequentes como (ip, quantidade).

    Ordem: maior quantidade primeiro; em caso de empate, IP em ordem alfabética.

    >>> top_ips(["1.1.1.1", "2.2.2.2", "1.1.1.1", "3.3.3.3", "2.2.2.2"], 2)
    [('1.1.1.1', 2), ('2.2.2.2', 2)]
    """
    raise NotImplementedError


def portas_do_servico(mapa: dict[int, str], servico: str) -> list[int]:
    """Q7. Dado {porta: serviço}, retorna as portas do serviço pedido, em ordem crescente.

    A comparação do nome do serviço ignora maiúsculas/minúsculas.

    >>> portas_do_servico({80: "http", 443: "https", 8080: "HTTP"}, "http")
    [80, 8080]
    """
    raise NotImplementedError


def media_tamanho(senhas: list[str]) -> float:
    """Q8. Retorna o tamanho médio das senhas. Lista vazia -> 0.0.

    >>> media_tamanho(["abc", "abcde"])
    4.0
    """
    raise NotImplementedError


def agrupar_por_usuario(eventos: list[dict]) -> dict[str, list[str]]:
    """Q9. Agrupa eventos por usuário, mantendo a ordem dos eventos.

    >>> agrupar_por_usuario([
    ...     {"usuario": "ana", "evento": "login"},
    ...     {"usuario": "bob", "evento": "login"},
    ...     {"usuario": "ana", "evento": "logout"},
    ... ])
    {'ana': ['login', 'logout'], 'bob': ['login']}
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Bloco C — Python prático (parsing, regex, arquivos, hashing)
# ---------------------------------------------------------------------------

def parse_linha_log(linha: str) -> dict[str, str]:
    """Q10. Converte uma linha de log no formato

        "<timestamp> <ip> <evento> user=<usuario>"

    em um dicionário com as chaves timestamp, ip, evento e usuario.

    >>> parse_linha_log("2026-11-24T10:00:00 192.168.0.10 LOGIN_FAIL user=admin")
    {'timestamp': '2026-11-24T10:00:00', 'ip': '192.168.0.10', 'evento': 'LOGIN_FAIL', 'usuario': 'admin'}
    """
    raise NotImplementedError


def dominios_normalizados(urls: list[str]) -> set[str]:
    """Q11. Extrai o domínio de cada URL, em minúsculas e sem o prefixo "www.".

    >>> sorted(dominios_normalizados(["https://WWW.Exemplo.com/login", "http://exemplo.com:8080/x"]))
    ['exemplo.com']
    """
    raise NotImplementedError


def extrair_ips(texto: str) -> list[str]:
    """Q12. Extrai endereços IPv4 de um texto, na ordem em que aparecem, sem repetir.

    Considere IPv4 como 4 números de 1 a 3 dígitos separados por ponto
    (não precisa validar se cada número é <= 255).

    >>> extrair_ips("Conexão de 10.0.0.5 para 8.8.8.8; depois 10.0.0.5 de novo")
    ['10.0.0.5', '8.8.8.8']
    """
    raise NotImplementedError


def sha256_texto(texto: str) -> str:
    """Q13. Retorna o hash SHA-256 (em hexadecimal) do texto codificado em UTF-8.

    >>> sha256_texto("abc")[:16]
    'ba7816bf8f01cfea'
    """
    raise NotImplementedError


def alertas_graves(caminho: str) -> list[str]:
    """Q14. Lê um arquivo JSON com uma lista de alertas no formato
    [{"regra": "...", "severidade": 7}, ...] e retorna os nomes das regras
    com severidade >= 7, na ordem do arquivo.

    Se o arquivo não existir, retorna lista vazia (não deixe o erro estourar).
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Bloco D — Orientação a objetos
# ---------------------------------------------------------------------------

class Alerta:
    """Q15. Representa um alerta de segurança.

    - Alerta("Brute force SSH", 9) guarda os atributos `regra` e `severidade`.
    - severidade fora de 1..10 -> ValueError no construtor.
    - eh_critico() -> True se severidade >= 9.
    - str(alerta) -> "[SEV 9] Brute force SSH"
    """

    def __init__(self, regra: str, severidade: int) -> None:
        raise NotImplementedError

    def eh_critico(self) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError
