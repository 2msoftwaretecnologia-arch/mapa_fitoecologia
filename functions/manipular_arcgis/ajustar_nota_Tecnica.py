import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.manipular_windos.abrir_documentos import *
from functions.manipular_arcgis.comandos_basicos import *
from outras_funcoes.outras_infos import *
from database.requests import *

def fazer_nota_tencnica():
    if Text_infos.tipo_mapa == 'Fitoecologia':
        fito_predominante = pyautogui.confirm(title="Fitofisionomia Predominante",text="Qual a fitofisionomia predominante da propriedade?",buttons=Text_infos.itens_atuais)
        Text_infos.tipo_dominante_fitoecologia = fito_predominante
        texto = f"""Nota Técnica

O mapa de Fitofisionomias da propriedade {Text_infos.nome_propriedade} detalha as formações vegetais da área, com destaque para a {Text_infos.tipo_dominante_fitoecologia}.
Esses dados são fundamentais para o planejamento ambiental, regularização fundiária e ações de conservação. Os direitos autorais e a propriedade intelectual deste mapeamento pertencem à ENVIMAP. Qualquer uso, reprodução ou distribuição deste registro técnico deve ser devidamente referenciado e autorizado."""
    
    if Text_infos.tipo_mapa == 'Geologia':
        geologia_predominante = pyautogui.confirm(title="Geologia Predominante",text="Qual a Geologia predominante da propriedade?",buttons=Text_infos.itens_atuais)
        Text_infos.tipo_dominante_geologia = geologia_predominante        
        texto= f"""Nota Técnica

O mapa geológico da propriedade {Text_infos.nome_propriedade} detalha as formações litológicas presentes na área, com destaque para a {Text_infos.tipo_dominante_geologia}.
Esses dados são fundamentais para o planejamento ambiental, regularização fundiária e ações de conservação. Os direitos autorais e a propriedade intelectual deste mapeamento pertencem à ENVIMAP. Qualquer uso, reprodução ou distribuição deste registro técnico deve ser devidamente referenciado e autorizado."""

    abrir_documento(caminho_word_nota_tecnica)
    janela_dinamica("espere o word abrir e aperte em OK")
    clicar_centro_tela()
    esperar(0.5)
    abrir_margen_pagina_Word(4)
    apertar_Tab(3, tempo_espera=0.1)
    escrever_texto('7,5')
    enter()
    esperar(0.5)
    selecionar_tudo_Word()
    esperar(0.5)
    escrever_texto(texto,velocidade=0.005)
    esperar(0.2)
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
    espaco_branco_coordenadas = get_or_set_coordinate(2,"aperte no espaço em branco pra eu saber onde fica")
    click(espaco_branco_coordenadas[0],espaco_branco_coordenadas[1],tempo=0.1)
    esperar(0.3)
    colar()
    esperar(1)
    ponto_incial_coordenadas = get_or_set_coordinate(9,"clique sobre texto para eu enteder onde fica")
    click(ponto_incial_coordenadas[0],ponto_incial_coordenadas[1],botao='right')
    esperar(0.6)
    apertar_ctrl_end()
    enter()
    esperar(0.3)
    size_position_coordenadas = get_or_set_coordinate(11,"clique em 'size and position' pra eu entender como fica")
    click(size_position_coordenadas[0],size_position_coordenadas[1], clicks_quant=3)
    apertar_Tab(tempo_espera=0.1)
    escrever_texto("0,4822 cm")
    apertar_Tab(tempo_espera=0.1)
    escrever_texto("0,1517 cm")
    apertar_Tab(3,tempo_espera=0.1)
    escrever_texto("6,3994 cm")
    apertar_Tab(tempo_espera=0.4)
    selecionar_tudo()
    escrever_texto("3,7103 cm")
    enter(tempo=0.5)