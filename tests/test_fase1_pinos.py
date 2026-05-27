"""Fase 1 -- Passos 1.1 e 1.2: PinoEntrada e PinoSaida (buffer duplo)."""

import pytest

from pinos import PinoEntrada, PinoSaida


# ---------- PinoEntrada (Passo 1.1) ----------

def test_pino_entrada_estado_inicial_false():
    e = PinoEntrada(componente=None)
    assert e.valor_atual is False


def test_pino_entrada_guarda_componente():
    obj = object()
    e = PinoEntrada(componente=obj)
    assert e.componente is obj


def test_pino_entrada_atualizar():
    e = PinoEntrada(componente=None)
    e.atualizar(True)
    assert e.valor_atual is True
    e.atualizar(False)
    assert e.valor_atual is False


# ---------- PinoSaida (Passo 1.2) ----------

def test_pino_saida_buffer_duplo_inicial():
    s = PinoSaida(componente=None)
    assert s.valor_atual is False
    assert s.valor_proximo is False


def test_set_proximo_nao_muda_valor_atual():
    s = PinoSaida(componente=None)
    s.set_proximo(True)
    assert s.valor_proximo is True, "valor_proximo deve refletir set_proximo"
    assert s.valor_atual is False, "set_proximo NÃO pode alterar valor_atual"


def test_set_proximo_nao_notifica_observadores():
    s = PinoSaida(componente=None)
    e = PinoEntrada(componente=None)
    s.conectar(e)
    s.set_proximo(True)
    assert e.valor_atual is False, "observador não pode ser notificado por set_proximo"


def test_commit_promove_proximo_a_atual():
    s = PinoSaida(componente=None)
    s.set_proximo(True)
    s.commit()
    assert s.valor_atual is True


def test_commit_notifica_um_observador():
    s = PinoSaida(componente=None)
    e = PinoEntrada(componente=None)
    s.conectar(e)
    s.set_proximo(True)
    s.commit()
    assert e.valor_atual is True


def test_commit_notifica_multiplos_observadores_simultaneamente():
    s = PinoSaida(componente=None)
    e1 = PinoEntrada(componente=None)
    e2 = PinoEntrada(componente=None)
    e3 = PinoEntrada(componente=None)
    for e in (e1, e2, e3):
        s.conectar(e)
    s.set_proximo(True)
    s.commit()
    assert all(e.valor_atual is True for e in (e1, e2, e3))


def test_commit_retorna_true_quando_muda():
    s = PinoSaida(componente=None)
    s.set_proximo(True)
    assert s.commit() is True


def test_commit_retorna_false_quando_nao_muda():
    s = PinoSaida(componente=None)
    # valor_atual e valor_proximo já são False -> nada muda
    assert s.commit() is False


def test_commit_retorna_false_em_chamada_repetida():
    s = PinoSaida(componente=None)
    s.set_proximo(True)
    s.commit()       # primeira: muda False->True
    assert s.commit() is False, "segunda commit não muda nada"


def test_set_proximo_repetido_apenas_ultimo_vence():
    """Múltiplas escritas no mesmo ciclo: só a última conta."""
    s = PinoSaida(componente=None)
    e = PinoEntrada(componente=None)
    s.conectar(e)
    s.set_proximo(True)
    s.set_proximo(False)
    s.commit()
    assert e.valor_atual is False
