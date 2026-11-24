# 🐍 Python Security Lab

Meu laboratório de estudos de Python, do básico ao intermediário, com foco em **IA aplicada à Segurança**.
Preparação para a Pós Tech FIAP — *IA para Engenharia de Segurança* (início em 07/03/2027).

O progresso (checklist, cronograma e projetos) fica no Notion; aqui fica o código.

## Como rodar

```bash
uv sync                 # cria o .venv e instala as dependências
uv run pytest           # roda todos os testes
uv run pytest diagnostico -v   # roda só uma pasta, mostrando cada teste
```

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `fase0_ambiente/` | Confere se o ambiente está certo (Python, venv, pytest) |
| `diagnostico/` | Teste diagnóstico para calibrar a checklist |
| `gabaritos/` | Soluções. **Só abra depois de tentar.** |
| `faseN_.../` | Exercícios de cada fase (adicionados conforme o cronograma) |
| `projetos/` | Mini-projetos e projeto final |

## Fluxo de um exercício

1. Abra o arquivo do exercício e leia a docstring de cada função.
2. Troque o `raise NotImplementedError` pela sua solução.
3. Rode `uv run pytest <pasta> -v` até tudo ficar verde.
4. Registre no Notion (status, tempo, se precisou do gabarito).
5. `git add`, `git commit -m "..."` e `git push`.

## Regras do lab

- Nada de segredos no código: chaves de API vão no `.env` (veja `.env.example`).
- Ferramentas de rede (scanners etc.) só contra o meu próprio lab.
- Amostras de malware só em VM isolada; nos exercícios usamos arquivos de teste inofensivos.
