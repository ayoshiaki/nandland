"""Análise estatística de circuitos com map/filter/reduce.

Exercícios de nível intermediário. Cada função DEVE usar pelo menos uma das
funções `map`, `filter` ou `functools.reduce`. Loops `for` e compreensões
(list/set/dict comprehensions) NÃO são permitidos no corpo principal —
recursão é permitida e, em vários exercícios, necessária.

Os exercícios pressupõem as APIs do esqueleto:
    - CircuitoComposto.componentes_internos : list[ComponenteLogico]
    - CircuitoComposto.pinos_entrada_externos / pinos_saida_externos
    - ComponenteLogico.pinos_saida_internos() -> list[PinoSaida]
    - PinoSaida.conectados, valor_atual, valor_proximo
    - Simulador.saidas_a_registrar : list[PinoSaida]
    - CatalogoCircuitos.nomes() / instanciar(nome)

Para cada função: remova o `raise NotImplementedError` e escreva a
implementação. Os testes em `test_analise.py` indicam o comportamento
esperado.
"""

from __future__ import annotations

from componentes import ComponenteLogico, PortaNand
from circuito import CircuitoComposto, CatalogoCircuitos
from pinos import PinoSaida
from simulador import Simulador


def _filhos(circuito: ComponenteLogico) -> list[ComponenteLogico]:
    """Filhos diretos de um componente (vazio se for primitivo).

    Auxiliar fornecido — pode ser usado livremente nos exercícios.
    """
    return list(getattr(circuito, "componentes_internos", []))


# 1. ------------------------------------------------------------------
def contar_nands(circuito: ComponenteLogico) -> int:
    """Número total de PortaNand dentro de `circuito` (recursivo).

    Dica: combine `map` (recursão sobre os filhos) com `reduce` para somar.

    >>> contar_nands(PortaNand())
    1
    """
    raise NotImplementedError("Exercício 1: implemente usando map/reduce.")


# 2. ------------------------------------------------------------------
def tipos_de_componentes(circuito: ComponenteLogico) -> set[type]:
    """Conjunto de classes distintas presentes em `circuito` (recursivo).

    Dica: a união de conjuntos pode ser combinada via `reduce`.
    """
    raise NotImplementedError("Exercício 2: implemente usando map/reduce.")


# 3. ------------------------------------------------------------------
def fan_out_maximo(circuito: ComponenteLogico) -> int:
    """Maior fan-out (len(pino.conectados)) entre todos os PinoSaida do circuito.

    Retorne 0 se não houver pinos. Dica: `map` para extrair os fan-outs e
    `reduce` (ou `max`) para agregar.
    """
    raise NotImplementedError("Exercício 3: implemente usando map e reduce/max.")


# 4. ------------------------------------------------------------------
def pinos_ativos(simulador: Simulador) -> list[PinoSaida]:
    """PinoSaida cujo valor_atual é True após o último commit.

    Dica: `filter` sobre `simulador.saidas_a_registrar`.
    """
    raise NotImplementedError("Exercício 4: implemente usando filter.")


# 5. ------------------------------------------------------------------
def pinos_instaveis(simulador: Simulador) -> list[PinoSaida]:
    """PinoSaida cujo próximo valor difere do atual (mudariam no próximo tick).

    Dica: `filter` com uma comparação entre `valor_proximo` e `valor_atual`.
    """
    raise NotImplementedError("Exercício 5: implemente usando filter.")


# 6. ------------------------------------------------------------------
def taxa_de_atividade(simulador: Simulador) -> float:
    """Fração de PinoSaida com valor_atual True. 0.0 se não há pinos.

    Dica: `map` para converter cada pino em 0/1 e `reduce` para somar.
    """
    raise NotImplementedError("Exercício 6: implemente usando map/reduce.")


# 7. ------------------------------------------------------------------
def profundidade(circuito: ComponenteLogico) -> int:
    """Profundidade de aninhamento de CircuitoComposto.

    Primitivos retornam 0; um CircuitoComposto contendo apenas primitivas
    retorna 1; cada nível adicional incrementa o valor.

    Dica: recursão sobre os filhos, agregando com `reduce`/`max`.
    """
    raise NotImplementedError("Exercício 7: implemente usando map e reduce/max.")


# 8. ------------------------------------------------------------------
def histograma_por_tipo(circuito: ComponenteLogico) -> dict[str, int]:
    """{nome_da_classe: contagem} agregando recursivamente.

    Inclua o próprio circuito na contagem. Dica: `collections.Counter` é
    somável e funciona bem com `reduce`.
    """
    raise NotImplementedError("Exercício 8: implemente usando map/reduce.")


# 9. ------------------------------------------------------------------
def circuitos_que_usam(catalogo: CatalogoCircuitos, nome: str) -> list[str]:
    """Nomes de circuitos do catálogo que referenciam `nome` internamente.

    Um circuito A "usa" `nome` se, ao instanciá-lo, algum componente interno
    (em qualquer nível) for do tipo registrado em `catalogo` sob `nome`.
    O próprio `nome` deve ser excluído do resultado.

    Dica: combine `filter` (para descartar o próprio nome e selecionar quem
    contém o tipo) com uma busca recursiva auxiliar.
    """
    raise NotImplementedError("Exercício 9: implemente usando filter.")


# 10. -----------------------------------------------------------------
def relatorio(circuito: ComponenteLogico) -> dict:
    """Relatório consolidado reutilizando as funções anteriores.

    Deve retornar um dict com as chaves:
        "nands", "tipos", "fan_out_maximo", "profundidade", "histograma".
    """
    raise NotImplementedError("Exercício 10: monte o dict reutilizando as anteriores.")
