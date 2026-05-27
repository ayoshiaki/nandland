"""Fase 4: SR-latch, D flip-flop, registro 1 bit (referência)."""

from biblioteca import (
    construir_sr_latch,
    construir_d_flip_flop,
    construir_registro_1bit,
)
from circuito import CatalogoCircuitos
from simulador import Simulador


def test_sr_latch_set_hold_reset():
    cat = CatalogoCircuitos()
    sr = construir_sr_latch(cat)
    sim = Simulador()
    sim.registrar(sr)

    S = sr.pinos_entrada_externos["S"]
    R = sr.pinos_entrada_externos["R"]
    Q = sr.pinos_saida_externos["Q"]

    # SET: S=0, R=1 -> Q=1
    S.atualizar(False)
    R.atualizar(True)
    sim.run_until_stable()
    assert Q.valor_atual is True

    # HOLD: S=1, R=1 -> Q permanece 1
    S.atualizar(True)
    sim.run_until_stable()
    assert Q.valor_atual is True

    # RESET: S=1, R=0 -> Q=0
    R.atualizar(False)
    sim.run_until_stable()
    assert Q.valor_atual is False


def test_d_flip_flop_borda_de_subida_e_retencao():
    cat = CatalogoCircuitos()
    dff = construir_d_flip_flop(cat)
    sim = Simulador()
    sim.registrar(dff)

    D = dff.pinos_entrada_externos["D"]
    CLK = dff.pinos_entrada_externos["CLK"]
    Q = dff.pinos_saida_externos["Q"]

    CLK.atualizar(False)
    D.atualizar(False)
    sim.run_until_stable()

    # captura D=True na borda de subida
    D.atualizar(True)
    CLK.atualizar(True)
    sim.run_until_stable()
    assert Q.valor_atual is True

    # baixa o clock; mudança em D não deve afetar Q
    CLK.atualizar(False)
    D.atualizar(False)
    sim.run_until_stable()
    assert Q.valor_atual is True

    # nova borda de subida agora captura D=False
    CLK.atualizar(True)
    sim.run_until_stable()
    assert Q.valor_atual is False


def test_registro_1bit_retem_estado_sem_clock():
    cat = CatalogoCircuitos()
    reg = construir_registro_1bit(cat)
    sim = Simulador()
    sim.registrar(reg)

    D = reg.pinos_entrada_externos["D"]
    CLK = reg.pinos_entrada_externos["CLK"]
    Q = reg.pinos_saida_externos["Q"]

    CLK.atualizar(False)
    D.atualizar(True)
    sim.run_until_stable()
    CLK.atualizar(True)
    sim.run_until_stable()
    assert Q.valor_atual is True

    CLK.atualizar(False)
    D.atualizar(False)
    for _ in range(10):
        sim.tick()
    assert Q.valor_atual is True
