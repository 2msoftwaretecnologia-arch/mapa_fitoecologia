import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.manipular_arcgis.comandos_basicos import *



def janela_de_protecao():
    confirmacao = input_texto_dinamico("Essa e uma janla de proteção ao usuario\npor favor, digite 'pronto' para continuar")
    while confirmacao.lower() != "pronto":
        confirmacao = input_texto_dinamico("Essa e uma janla de proteção ao usuario\n, por favor, digite 'pronto' para continuar")