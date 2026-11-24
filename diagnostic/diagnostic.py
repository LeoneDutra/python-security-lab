"""Diagnostic test — calibra a checklist do Notion.

Como fazer (tempo sugerido: 2 a 3 horas, pode dividir em dias):
- Resolva na ordem. Vale consultar a documentação, mas anote quando consultou.
- NÃO abra a pasta solutions/ antes de terminar ou de desistir de uma questão.
- Rode:  uv run pytest diagnostic -v
- Ao final, preencha a tabela de autoavaliação em diagnostic/README.md
  e atualize o "Nível" dos tópicos no Notion.

Cada função tem uma docstring com o que fazer e exemplos.
Troque `raise NotImplementedError` pela sua solução.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Block A — Fundamentals (tipos, condicionais, strings, laços)
# ---------------------------------------------------------------------------


def classify_port(port: int) -> str:
    """Q1. Classifica uma porta TCP/UDP.

    - 0 a 1023       -> "well-known"
    - 1024 a 49151   -> "registered"
    - 49152 a 65535  -> "dynamic"
    - fora disso     -> lança ValueError

    >>> classify_port(443)
    'well-known'
    """
    raise NotImplementedError


def mask_email(email: str) -> str:
    """Q2. Esconde o usuário de um e-mail, mantendo só a 1ª letra.

    O número de asteriscos é igual ao número de letras escondidas.

    >>> mask_email("leone@example.com")
    'l****@example.com'
    """
    raise NotImplementedError


def count_failures(lines: list[str]) -> int:
    """Q3. Conta quantas linhas de log contêm "Failed password".

    >>> count_failures(["Failed password for root", "Accepted password for bob"])
    1
    """
    raise NotImplementedError


def is_strong_password(password: str) -> bool:
    """Q4. Retorna True se a senha tem TODOS os critérios:

    - 12 caracteres ou mais
    - pelo menos 1 letra maiúscula, 1 minúscula e 1 dígito
    - pelo menos 1 caractere que não seja letra nem dígito (símbolo)

    >>> is_strong_password("Fiap@PosTech2027")
    True
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Block B — Collections and functions (listas, sets, dicts)
# ---------------------------------------------------------------------------


def unique_ips(ips: list[str]) -> list[str]:
    """Q5. Remove IPs repetidos e retorna a lista em ordem alfabética.

    >>> unique_ips(["10.0.0.2", "10.0.0.1", "10.0.0.2"])
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


def ports_for_service(services: dict[int, str], service: str) -> list[int]:
    """Q7. Dado {porta: serviço}, retorna as portas do serviço pedido, em ordem crescente.

    A comparação do nome do serviço ignora maiúsculas/minúsculas.

    >>> ports_for_service({80: "http", 443: "https", 8080: "HTTP"}, "http")
    [80, 8080]
    """
    raise NotImplementedError


def average_length(passwords: list[str]) -> float:
    """Q8. Retorna o tamanho médio das senhas. Lista vazia -> 0.0.

    >>> average_length(["abc", "abcde"])
    4.0
    """
    raise NotImplementedError


def group_by_user(events: list[dict]) -> dict[str, list[str]]:
    """Q9. Agrupa eventos por usuário, mantendo a ordem dos eventos.

    >>> group_by_user([
    ...     {"user": "ana", "event": "login"},
    ...     {"user": "bob", "event": "login"},
    ...     {"user": "ana", "event": "logout"},
    ... ])
    {'ana': ['login', 'logout'], 'bob': ['login']}
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Block C — Practical Python (parsing, regex, arquivos, hashing)
# ---------------------------------------------------------------------------


def parse_log_line(line: str) -> dict[str, str]:
    """Q10. Converte uma linha de log no formato

        "<timestamp> <ip> <event> user=<user>"

    em um dicionário com as chaves timestamp, ip, event e user.

    >>> parse_log_line("2026-11-24T10:00:00 192.168.0.10 LOGIN_FAIL user=admin")
    {'timestamp': '2026-11-24T10:00:00', 'ip': '192.168.0.10', 'event': 'LOGIN_FAIL', 'user': 'admin'}
    """
    raise NotImplementedError


def normalize_domains(urls: list[str]) -> set[str]:
    """Q11. Extrai o domínio de cada URL, em minúsculas e sem o prefixo "www.".

    >>> sorted(normalize_domains(["https://WWW.Example.com/login", "http://example.com:8080/x"]))
    ['example.com']
    """
    raise NotImplementedError


def extract_ips(text: str) -> list[str]:
    """Q12. Extrai endereços IPv4 de um texto, na ordem em que aparecem, sem repetir.

    Considere IPv4 como 4 números de 1 a 3 dígitos separados por ponto
    (não precisa validar se cada número é <= 255).

    >>> extract_ips("Conexão de 10.0.0.5 para 8.8.8.8; depois 10.0.0.5 de novo")
    ['10.0.0.5', '8.8.8.8']
    """
    raise NotImplementedError


def sha256_text(text: str) -> str:
    """Q13. Retorna o hash SHA-256 (em hexadecimal) do texto codificado em UTF-8.

    >>> sha256_text("abc")[:16]
    'ba7816bf8f01cfea'
    """
    raise NotImplementedError


def severe_alerts(path: str) -> list[str]:
    """Q14. Lê um arquivo JSON com uma lista de alertas no formato
    [{"rule": "...", "severity": 7}, ...] e retorna os nomes das regras
    com severity >= 7, na ordem do arquivo.

    Se o arquivo não existir, retorna lista vazia (não deixe o erro estourar).
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Block D — Object-oriented programming
# ---------------------------------------------------------------------------


class Alert:
    """Q15. Representa um alerta de segurança.

    - Alert("SSH brute force", 9) guarda os atributos `rule` e `severity`.
    - severity fora de 1..10 -> ValueError no construtor.
    - is_critical() -> True se severity >= 9.
    - str(alert) -> "[SEV 9] SSH brute force"
    """

    def __init__(self, rule: str, severity: int) -> None:
        raise NotImplementedError

    def is_critical(self) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError
