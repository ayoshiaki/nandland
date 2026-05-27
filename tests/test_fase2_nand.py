"""Fase 2: PortaNand."""

import pytest

from componentes import PortaNand
from simulador import Simulador


def test_porta_nand_tem_pinos():
    n = PortaNand()
    assert n.A is not None
    assert n.B is not None
    assert n.OUT is not None


@pytest.mark.parametrize("a,b,esperado", [
    (False, False, True),
    (False, True,  True),
    (True,  False, True),
    (True,  True,  False),
])
def test_tabela_verdade_nand(a, b, esperado):
    sim = Simulador()
    nand = PortaNand()
    sim.registrar(nand)
    nand.A.atualizar(a)
    nand.B.atualizar(b)
    sim.run_until_stable()
    assert nand.OUT.valor_atual is esperado


def test_clonar_produz_instancia_independente():
    n1 = PortaNand()
    n2 = n1.clonar()
    assert n1 is not n2
    assert n1.A is not n2.A
    assert n1.B is not n2.B
    assert n1.OUT is not n2.OUT


def test_clone_sem_conexoes_herdadas():
    n1 = PortaNand()
    # simula uma conexão no original
    from pinos import PinoEntrada
    alvo = PinoEntrada(componente=None)
    n1.OUT.conectar(alvo)
    n2 = n1.clonar()
    # ao mudar a saída do clone, o alvo original NÃO deve ser afetado
    n2.OUT.set_proximo(True)
    n2.OUT.commit()
    assert alvo.valor_atual is False, "clone não deve compartilhar observadores"
