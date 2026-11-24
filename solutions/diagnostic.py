"""Solutions for the diagnostic test. Só abra depois de tentar!

Repare que há mais de uma solução correta para quase todas as questões.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from urllib.parse import urlparse


def classify_port(port: int) -> str:
    if 0 <= port <= 1023:
        return "well-known"
    if 1024 <= port <= 49151:
        return "registered"
    if 49152 <= port <= 65535:
        return "dynamic"
    raise ValueError(f"Invalid port: {port}")


def mask_email(email: str) -> str:
    user, domain = email.split("@", 1)
    return user[0] + "*" * (len(user) - 1) + "@" + domain


def count_failures(lines: list[str]) -> int:
    return sum(1 for line in lines if "Failed password" in line)


def is_strong_password(password: str) -> bool:
    return (
        len(password) >= 12
        and any(c.isupper() for c in password)
        and any(c.islower() for c in password)
        and any(c.isdigit() for c in password)
        and any(not c.isalnum() for c in password)
    )


def unique_ips(ips: list[str]) -> list[str]:
    return sorted(set(ips))


def top_ips(ips: list[str], n: int) -> list[tuple[str, int]]:
    counts = Counter(ips)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:n]


def ports_for_service(services: dict[int, str], service: str) -> list[int]:
    target = service.lower()
    return sorted(port for port, name in services.items() if name.lower() == target)


def average_length(passwords: list[str]) -> float:
    if not passwords:
        return 0.0
    return sum(len(p) for p in passwords) / len(passwords)


def group_by_user(events: list[dict]) -> dict[str, list[str]]:
    groups: defaultdict[str, list[str]] = defaultdict(list)
    for e in events:
        groups[e["user"]].append(e["event"])
    return dict(groups)


def parse_log_line(line: str) -> dict[str, str]:
    timestamp, ip, event, user = line.split()
    return {
        "timestamp": timestamp,
        "ip": ip,
        "event": event,
        "user": user.removeprefix("user="),
    }


def normalize_domains(urls: list[str]) -> set[str]:
    result = set()
    for url in urls:
        host = (urlparse(url).hostname or "").lower()  # hostname already drops the port
        result.add(host.removeprefix("www."))
    return result


IPV4 = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")


def extract_ips(text: str) -> list[str]:
    # dict.fromkeys removes duplicates while keeping order
    return list(dict.fromkeys(IPV4.findall(text)))


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def severe_alerts(path: str) -> list[str]:
    try:
        with open(path, encoding="utf-8") as f:
            alerts = json.load(f)
    except FileNotFoundError:
        return []
    return [a["rule"] for a in alerts if a["severity"] >= 7]


class Alert:
    def __init__(self, rule: str, severity: int) -> None:
        if not 1 <= severity <= 10:
            raise ValueError("severity must be between 1 and 10")
        self.rule = rule
        self.severity = severity

    def is_critical(self) -> bool:
        return self.severity >= 9

    def __str__(self) -> str:
        return f"[SEV {self.severity}] {self.rule}"
