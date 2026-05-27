<div align="center">

# 🔌 NANDLand

### Simulador de Circuitos Lógicos Universais a partir da porta NAND

*Construa toda a lógica digital — de uma porta NOT a um flip-flop D — usando apenas NANDs.*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/tests-pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)](https://pytest.org/)
[![Status](https://img.shields.io/badge/status-template%20de%20trabalho-orange?style=flat-square)]()
[![License](https://img.shields.io/badge/license-acadêmico-lightgrey?style=flat-square)]()

</div>

---

## ✨ Sobre

**NANDland** é um exercício prático de arquitetura de software *e* de lógica digital. Você recebe um esqueleto de projeto onde cada método essencial está stubado com `NotImplementedError("Passo X.Y: …")`, e seu trabalho é fazer a suíte de testes passar — passo a passo, fase a fase — até ter um simulador síncrono capaz de executar circuitos compostos arbitrários a partir de uma única primitiva: a **porta NAND**.

> 📄 O enunciado completo está em [`enunciado.pdf`](enunciado.pdf) (fonte LaTeX em [`enunciado.tex`](enunciado.tex)).

---

## 📦 Estrutura do projeto

```
nandland/
├── pinos.py          → PinoEntrada, PinoSaida, PinoEntradaExterna
├── componentes.py    → ComponenteLogico (abstrato), PortaNand
├── simulador.py      → Simulador síncrono
├── circuito.py       → CircuitoComposto, CatalogoCircuitos + persistência JSON
├── biblioteca.py     → NOT, AND, SR_LATCH, D_LATCH, D_FLIP_FLOP, REGISTRO_1BIT
└── tests/
    ├── conftest.py
    ├── test_fase1_pinos.py
    ├── test_fase1_simulador.py
    ├── test_fase2_nand.py
    ├── test_fase3_composto_e_catalogo.py
    └── test_fase4_sequencial.py
```

---

## 🚀 Começando

### Instalação

```bash
pip install pytest
```

### Rodando os testes

```bash
python -m pytest tests/ -v
```

No início, **todos os testes falham com `NotImplementedError`** — isso é esperado. À medida que cada passo é implementado, mais testes passam. Quando os **34/34** passarem, as Fases 1–4 estão completas. 🎉

### Atalhos úteis

| Comando | Descrição |
|---|---|
| `python -m pytest -q` | Resumo enxuto |
| `python -m pytest tests/test_fase1_pinos.py -v` | Roda apenas a Fase 1 (pinos) |
| `python -m pytest tests/test_fase2_nand.py -v` | Roda apenas a Fase 2 (NAND) |
| `python -m pytest -k flip_flop -v` | Filtra por nome |

---

## 🗺️ Roteiro de fases

> As fases podem ser feitas em qualquer ritmo, sem prazos semanais fixos. Entregue o máximo que conseguir — cada fase tem sua própria bateria de testes como critério de aceitação.

| Fase | Foco                                | Arquivos                                         | Passos               |
|:---:|--------------------------------------|--------------------------------------------------|----------------------|
| 1️⃣  | Pinos e simulador combinacional     | `pinos.py`, `componentes.py`, `simulador.py`     | 1.1–1.3, 2.1–2.5     |
| 2️⃣  | Porta NAND + circuitos compostos    | `circuito.py`, `biblioteca.py` (parcial)         | 3.1–3.4 (+ `construir_not`) |
| 3️⃣  | Lógica sequencial (latches, FF)     | `biblioteca.py` (sequencial)                     | 4.1–4.4              |
| 4️⃣  | *(opcional)* GUI                    | extra                                            | Fase 5               |

---

## 🔁 Dinâmica de entrega via GitHub

Todo o desenvolvimento acontece no GitHub seguindo um fluxo baseado em **Pull Requests**. ❌ Não faça commits diretamente em `main`.

### Fluxo recomendado

<details>
<summary><strong>1. Fork e clone</strong></summary>

```bash
git clone https://github.com/<seu-usuario>/nandland.git
cd nandland
git remote add upstream https://github.com/<owner>/nandland.git
```
</details>

<details>
<summary><strong>2. Crie uma branch por fase/passo</strong></summary>

Nunca trabalhe direto em `main`. Use nomes descritivos:

```bash
git checkout -b fase1/pinos
git checkout -b fase2/porta-nand
git checkout -b fase3/d-flip-flop
```
</details>

<details>
<summary><strong>3. Commits pequenos e frequentes</strong></summary>

Mensagens claras, no imperativo:
- ✅ `implementa PinoSaida`
- ✅ `corrige propagação no Simulador`
- ❌ `mudei umas coisas`

Cada commit deve, idealmente, deixar a suíte em um estado coerente.
</details>

<details>
<summary><strong>4. Rode os testes antes de abrir o PR</strong></summary>

```bash
python -m pytest -q
```

Informe no corpo do PR quais testes passam — ex.: `Fase 1: 12/12`, `Fase 2: 8/8`.
</details>

<details>
<summary><strong>5. Abra o Pull Request</strong></summary>

Do seu *fork* para a branch `main` do repositório original. O título deve identificar a fase/passo, por exemplo:

> `Fase 2 — Porta NAND e propagação`
</details>

<details>
<summary><strong>6. Descrição do PR</strong></summary>

Deve conter:
- 🔧 O que foi implementado (passos cobertos, ex.: 2.1–2.5).
- ▶️ Como rodar/validar (comando de testes + resultado esperado).
- ❓ Pontos em aberto, dúvidas ou decisões de projeto.
</details>

<details>
<summary><strong>7. Code review</strong></summary>

Responda aos comentários com novos commits na mesma branch — o PR atualiza sozinho. Evite `force-push` após o início da revisão, para preservar o histórico da discussão.
</details>

<details>
<summary><strong>8. Merge e sincronização</strong></summary>

O *merge* é feito pelo revisor após aprovação. Depois:

```bash
git checkout main
git pull upstream main
git push origin main
```
</details>

### ✅ Boas práticas

- **Um PR por fase** (ou por passo, se a fase for grande). PRs gigantes são difíceis de revisar.
- Nunca inclua arquivos gerados (`__pycache__/`, `.pytest_cache/`, configs de IDE) — use `.gitignore`.
- **Nunca** faça commit de credenciais, chaves ou dados pessoais.
- Mantenha sua branch atualizada com `main` via `git rebase upstream/main` (ou `git merge`) antes de pedir revisão.

---

<div align="center">

*Feito para ensinar — uma porta NAND de cada vez.* ⚡

</div>
