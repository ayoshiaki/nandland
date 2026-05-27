"""Testes para analise.py.

Como o esqueleto do simulador ainda contém NotImplementedError, os testes
usam dublês leves (fakes) que implementam apenas a superfície de API que
analise.py consome. Quando os alunos completarem as fases 1-3 do
simulador, as mesmas funções continuarão funcionando sobre os objetos
reais sem alteração.
"""

from __future__ import annotations

import types

import pytest

import analise
from componentes import ComponenteLogico, PortaNand
from circuito import CircuitoComposto


# ---------- Fakes -----------------------------------------------------

class FakeNand(ComponenteLogico):
    """Substituto de PortaNand sem __init__ quebrado.

    Reusamos o nome da classe verdadeira fazendo monkeypatch global do
    isinstance via subclasse: registramos FakeNand como subclasse de
    PortaNand não — em vez disso, os testes que dependem de PortaNand
    constroem instâncias reais quando possível (e quando não, marcam
    skip).
    """

    def avaliar(self):  # pragma: no cover
        pass

    def clonar(self):  # pragma: no cover
        return FakeNand()


class FakeComposto(ComponenteLogico):
    """Mimetiza CircuitoComposto: tem `componentes_internos`."""

    def __init__(self, filhos, saidas=()):
        self.componentes_internos = list(filhos)
        self._saidas = list(saidas)

    def avaliar(self):  # pragma: no cover
        pass

    def clonar(self):  # pragma: no cover
        return FakeComposto(self.componentes_internos, self._saidas)

    def pinos_saida_internos(self):
        proprias = list(self._saidas)
        for c in self.componentes_internos:
            proprias.extend(c.pinos_saida_internos())
        return proprias


class FakePinoSaida:
    def __init__(self, valor_atual=False, valor_proximo=None, n_conectados=0):
        self.valor_atual = valor_atual
        self.valor_proximo = valor_atual if valor_proximo is None else valor_proximo
        self.conectados = [object()] * n_conectados


def _fake_simulador(pinos):
    sim = types.SimpleNamespace()
    sim.saidas_a_registrar = list(pinos)
    return sim


# Tentamos instanciar PortaNand real; se falhar (esqueleto), usamos FakeNand
# e fazemos isinstance checks via patching local.
try:
    _real_nand = PortaNand()
    _USA_REAL_NAND = True
except NotImplementedError:
    _USA_REAL_NAND = False


def _nand():
    """Retorna uma instância que conta como PortaNand para analise.contar_nands.

    Quando a PortaNand real não está implementada, monkeypatch isinstance
    fica frágil — então, em vez disso, redefinimos analise.PortaNand para
    FakeNand no nível do módulo apenas para a sessão de teste.
    """
    if _USA_REAL_NAND:
        return PortaNand()
    return FakeNand()


@pytest.fixture(autouse=True)
def _patch_porta_nand(monkeypatch):
    if not _USA_REAL_NAND:
        monkeypatch.setattr(analise, "PortaNand", FakeNand)
    # CircuitoComposto real também pode estar quebrado: usamos FakeComposto
    # como referência de tipo para o teste de profundidade.
    try:
        CircuitoComposto()
    except NotImplementedError:
        monkeypatch.setattr(analise, "CircuitoComposto", FakeComposto)


# ---------- Testes ----------------------------------------------------

def test_contar_nands_folha():
    assert analise.contar_nands(_nand()) == 1


def test_contar_nands_aninhado():
    c = FakeComposto([_nand(), _nand(), FakeComposto([_nand()])])
    assert analise.contar_nands(c) == 3


def test_contar_nands_sem_nands():
    assert analise.contar_nands(FakeComposto([])) == 0


def test_tipos_de_componentes():
    c = FakeComposto([_nand(), FakeComposto([_nand()])])
    tipos = analise.tipos_de_componentes(c)
    nomes = {t.__name__ for t in tipos}
    assert "FakeComposto" in nomes
    assert any(n in nomes for n in ("PortaNand", "FakeNand"))


def test_fan_out_maximo():
    p1 = FakePinoSaida(n_conectados=1)
    p2 = FakePinoSaida(n_conectados=5)
    p3 = FakePinoSaida(n_conectados=2)
    c = FakeComposto([], saidas=[p1, p2, p3])
    assert analise.fan_out_maximo(c) == 5


def test_fan_out_maximo_vazio():
    assert analise.fan_out_maximo(FakeComposto([])) == 0


def test_pinos_ativos():
    p1 = FakePinoSaida(valor_atual=True)
    p2 = FakePinoSaida(valor_atual=False)
    p3 = FakePinoSaida(valor_atual=True)
    sim = _fake_simulador([p1, p2, p3])
    assert analise.pinos_ativos(sim) == [p1, p3]


def test_pinos_instaveis():
    estavel = FakePinoSaida(valor_atual=True, valor_proximo=True)
    instavel = FakePinoSaida(valor_atual=False, valor_proximo=True)
    sim = _fake_simulador([estavel, instavel])
    assert analise.pinos_instaveis(sim) == [instavel]


def test_taxa_de_atividade():
    sim = _fake_simulador(
        [
            FakePinoSaida(valor_atual=True),
            FakePinoSaida(valor_atual=False),
            FakePinoSaida(valor_atual=True),
            FakePinoSaida(valor_atual=False),
        ]
    )
    assert analise.taxa_de_atividade(sim) == 0.5


def test_taxa_de_atividade_vazia():
    assert analise.taxa_de_atividade(_fake_simulador([])) == 0.0


def test_profundidade_primitivo():
    assert analise.profundidade(_nand()) == 0


def test_profundidade_um_nivel():
    c = FakeComposto([_nand(), _nand()])
    assert analise.profundidade(c) == 1


def test_profundidade_aninhado():
    c = FakeComposto([FakeComposto([FakeComposto([_nand()])])])
    assert analise.profundidade(c) == 3


def test_histograma_por_tipo():
    c = FakeComposto([_nand(), _nand(), FakeComposto([_nand()])])
    h = analise.histograma_por_tipo(c)
    nand_key = "PortaNand" if _USA_REAL_NAND else "FakeNand"
    assert h[nand_key] == 3
    assert h["FakeComposto"] == 2


def test_relatorio_chaves():
    c = FakeComposto([_nand(), FakeComposto([_nand(), _nand()])])
    rel = analise.relatorio(c)
    assert set(rel.keys()) == {
        "nands",
        "tipos",
        "fan_out_maximo",
        "profundidade",
        "histograma",
    }
    assert rel["nands"] == 3
    assert rel["profundidade"] == 2


# ---------- circuitos_que_usam: depende do catálogo real --------------

def test_circuitos_que_usam_requer_catalogo_real():
    """Smoke test: roda apenas se o catálogo (Fase 3) estiver implementado."""
    try:
        from circuito import CatalogoCircuitos
        from biblioteca import popular_catalogo

        cat = CatalogoCircuitos()
        popular_catalogo(cat)
    except NotImplementedError:
        pytest.skip("CatalogoCircuitos ainda não implementado")

    usuarios = analise.circuitos_que_usam(cat, "AND")
    assert isinstance(usuarios, list)
