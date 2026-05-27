"""Simulador síncrono (Fase 1, Passo 1.3)."""

from __future__ import annotations

from componentes import ComponenteLogico
from pinos import PinoSaida


class OscilacaoDetectada(RuntimeError):
    """Levantada por Simulador.run_until_stable quando o circuito não
    estabiliza dentro de max_ticks. Sua implementação de run_until_stable
    deve lançar esta exceção (já pronta — não modifique)."""


class Simulador:
    def __init__(self):
        # TODO Passo 1.3
        raise NotImplementedError("Passo 1.3: Simulador.__init__")

    def registrar(self, componente: ComponenteLogico) -> None:
        # TODO Passo 1.3
        raise NotImplementedError("Passo 1.3: Simulador.registrar")

    def tick(self) -> bool:
        # TODO Passo 1.3
        raise NotImplementedError("Passo 1.3: Simulador.tick")

    def run_until_stable(self, max_ticks: int = 100) -> int:
        # TODO Passo 1.3 (em caso de não-estabilização, lance OscilacaoDetectada)
        raise NotImplementedError("Passo 1.3: Simulador.run_until_stable")
