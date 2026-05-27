"""Fase 3: CircuitoComposto, catálogo e persistência (referência)."""

import os
import tempfile

from biblioteca import construir_not
from circuito import CatalogoCircuitos, CircuitoComposto
from componentes import PortaNand
from simulador import Simulador


def test_catalogo_nasce_com_nand():
    cat = CatalogoCircuitos()
    assert "NAND" in cat.nomes()


def test_instanciar_nand_retorna_porta_funcional():
    cat = CatalogoCircuitos()
    nand = cat.instanciar("NAND")
    assert isinstance(nand, PortaNand)


def test_instanciar_retorna_clones_independentes():
    cat = CatalogoCircuitos()
    n1 = cat.instanciar("NAND")
    n2 = cat.instanciar("NAND")
    assert n1 is not n2
    assert n1.A is not n2.A


def test_not_via_circuito_composto():
    cat = CatalogoCircuitos()
    not_gate = construir_not(cat)
    sim = Simulador()
    sim.registrar(not_gate)

    not_gate.pinos_entrada_externos["IN"].atualizar(False)
    sim.run_until_stable()
    assert not_gate.pinos_saida_externos["OUT"].valor_atual is True

    not_gate.pinos_entrada_externos["IN"].atualizar(True)
    sim.run_until_stable()
    assert not_gate.pinos_saida_externos["OUT"].valor_atual is False


def test_clonar_circuito_composto_isola_estado():
    cat = CatalogoCircuitos()
    original = CircuitoComposto()
    original.subcomponentes.append(cat.instanciar("NAND"))
    clone1 = original.clonar()
    clone2 = original.clonar()
    assert clone1.subcomponentes[0] is not original.subcomponentes[0]
    assert clone1.subcomponentes[0] is not clone2.subcomponentes[0]


def test_salvar_e_carregar_catalogo_preserva_nomes():
    cat = CatalogoCircuitos()
    cat.registrar("NOT", construir_not(cat))

    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        caminho = f.name
    try:
        cat.salvar(caminho)
        cat2 = CatalogoCircuitos()
        cat2.carregar(caminho)
        assert "NOT" in cat2.nomes()
        assert "NAND" in cat2.nomes()
    finally:
        os.unlink(caminho)


def test_not_via_catalogo_apos_salvar_carregar():
    cat = CatalogoCircuitos()
    cat.registrar("NOT", construir_not(cat))

    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        caminho = f.name
    try:
        cat.salvar(caminho)
        cat2 = CatalogoCircuitos()
        cat2.carregar(caminho)
        not_gate = cat2.instanciar("NOT")
        sim = Simulador()
        sim.registrar(not_gate)
        not_gate.pinos_entrada_externos["IN"].atualizar(True)
        sim.run_until_stable()
        assert not_gate.pinos_saida_externos["OUT"].valor_atual is False
    finally:
        os.unlink(caminho)
