# 🩺 Teste diagnóstico

São 15 questões em 4 blocos. O objetivo **não é tirar 100%**: é descobrir o que você já domina
para pular o que é fácil e gastar tempo no que é fraco.

```bash
uv run pytest diagnostico -v          # roda tudo
uv run pytest diagnostico -k q04 -v   # roda só a questão 4
```

## Autoavaliação

Para cada questão, marque como foi:

- **A** — passei sozinho, sem consultar nada → tópicos em **3 — Confortável**
- **B** — passei, mas consultei documentação ou exemplos → **2 — Com consulta**
- **C** — passei só depois de olhar o gabarito → **1 — Já vi**
- **D** — não consegui / não entendi o enunciado → **0 — Não vi**

| Questão | Tópicos da checklist (Notion) | Resultado (A/B/C/D) |
|---|---|---|
| Q1 `classificar_porta` | Condicionais; Operadores; raise e exceções | |
| Q2 `mascarar_email` | Strings: índices e fatiamento; Métodos de string | |
| Q3 `contar_falhas` | Laço for; Métodos de string | |
| Q4 `senha_forte` | Métodos de string; Operadores lógicos; Funções | |
| Q5 `ips_unicos` | Conjuntos; Listas | |
| Q6 `top_ips` | Dicionários; collections (Counter); lambda e sorted com key | |
| Q7 `portas_do_servico` | Dicionários; Compreensões de lista | |
| Q8 `media_tamanho` | Funções; Conversão de tipos | |
| Q9 `agrupar_por_usuario` | Dicionários aninhados; collections (defaultdict) | |
| Q10 `parse_linha_log` | Tuplas e desempacotamento; Métodos de string | |
| Q11 `dominios_normalizados` | Módulos (import); Conjuntos; Métodos de string | |
| Q12 `extrair_ips` | Regex básico; Regex com grupos | |
| Q13 `sha256_texto` | hashlib; Bytes e encodings | |
| Q14 `alertas_graves` | Arquivos (with open); JSON; try/except | |
| Q15 `Alerta` | Classes e objetos; Atributos, métodos e `__init__`; Métodos especiais | |

Depois de preencher, atualize o **Nível** dos tópicos no Notion (Checklist → visão "Por fase").
Se um tópico aparecer em mais de uma questão, fique com o **menor** resultado.
