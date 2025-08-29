import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from configs.escala_config import *
from functions.interfaces.campo_dinamico_opcoes import *
from functions.pyaytogui.funcoes_teclado_mouse import * 
from functions.pyaytogui.mexer_mouse import * 
from functions.outras_funcoes.helpers import *
from functions.manipular_windos.manipular_windos import *
from functions.manipular_windos.capturar_click import *
from functions.manipular_arcgis.comandos_basicos import *
from functions.outras_funcoes.coordenadas import *
from functions.interfaces.alerta_simples import *


def ajustar_escala():
    
    esperar(1)
    clicar_centro_tela(1)
    insert(2)
    janela_dinamica("agora ajeitar a escala")
    texto_escala_padrao = escala_padrao()
    copiar_para_area_transferencia(texto_escala_padrao)
    esperar(1)
    abrir_console()
    janela_dinamica("verifique se o console está aberto, se não estiver, clique no botão de abrir console")
    click(x=coordinates.x_console_quadro, y=coordinates.y_console_quadro)
    apertar_ctrl_home()#apertando pra ele focar no console e não apertar duaz vezes
    esperar(0.5)
    colar()
    esperar(0.5)
    enter(3, tempo=0.1)
    limpar_area_transferencia()
    esperar(1)
    click(x=coordinates.fechar_console_x, y=coordinates.fechar_console_y)
    janela_dinamica("verifique se a janela do console fechou, se não fechou, clique no botão de fechar console")



    refazer_escala = pyautogui.confirm(text="Deseja substituir a escala?", buttons=["sim", "não"])
    if refazer_escala == "sim":
        x_escala, y_escala = capturar_clique("clique em escala para eu saber onde fica")
        coordinates.x_escala = x_escala
        coordinates.y_escala = y_escala
        clicar_centro_tela(1)
        numero_padrao = 25000  
        fazer_novamente = None

        while fazer_novamente != "não":
            ajuste_escala = pyautogui.confirm(text="Deseja aumentar ou diminuir a escala?", buttons=["Aumentar", "Diminiuir"])
            if ajuste_escala == "Aumentar":
                numero_padrao += 5000
            elif ajuste_escala == "Diminiuir":
                numero_padrao -= 5000

            texto = escala_padrao(numero_padrao)
            copiar_para_area_transferencia(texto)
            esperar(1)
            click(coordinates.x_escala, coordinates.y_escala)
            selecionar_tudo()
            escrever_texto(str(numero_padrao))
            enter(1)
            limpar_area_transferencia()
            esperar(1.5)
            clicar_centro_tela(1)
            fazer_novamente = pyautogui.confirm(text="Deseja substituir a escala?", buttons=["sim", "não"])

