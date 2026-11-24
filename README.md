# 🐍 Python Security Lab

[![CI](https://github.com/LeoneDutra/python-security-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/LeoneDutra/python-security-lab/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![Tests](https://img.shields.io/badge/tests-pytest-green)
![Lint](https://img.shields.io/badge/lint-ruff-purple)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

My hands-on lab for learning Python from the fundamentals to intermediate level,
with every exercise framed around **security operations and AI for security**:
log parsing, IOC extraction, hashing, alert triage, ML-based detection and secure LLM agents.

It is my preparation track for a postgraduate program in **AI for Security Engineering** (FIAP, starting March 2027).

## 🗺️ Roadmap

| Phase | Topic | Security focus | Status |
|---|---|---|---|
| 0 | Environment (uv, Git, pytest, Jupyter) | Secrets hygiene (`.env`, `.gitignore`) | 🟡 In progress |
| 1 | Fundamentals | Password strength checker | ⏳ |
| 2 | Practical Python (files, regex, CLI, logging) | SSH brute-force detector | ⏳ |
| 3 | Intermediate (OOP, testing, APIs, async) | IOC extractor with reputation lookup | ⏳ |
| 4 | Data (numpy, pandas) | Network traffic exploratory analysis | ⏳ |
| 5 | Machine Learning (scikit-learn) | Phishing URL classifier, log anomaly detection | ⏳ |
| 6 | LLMs, agents and MCP | Incident triage assistant, MCP server with SOC tools | ⏳ |
| 7 | AI security | Prompt injection tests, LLM Guard guardrails, MCP hardening | ⏳ |

**Capstone:** an AI-assisted SOC analyst. Wazuh alerts → ML prioritisation → LLM agent investigating via MCP tools → guardrails → incident report.

## 🚀 Getting started

Requires [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/LeoneDutra/python-security-lab.git
cd python-security-lab
uv sync                      # creates .venv and installs dependencies
uv run pytest                # runs every exercise's tests
uv run pytest diagnostic -v  # runs a single folder, verbose
```

## 📁 Structure

| Folder | Content |
|---|---|
| `phase0_setup/` | Checks the environment (Python version, virtualenv, pytest) |
| `diagnostic/` | 15-question diagnostic used to calibrate the learning plan |
| `solutions/` | Reference solutions (opened only after attempting an exercise) |
| `phaseN_*/` | Exercises for each phase, added as the schedule advances |
| `projects/` | Phase projects and the capstone |

## 🧪 How exercises work

Each exercise is a Python module with function stubs (`raise NotImplementedError`) and
docstrings describing the expected behaviour, plus a `pytest` file that checks it.
The workflow is: read the docstring → implement → run the tests until green → commit.

CI runs `ruff` and validates the whole test suite against the reference solutions
(`SOLUTIONS=1 uv run pytest`) on every push.

## 🔐 Lab rules

- No secrets in code. API keys live in `.env` (see `.env.example`), which is git-ignored.
- Network tools (scanners etc.) are only run against my own lab.
- Malware analysis uses harmless test files or isolated VMs only.

## 📄 License

[MIT](LICENSE)
