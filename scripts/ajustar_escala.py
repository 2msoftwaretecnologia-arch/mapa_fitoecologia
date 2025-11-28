import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from buildkite.functions_pyautogui.funcoes_teclado_mouse import click_center_screen,click, selecionar_tudo, escrever_texto, enter
from buildkite.interfaces.janelas_dinamicas import input_texto_dinamico
from buildkite.Windows.manipular_windos import esperar , limpar_area_transferencia
from database.requests import get_or_set_coordinate
import pyautogui

def ajustar_escala():

    refazer_escala = pyautogui.confirm(text="Deseja substituir a escala?", buttons=["sim", "não"])
    if refazer_escala == "sim":
        escala_coordenadas = get_or_set_coordinate(10,"clique em escala para eu saber onde fica")
        esperar(0.3)
        click_center_screen()
        fazer_novamente = None

        while fazer_novamente != "não":
            ajuste_escala = input_texto_dinamico(mensagem="digite sua escla\nse voce não digitar nada e confirmar com 'ok' ou 'enter'\nvamos confirmar que voce não quer mais ajustar\na escala")
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
                click_center_screen()

