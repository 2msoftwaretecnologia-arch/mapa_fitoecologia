import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.interfaces.input_Texto_dinamico import *
from functions.interfaces.campo_dinamico_opcoes import *

from functions.pyaytogui.funcoes_teclado_mouse import * 
from functions.pyaytogui.mexer_mouse import * 
from functions.outras_funcoes.helpers import *
from functions.pyaytogui.localizacao import *
from functions.pyaytogui.protecao import *
from functions.pyaytogui.encontrar_cor import * 
from functions.manipular_arcgis.listar_camadas import *
from functions.manipular_arcgis.manipular_camadas import *
from functions.manipular_windos.manipular_windos import *
from functions.manipular_windos.capturar_click import *
from functions.manipular_windos.abrir_documentos import *
from functions.manipular_arcgis.comandos_basicos import *
from functions.manipular_textos.manipular_textos import *
from functions.outras_funcoes.coordenadas import *
from functions.manipular_arcgis.scritpts_leves import *
from functions.interfaces.alerta_simples import *


def fazer_nota_tencnica():
    fito_predominante = pyautogui.confirm(title="Fitofisionomia Predominante",text="Qual a fitofisionomia predominante da propriedade?",buttons=Text_infos.fito_ecologias)
    Text_infos.tipo_dominante = fito_predominante
    texto = f"""Nota Técnica

O mapa de Fitofisionomias da propriedade {Text_infos.nome_propriedade} detalha as formações vegetais da área, com destaque para a {Text_infos.tipo_dominante}.
Esses dados são fundamentais para o planejamento ambiental, regularização fundiária e ações de conservação. Os direitos autorais e a propriedade intelectual deste mapeamento pertencem à ENVIMAP. Qualquer uso, reprodução ou distribuição deste registro técnico deve ser devidamente referenciado e autorizado."""
    abrir_documento(caminho_word_nota_tecnica)
    janela_dinamica("espere o word abrir e aperte em OK")
    clicar_centro_tela()
    esperar(0.5)
    selecionar_tudo_Word()
    esperar(0.5)
    escrever_texto(texto,velocidade=0.005)
    apertar_ctrl_home()
    centralizar_texto_Word()
    selecionar_tudo_Word()
    escolher_fonte_Word()
    escrever_texto("Times New Roman")
    enter()
    esperar(0.5)
    copiar()
    click(coordinates.x_arcgis,coordinates.y_arcgis)#clicando na janela do arggis
    esperar(0.7)
    click(coordinates.x_espaco_Branco,coordinates.y_espaco_Branco,tempo=0.1)
    esperar(0.3)
    colar()
    esperar(1)
    click(coordinates.x_incio,coordinates.y_incio,botao='right')
    esperar(0.6)
    apertar_ctrl_end()
    enter()
    x_size_position,y_size_position = capturar_clique("clique em 'size and position' pra eu entender como fica")
    esperar(0.3)
    coordinates.x_size_position = x_size_position
    coordinates.y_size_position = y_size_position
    click(coordinates.x_arcgis,coordinates.y_arcgis,clicks_quant=3)
    apertar_Tab(tempo_espera=0.1)
    escrever_texto("0,4145")
    apertar_Tab(tempo_espera=0.1)
    escrever_texto("0,5287")
    apertar_Tab(3,tempo_espera=0.1)
    escrever_texto("6,5696")
    apertar_Tab(tempo_espera=0.1)
    esperar(0.3)
    selecionar_tudo()
    escrever_texto("3,1902")
    enter(tempo=0.5)