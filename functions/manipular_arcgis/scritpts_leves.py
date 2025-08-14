import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.tkinter.input_Texto_dinamico import *
from functions.tkinter.campo_dinamico_opcoes import *
from functions.tkinter.formulario_inicial import *
from functions.pyaytogui.funcoes_teclado_mouse import * 
from functions.pyaytogui.mexer_mouse import * 
from functions.outras_funcoes.helpers import *
from functions.pyaytogui.localizacao import *
from functions.manipular_textos.manipular_textos import *
from configs.configs_apr import *
from configs.substuir_names_config import *
from functions.pyaytogui.encontrar_cor import * 
from functions.manipular_arcgis.listar_camadas import *
from functions.manipular_arcgis.manipular_camadas import *
from functions.manipular_arcgis.comandos_basicos import *
from functions.manipular_arcgis.helpers_arcgis import *
from functions.manipular_windos.manipular_windos import *
from functions.manipular_windos.capturar_click import *
from functions.outras_funcoes.coordenadas import *
from functions.tkinter.alerta_simples import *


def colar_scripts():
    formulario_incial()
    esperar(1)
    clicar_centro_tela(1)
    insert(2)
    janela_dinamica("agora vou colar os scripts mais basicos e leves")
    nome_proprietario_repartido = quebrar_texto(Text_infos.proprietario,29)
    cidade_repartida = quebrar_texto(Text_infos.proprietario,17)
    texto_apr = texto_config_Apr(Text_infos.nome_propriedade)
    texto_info_propriedade = texto_substituir_nomes(
        nome_proprietario_repartido,
        Text_infos.matricula,
        cidade_repartida
        )
    textos_para_colar = [texto_apr,texto_info_propriedade]
    esperar(1)
    abrir_console()
    #janela_dinamica("verifique se o console está aberto, se não estiver, clique no botão de abrir console")
    x_janela_python, y_janela_python = capturar_clique("clique na janela do python para eu saber onde é a janela")
    coordinates.x_console_quadro = x_janela_python
    coordinates.y_console_quadro = y_janela_python
    for texto in textos_para_colar:
        copiar_para_area_transferencia(texto)
        apertar_ctrl_end()
        esperar(0.5)
        colar()
        esperar(0.5)
        enter(3, tempo=0.1)
        limpar_area_transferencia()
        #janela_dinamica("verifique se o texto foi colado corretamente, se não foi, aperte ctrl + v")
        click(x=coordinates.x_console_quadro, y=coordinates.y_console_quadro)

    x_fechar_console, y_fechar_console = capturar_clique("clique em fechar console pra eu saber onde fica!")
    coordinates.fechar_console_x = x_fechar_console
    coordinates.fechar_console_y = y_fechar_console
    click(x=coordinates.fechar_console_x, y=coordinates.fechar_console_y)
    #janela_dinamica("verifique se a janela do console fechou, se não fechou, clique no botão de fechar console")



    