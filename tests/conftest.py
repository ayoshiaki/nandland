"""Adiciona o diretório raiz do esqueleto ao sys.path para que os testes
importem os módulos sem precisar de pacote/instalação."""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
