# 🩺 Diagnostic test

> 🇧🇷 Instruções de estudo em português. *15 security-flavored questions used to calibrate the learning checklist.*

São 15 questões em 4 blocos. O objetivo **não é tirar 100%**: é descobrir o que você já domina
para pular o que é fácil e gastar tempo no que é fraco.

```bash
uv run pytest diagnostic -v          # roda tudo
uv run pytest diagnostic -k q04 -v   # roda só a questão 4
```

## Autoavaliação

Para cada questão, marque como foi:

- **A** — passei sozinho, sem consultar nada → tópicos em **3 — Confortável**
- **B** — passei, mas consultei documentação ou exemplos → **2 — Com consulta**
- **C** — passei só depois de olhar a solução → **1 — Já vi**
- **D** — não consegui / não entendi o enunciado → **0 — Não vi**

| Questão | Tópicos da checklist (Notion) | Resultado (A/B/C/D) |
|---|---|---|
| Q1 `classify_port` | Condicionais; Operadores; raise e exceções | |
| Q2 `mask_email` | Strings: índices e fatiamento; Métodos de string | |
| Q3 `count_failures` | Laço for; Métodos de string | |
| Q4 `is_strong_password` | Métodos de string; Operadores lógicos; Funções | |
| Q5 `unique_ips` | Conjuntos; Listas | |
| Q6 `top_ips` | Dicionários; collections (Counter); lambda e sorted com key | |
| Q7 `ports_for_service` | Dicionários; Compreensões de lista | |
| Q8 `average_length` | Funções; Conversão de tipos | |
| Q9 `group_by_user` | Dicionários aninhados; collections (defaultdict) | |
| Q10 `parse_log_line` | Tuplas e desempacotamento; Métodos de string | |
| Q11 `normalize_domains` | Módulos (import); Conjuntos; Métodos de string | |
| Q12 `extract_ips` | Regex básico; Regex com grupos | |
| Q13 `sha256_text` | hashlib; Bytes e encodings | |
| Q14 `severe_alerts` | Arquivos (with open); JSON; try/except | |
| Q15 `Alert` | Classes e objetos; Atributos, métodos e `__init__`; Métodos especiais | |

Depois de preencher, atualize o **Nível** dos tópicos no Notion (Checklist → visão "Por fase").
Se um tópico aparecer em mais de uma questão, fique com o **menor** resultado.
