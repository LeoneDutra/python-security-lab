import importlib
import json
import os

import pytest

d = importlib.import_module(
    "solutions.diagnostic" if os.getenv("SOLUTIONS") else "diagnostic.diagnostic"
)


# Block A ------------------------------------------------------------------

@pytest.mark.parametrize(
    ("port", "expected"),
    [(0, "well-known"), (22, "well-known"), (1023, "well-known"), (1024, "registered"),
     (3389, "registered"), (49151, "registered"), (49152, "dynamic"), (65535, "dynamic")],
)
def test_q01_classify_port(port, expected):
    assert d.classify_port(port) == expected


@pytest.mark.parametrize("port", [-1, 65536, 100000])
def test_q01_invalid_port(port):
    with pytest.raises(ValueError):
        d.classify_port(port)


def test_q02_mask_email():
    assert d.mask_email("leone@example.com") == "l****@example.com"
    assert d.mask_email("a@b.com") == "a@b.com"
    assert d.mask_email("soc.team@company.com.br") == "s*******@company.com.br"


def test_q03_count_failures():
    lines = [
        "Nov 24 10:00:01 srv sshd[1]: Failed password for root from 1.2.3.4",
        "Nov 24 10:00:02 srv sshd[1]: Accepted password for bob from 5.6.7.8",
        "Nov 24 10:00:03 srv sshd[1]: Failed password for invalid user test from 1.2.3.4",
    ]
    assert d.count_failures(lines) == 2
    assert d.count_failures([]) == 0


@pytest.mark.parametrize(
    ("password", "expected"),
    [("Fiap@PosTech2027", True), ("short@1A", False), ("NoSymbol2027ABcd", False),
     ("NOLOWERCASE@2027", False), ("nouppercase@2027", False), ("NoDigits@@@@abc", False)],
)
def test_q04_is_strong_password(password, expected):
    assert d.is_strong_password(password) is expected


# Block B ------------------------------------------------------------------

def test_q05_unique_ips():
    assert d.unique_ips(["10.0.0.2", "10.0.0.1", "10.0.0.2"]) == ["10.0.0.1", "10.0.0.2"]
    assert d.unique_ips([]) == []


def test_q06_top_ips():
    ips = ["1.1.1.1", "2.2.2.2", "1.1.1.1", "3.3.3.3", "2.2.2.2", "9.9.9.9", "9.9.9.9", "9.9.9.9"]
    assert d.top_ips(ips, 1) == [("9.9.9.9", 3)]
    assert d.top_ips(ips, 3) == [("9.9.9.9", 3), ("1.1.1.1", 2), ("2.2.2.2", 2)]


def test_q07_ports_for_service():
    services = {8080: "HTTP", 80: "http", 443: "https", 22: "ssh"}
    assert d.ports_for_service(services, "http") == [80, 8080]
    assert d.ports_for_service(services, "SSH") == [22]
    assert d.ports_for_service(services, "ftp") == []


def test_q08_average_length():
    assert d.average_length(["abc", "abcde"]) == 4.0
    assert d.average_length([]) == 0.0


def test_q09_group_by_user():
    events = [
        {"user": "ana", "event": "login"},
        {"user": "bob", "event": "login"},
        {"user": "ana", "event": "logout"},
    ]
    assert d.group_by_user(events) == {"ana": ["login", "logout"], "bob": ["login"]}
    assert d.group_by_user([]) == {}


# Block C ------------------------------------------------------------------

def test_q10_parse_log_line():
    line = "2026-11-24T10:00:00 192.168.0.10 LOGIN_FAIL user=admin"
    assert d.parse_log_line(line) == {
        "timestamp": "2026-11-24T10:00:00",
        "ip": "192.168.0.10",
        "event": "LOGIN_FAIL",
        "user": "admin",
    }


def test_q11_normalize_domains():
    urls = [
        "https://WWW.Example.com/login",
        "http://example.com:8080/x",
        "https://bank-phishing.xyz/?a=1",
        "https://sub.domain.org",
    ]
    assert d.normalize_domains(urls) == {"example.com", "bank-phishing.xyz", "sub.domain.org"}


def test_q12_extract_ips():
    text = "Connection from 10.0.0.5 to 8.8.8.8; later 10.0.0.5 again. Version 1.2 is not an IP."
    assert d.extract_ips(text) == ["10.0.0.5", "8.8.8.8"]
    assert d.extract_ips("no ip here") == []


def test_q13_sha256_text():
    assert d.sha256_text("abc") == (
        "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    )
    assert len(d.sha256_text("")) == 64


def test_q14_severe_alerts(tmp_path):
    file = tmp_path / "alerts.json"
    file.write_text(json.dumps([
        {"rule": "Port scan", "severity": 5},
        {"rule": "SSH brute force", "severity": 9},
        {"rule": "Malware detected", "severity": 7},
    ]), encoding="utf-8")
    assert d.severe_alerts(str(file)) == ["SSH brute force", "Malware detected"]


def test_q14_missing_file(tmp_path):
    assert d.severe_alerts(str(tmp_path / "missing.json")) == []


# Block D ------------------------------------------------------------------

def test_q15_alert():
    a = d.Alert("SSH brute force", 9)
    assert a.rule == "SSH brute force"
    assert a.severity == 9
    assert a.is_critical() is True
    assert str(a) == "[SEV 9] SSH brute force"
    assert d.Alert("Port scan", 4).is_critical() is False


@pytest.mark.parametrize("severity", [0, 11])
def test_q15_alert_invalid_severity(severity):
    with pytest.raises(ValueError):
        d.Alert("x", severity)
