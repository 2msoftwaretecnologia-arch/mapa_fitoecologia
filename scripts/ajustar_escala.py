import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from buildkite.functions_pyautogui.funcoes_teclado_mouse import *
from scripts.comandos_basicos import *
from buildkite.interfaces.janelas_dinamicas import *
from database.requests import *


def ajustar_escala():

    refazer_escala = pyautogui.confirm(text="Deseja substituir a escala?", buttons=["sim", "não"])
    if refazer_escala == "sim":
        escala_coordenadas = request("get",objeto_id=10)
        if escala_coordenadas == (0,0):
            x_escala, y_escala = capturar_clique("clique em escala para eu saber onde fica")
            request("set",objeto_id=10,x=x_escala,y=y_escala)
            escala_coordenadas = request("get",objeto_id=10)
        else:
            esperar(0.3)
            click(escala_coordenadas[0],escala_coordenadas[1])
        clicar_centro_tela(1)
        fazer_novamente = None

        while fazer_novamente != "não":
            ajuste_escala = input_texto_dinamico(texto="digite sua escla\nse voce não digitar nada e confirmar com 'ok' ou 'enter'\nvamos confirmar que voce não quer mais ajustar\na escala")
            if ajuste_escala.strip() == "":
                fazer_novamente = "não"
            else:
                esperar(1)
                click(escala_coordenadas[0],escala_coordenadas[1])
                selecionar_tudo()
                escrever_texto(str(ajuste_escala))
                enter(1)
                limpar_area_transferencia()
                esperar(1.5)
                clicar_centro_tela(1)

