import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from buildkite.Windows.abrir_documentos import abrir_documento,caminho_word_nota_tecnica
from buildkite.Windows.manipular_windos import esperar
from buildkite.functions_pyautogui.funcoes_teclado_mouse import (clicar_centro_tela,enter,escrever_texto,apertar_Tab,click,
                                                                 colar,selecionar_tudo,apertar_ctrl_end,copiar,escolher_fonte_Word,
                                                                 abrir_margen_pagina_Word,selecionar_tudo_Word,centralizar_texto_Word,
                                                                 apertar_ctrl_home)
from database.text_infos import Text_infos
from database.coordenadas import coordinates
from buildkite.interfaces.janelas_dinamicas import janela_pausa
import pyautogui

def fazer_nota_tencnica():
    if Text_infos.tipo_mapa == 'Fitoecologia':
        fito_predominante = pyautogui.confirm(title="Fitofisionomia Predominante",text="Qual a fitofisionomia predominante da propriedade?",buttons=Text_infos.itens_atuais)
        Text_infos.tipo_dominante_fitoecologia = fito_predominante
        texto_nota_tecnica = f"""Nota Técnica

O mapa de Fitofisionomias da propriedade {Text_infos.nome_propriedade} detalha as formações vegetais da área, com destaque para a {Text_infos.tipo_dominante_fitoecologia}.
Esses dados são fundamentais para o planejamento ambiental, regularização fundiária e ações de conservação. Os direitos autorais e a propriedade intelectual deste mapeamento pertencem à ENVIMAP. Qualquer uso, reprodução ou distribuição deste registro técnico deve ser devidamente referenciado e autorizado."""
    
    if Text_infos.tipo_mapa == 'Geologia':
        geologia_predominante = pyautogui.confirm(title="Geologia Predominante",text="Qual a Geologia predominante da propriedade?",buttons=Text_infos.itens_atuais)
        Text_infos.tipo_dominante_geologia = geologia_predominante        
        texto_nota_tecnica= f"""Nota Técnica

O mapa geológico da propriedade {Text_infos.nome_propriedade} detalha as formações litológicas presentes na área, com destaque para a {Text_infos.tipo_dominante_geologia}.
Esses dados são fundamentais para o planejamento ambiental, regularização fundiária e ações de conservação. Os direitos autorais e a propriedade intelectual deste mapeamento pertencem à ENVIMAP. Qualquer uso, reprodução ou distribuição deste registro técnico deve ser devidamente referenciado e autorizado."""

    if Text_infos.tipo_mapa == 'Pedologia':
        pedologia_predominante = pyautogui.confirm(title="Pedologia Predominante",text="Qual a Pedologia predominante da propriedade?",buttons=Text_infos.itens_atuais)
        Text_infos.tipo_dominante_pedologia = pedologia_predominante
        texto_nota_tecnica= f"""Nota Técnica

O mapa pedológico da propriedade {Text_infos.nome_propriedade} detalha as formações solares presentes na área, com destaque para a {Text_infos.tipo_dominante_pedologia}.
Esses dados são fundamentais para o planejamento ambiental, regularização fundiária e ações de conservação. Os direitos autorais e a propriedade intelectual deste mapeamento pertencem à ENVIMAP. Qualquer uso, reprodução ou distribuição deste registro técnico deve ser devidamente referenciado e autorizado."""

    if Text_infos.tipo_mapa == 'Regioes_climaticas':
        regiao_climatica_predominante = pyautogui.confirm(title="Região Climática Predominante",text="Qual a Região Climática predominante da propriedade?",buttons=Text_infos.itens_atuais)
        Text_infos.tipo_dominante_regiao_climatica = regiao_climatica_predominante
        texto_nota_tecnica= f"""Nota Técnica 

O mapa de Regiões Climáticas da propriedade {Text_infos.nome_propriedade} detalha as regiões climáticas predominantes na área, com destaque para a {Text_infos.tipo_dominante_regiao_climatica}.
Esses dados são fundamentais para o planejamento ambiental, regularização fundiária e ações de conservação. Os direitos autorais e a propriedade intelectual deste mapeamento pertencem à ENVIMAP. Qualquer uso, reprodução ou distribuição deste registro técnico deve ser devidamente referenciado e autorizado."""

    if Text_infos.tipo_mapa == 'Declividade':
        declividade_predominante = pyautogui.confirm(title="Declividade Predominante",text="Qual a Declividade predominante da propriedade?",buttons=Text_infos.itens_atuais)
        Text_infos.tipo_dominante_declividade = declividade_predominante
        texto_nota_tecnica= f"""Nota Técnica

O mapa de Declividade da propriedade {Text_infos.nome_propriedade} detalha as declividades predominantes na área, com destaque para a {Text_infos.tipo_dominante_declividade}.
Esses dados são fundamentais para o planejamento ambiental, regularização fundiária e ações de conservação. Os direitos autorais e a propriedade intelectual deste mapeamento pertencem à ENVIMAP. Qualquer uso, reprodução ou distribuição deste registro técnico deve ser devidamente referenciado e autorizado."""

    abrir_documento(caminho_word_nota_tecnica)
    janela_pausa("espere o word abrir e aperte em OK")
    clicar_centro_tela()
    esperar(0.5)
    abrir_margen_pagina_Word(4)
    apertar_Tab(3, tempo_espera=0.1)
    escrever_texto('7,5')
    enter()
    esperar(0.5)
    selecionar_tudo_Word()
    esperar(0.5)
    escrever_texto(texto=texto_nota_tecnica,velocidade=0.005)
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
    click(coordinates.x_espaco_Branco,coordinates.y_espaco_Branco,tempo=0.1)
    esperar(0.3)
    colar()
    esperar(1)
    click(coordinates.x_ponto_incial,coordinates.y_ponto_incial,botao='right')
    esperar(0.6)
    apertar_ctrl_end()
    enter()
    esperar(0.3)
    click(coordinates.x_size_position,coordinates.y_size_position, clicks_quant=3)
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