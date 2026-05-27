"""Pinos (Fase 1, Passos 1.1 e 1.2) e PinoEntradaExterna (Fase 3, Passo 3.1).

- PinoEntrada: lê valor_atual (escrito apenas via atualizar()).
- PinoSaida: buffer duplo (valor_atual e valor_proximo); commit() promove e
  notifica os observadores.
- PinoEntradaExterna: usado por CircuitoComposto para distribuir um sinal
  externo para múltiplos pinos internos.
"""

from __future__ import annotations


class PinoEntrada:
    def __init__(self, componente):
        # TODO Passo 1.1
        raise NotImplementedError("Passo 1.1: PinoEntrada.__init__")

    def atualizar(self, novo_estado: bool) -> None:
        # TODO Passo 1.1
        raise NotImplementedError("Passo 1.1: PinoEntrada.atualizar")


class PinoSaida:
    def __init__(self, componente):
        # TODO Passo 1.2
        raise NotImplementedError("Passo 1.2: PinoSaida.__init__")

    def conectar(self, pino_entrada: PinoEntrada) -> None:
        # TODO Passo 1.2
        raise NotImplementedError("Passo 1.2: PinoSaida.conectar")

    def set_proximo(self, novo_estado: bool) -> None:
        # TODO Passo 1.2
        raise NotImplementedError("Passo 1.2: PinoSaida.set_proximo")

    def commit(self) -> bool:
        # TODO Passo 1.2
        raise NotImplementedError("Passo 1.2: PinoSaida.commit")


class PinoEntradaExterna(PinoEntrada):
    """Pino de entrada de um CircuitoComposto: propaga a escrita para todos
    os pinos internos espelhados (fan-out)."""

    def __init__(self):
        # TODO Passo 3.1
        raise NotImplementedError("Passo 3.1: PinoEntradaExterna.__init__")

    def conectar_interno(self, pino: PinoEntrada) -> None:
        # TODO Passo 3.1
        raise NotImplementedError("Passo 3.1: PinoEntradaExterna.conectar_interno")

    def atualizar(self, novo_estado: bool) -> None:
        # TODO Passo 3.1
        raise NotImplementedError("Passo 3.1: PinoEntradaExterna.atualizar")
