"""Fase 1 -- Passo 1.3: Simulador (depende da PortaNand da Fase 2)."""

from componentes import PortaNand
from simulador import Simulador


def test_simulador_registra_componente():
    sim = Simulador()
    nand = PortaNand()
    sim.registrar(nand)  # não deve lançar


def test_tick_combinacional_em_um_ciclo():
    """NAND(1,1)=0: lógica combinacional pura estabiliza em um único tick."""
    sim = Simulador()
    nand = PortaNand()
    sim.registrar(nand)
    nand.A.atualizar(True)
    nand.B.atualizar(True)
    sim.tick()
    assert nand.OUT.valor_atual is False


def test_run_until_stable_retorna_numero_de_ticks():
    sim = Simulador()
    nand = PortaNand()
    sim.registrar(nand)
    nand.A.atualizar(False)
    nand.B.atualizar(False)
    n = sim.run_until_stable()
    assert isinstance(n, int)
    assert n >= 1
    assert nand.OUT.valor_atual is True  # NAND(0,0)=1


def test_run_until_stable_respeita_max_ticks():
    """Mesmo num oscilador hipotético, não deve travar."""
    sim = Simulador()
    nand = PortaNand()
    sim.registrar(nand)
    n = sim.run_until_stable(max_ticks=5)
    assert n <= 5
