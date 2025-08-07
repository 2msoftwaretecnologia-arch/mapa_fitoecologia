import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.tkinter.input_Texto_dinamico import *
from functions.tkinter.campo_dinamico_opcoes import *
from functions.tkinter.alerta_dinamico import *
from functions.pyaytogui.funcoes_teclado_mouse import * 
from functions.pyaytogui.mexer_mouse import * 
from functions.outras_funcoes.helpers import *
from functions.pyaytogui.localizacao import *
from functions.pyaytogui.protecao import *
from configs.substituir_textos_config import *
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
from functions.tkinter.alerta_simples import *


def fazer_nota_tencnica():
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
    janela_dinamica("abra o arcgis")
    janela_de_protecao()
    clicar_centro_tela()
    esperar(0.5)
    colar()
    show_alert_dinamic("Va nas propriedades da legenda em\n'size and Position' e desative todas as checkbox")
    janela_de_protecao()
    x_random, y_random = capturar_clique("clique no eixo 'x' pra eu saber onde e")
    esperar(0.5)
    selecionar_tudo(tempo=0.5)
    escrever_texto('0,4987')
    apertar_Tab()
    escrever_texto('0,435')
    apertar_Tab(3,tempo_espera=0.1)
    escrever_texto('6,2787')
    apertar_Tab()
    escrever_texto('3,2552')
    enter()
    limpar_area_transferencia()










