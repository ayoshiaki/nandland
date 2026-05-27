"""Construtores de circuitos derivados (NOT, AND, SR_LATCH, D_LATCH,
D_FLIP_FLOP, REGISTRO_1BIT) -- todos a partir apenas de NAND.

Implementar nos Passos 3.1 (NOT) e 4.1-4.4.
Use popular_catalogo(cat) para registrar todos esses nomes num catálogo.
"""

from __future__ import annotations

from circuito import CatalogoCircuitos, CircuitoComposto
from pinos import PinoEntradaExterna, PinoSaida


def _semear(saida: PinoSaida, valor: bool) -> None:
    """Define o estado inicial de um PinoSaida e propaga para as entradas
    conectadas. Já pronto — não modifique.

    Use em `construir_sr_latch` e `construir_d_latch` para semear o laço SR
    em um estado assimétrico (Q=False, Q_BARRA=True). Sem isso, o latch
    começa em Q=Q_BARRA=False e, em modo HOLD (S=R=True), oscila
    indefinidamente entre (0,0) e (1,1), disparando OscilacaoDetectada."""
    saida.valor_atual = bool(valor)
    saida.valor_proximo = bool(valor)
    for e in saida.conectados:
        e.atualizar(valor)


def construir_not(cat: CatalogoCircuitos) -> CircuitoComposto:
    """Porta NOT: inversor lógico construído a partir de uma única NAND.
    Pino externo: IN; pino de saída: OUT."""
    # TODO Passo 3.1
    raise NotImplementedError("Passo 3.1: construir_not")


def construir_and(cat: CatalogoCircuitos) -> CircuitoComposto:
    """Porta AND. Pinos externos: A, B; pino de saída: OUT."""
    # TODO (extra)
    raise NotImplementedError("Extra: construir_and")


def construir_sr_latch(cat: CatalogoCircuitos) -> CircuitoComposto:
    """SR-latch (ativo em nível baixo). Pinos externos: S, R, Q, Q_BARRA.
    Lembre-se de inicializar o circuito num estado coerente (use _semear)
    para evitar oscilação no modo hold."""
    # TODO Passo 4.1
    raise NotImplementedError("Passo 4.1: construir_sr_latch")


def construir_d_latch(cat: CatalogoCircuitos) -> CircuitoComposto:
    """D-latch nível-sensível. Pinos externos: D, ENABLE, Q, Q_BARRA.
    Lembre-se de inicializar o estado interno coerentemente (use _semear)."""
    # TODO Passo 4.2
    raise NotImplementedError("Passo 4.2: construir_d_latch")


def construir_d_flip_flop(cat: CatalogoCircuitos) -> CircuitoComposto:
    """D flip-flop master-slave, sensível à borda de subida do clock.
    Pinos externos: D, CLK, Q."""
    # TODO Passo 4.3
    raise NotImplementedError("Passo 4.3: construir_d_flip_flop")


def construir_registro_1bit(cat: CatalogoCircuitos) -> CircuitoComposto:
    """Registrador de 1 bit. Pinos externos: D, CLK, Q."""
    # TODO Passo 4.4
    raise NotImplementedError("Passo 4.4: construir_registro_1bit")


def popular_catalogo(cat: CatalogoCircuitos) -> None:
    """Registra os circuitos derivados padrão no catálogo (chame após
    implementar os construtores acima)."""
    cat.registrar("NOT", construir_not(cat))
    cat.registrar("AND", construir_and(cat))
    cat.registrar("SR_LATCH", construir_sr_latch(cat))
    cat.registrar("D_LATCH", construir_d_latch(cat))
    cat.registrar("D_FLIP_FLOP", construir_d_flip_flop(cat))
    cat.registrar("REGISTRO_1BIT", construir_registro_1bit(cat))
