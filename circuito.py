"""Circuitos compostos e catálogo (Fase 3)."""

from __future__ import annotations

import copy
import json

from componentes import ComponenteLogico, PortaNand
from pinos import PinoEntrada, PinoSaida, PinoEntradaExterna


class CircuitoComposto(ComponenteLogico):
    def __init__(self):
        # TODO Passo 3.1
        raise NotImplementedError("Passo 3.1: CircuitoComposto.__init__")

    def avaliar(self) -> None:
        # TODO Passo 3.1
        raise NotImplementedError("Passo 3.1: CircuitoComposto.avaliar")

    def clonar(self) -> "CircuitoComposto":
        # TODO Passo 3.3
        raise NotImplementedError("Passo 3.3: CircuitoComposto.clonar")

    def pinos_saida_internos(self) -> list[PinoSaida]:
        # TODO Passo 3.1
        raise NotImplementedError("Passo 3.1: CircuitoComposto.pinos_saida_internos")

    def pinos_entrada_dict(self) -> dict[str, PinoEntrada]:
        return dict(self.pinos_entrada_externos)

    def pinos_saida_dict(self) -> dict[str, PinoSaida]:
        return dict(self.pinos_saida_externos)


class CatalogoCircuitos:
    PRIMITIVA = "NAND"

    def __init__(self):
        # TODO Passo 3.2
        raise NotImplementedError("Passo 3.2: CatalogoCircuitos.__init__")

    def registrar(self, nome: str, prototipo: ComponenteLogico) -> None:
        # TODO Passo 3.2
        raise NotImplementedError("Passo 3.2: CatalogoCircuitos.registrar")

    def instanciar(self, nome: str) -> ComponenteLogico:
        # TODO Passo 3.2
        raise NotImplementedError("Passo 3.2: CatalogoCircuitos.instanciar")

    def nomes(self) -> list[str]:
        # TODO Passo 3.2
        raise NotImplementedError("Passo 3.2: CatalogoCircuitos.nomes")

    # ---- Persistência (Passo 3.4) ----

    def salvar(self, caminho: str) -> None:
        # TODO Passo 3.4
        raise NotImplementedError("Passo 3.4: salvar")

    def carregar(self, caminho: str) -> None:
        # TODO Passo 3.4
        raise NotImplementedError("Passo 3.4: carregar")
