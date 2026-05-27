"""Componentes lógicos (Fase 2)."""

from __future__ import annotations
from abc import ABC, abstractmethod

from pinos import PinoEntrada, PinoSaida


class ComponenteLogico(ABC):
    """Interface comum a toda porta ou circuito."""

    @abstractmethod
    def avaliar(self) -> None:
        """Lê valor_atual das entradas e escreve valor_proximo nas saídas."""

    @abstractmethod
    def clonar(self) -> "ComponenteLogico":
        """Retorna nova instância equivalente, com pinos próprios."""

    def pinos_saida_internos(self) -> list[PinoSaida]:
        """Hook: lista todos os PinoSaida deste componente (recursivamente em
        circuitos compostos). Usado por Simulador.registrar."""
        return []

    def pinos_entrada_dict(self) -> dict[str, PinoEntrada]:
        """Mapa nome -> PinoEntrada (útil para persistência e GUI)."""
        return {}

    def pinos_saida_dict(self) -> dict[str, PinoSaida]:
        """Mapa nome -> PinoSaida (útil para persistência e GUI)."""
        return {}


class PortaNand(ComponenteLogico):
    def __init__(self):
        # TODO Passo 2.2
        raise NotImplementedError("Passo 2.2: PortaNand.__init__")

    def avaliar(self) -> None:
        # TODO Passo 2.3
        raise NotImplementedError("Passo 2.3: PortaNand.avaliar")

    def clonar(self) -> "PortaNand":
        # TODO Passo 2.4
        raise NotImplementedError("Passo 2.4: PortaNand.clonar")

    def pinos_saida_internos(self) -> list[PinoSaida]:
        # TODO Passo 2.5
        raise NotImplementedError("Passo 2.5: PortaNand.pinos_saida_internos")

    def pinos_entrada_dict(self) -> dict[str, PinoEntrada]:
        # TODO Passo 2.5 (opcional)
        raise NotImplementedError("Passo 2.5: PortaNand.pinos_entrada_dict")

    def pinos_saida_dict(self) -> dict[str, PinoSaida]:
        # TODO Passo 2.5 (opcional)
        raise NotImplementedError("Passo 2.5: PortaNand.pinos_saida_dict")
