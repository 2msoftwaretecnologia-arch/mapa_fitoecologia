import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from buildkite.functions_pyautogui.funcoes_teclado_mouse import press_enter,write_text,press_tab,press_ctrl_end,select_all,create_text
from buildkite.functions_pyautogui.mause_complexo import click
from buildkite.functions_pyautogui.arrows_keyboard import ArrowsKeyboard
from buildkite.manipular_textos.manipular_textos import quebrar_texto
from buildkite.interfaces.janelas_dinamicas import BRAKE_WINDOW
from buildkite.Windows.manipular_windos import WAIT
from buildkite.utils.info_arcgis import Positions_subtitles,property_infos
from database.text_infos import Text_infos
from database.coordenadas import coordinates
from database.requests import get_or_set_coordinate
import pyautogui

def set_info_property():
    for position,info in zip(Positions_subtitles,property_infos):        
        click(coordinates.x_espaco_Branco,coordinates.y_espaco_Branco,wait_time=0.1)
        WAIT(0.2)
        create_text()
        WAIT(0.3)
        select_all()
        write_text(info)
        press_enter(wait_time=0.5)
        ponto_incial_coordenadas = get_or_set_coordinate(9,"clique sobre texto para eu enteder onde fica")
        coordinates.x_start_point = ponto_incial_coordenadas[0]
        coordinates.y_start_point = ponto_incial_coordenadas[1]
        WAIT(0.3)
        click(coordinates.x_start_point,coordinates.y_start_point)
        WAIT(0.3)
        click(coordinates.x_espaco_Branco,coordinates.y_espaco_Branco,wait_time=0.1)
        WAIT(0.3)
        click(coordinates.x_start_point,coordinates.y_start_point,botao='right')
        WAIT(0.6)
        press_ctrl_end()
        press_enter(wait_time=0.5)
        BRAKE_WINDOW("espere abrir e aperte 'OK'")
        text_coordinators = get_or_set_coordinate(13,"clique em 'Text' pra eu entender como fica")
        WAIT(0.3)
        click(coordinates.x_start_point,coordinates.y_start_point,clicks_quant=3)
        ArrowsKeyboard._press_right()
        press_tab(wait_time=0.1)
        write_text(position[0])
        press_tab(wait_time=0.1)
        write_text(position[1])
        press_tab(3,wait_time=0.1)
        write_text(position[2])
        press_tab(wait_time=0.1)
        WAIT(0.3)
        select_all()
        write_text(position[3])
        press_enter(wait_time=0.7)


    if len(Text_infos.city_uf) > 16:
        p1,p2 = quebrar_texto(Text_infos.city_uf,16,multi=False,duas_variaveis=True)
    click(coordinates.x_blank_space,coordinates.y_blank_space,wait_time=0.1)
    create_text(wait_time=0.3)
    select_all()
    if len(Text_infos.city_uf) > 16:
        write_text(p1)
        pyautogui.hotkey("ctrl","enter")
        write_text(p2)
    if len(Text_infos.city_uf) <= 16:
        write_text(Text_infos.city_uf)
    press_enter(wait_time=0.5)
    click(coordinates.x_blank_space,coordinates.y_blank_space,wait_time=0.1)
    WAIT(0.3)
    click(ponto_incial_coordenadas[0],ponto_incial_coordenadas[1],botao='right')
    WAIT(0.6)
    press_ctrl_end()
    press_enter(wait_time=0.5)  
    click(text_coordinators[0],text_coordinators[1],clicks_quant=3)
    ArrowsKeyboard._press_right()
    if len(Text_infos.city_uf) > 16: 
        press_tab(wait_time=0.1)
        write_text("27,965")
        press_tab(wait_time=0.1)
        write_text("0,5747")
        press_tab(3,wait_time=0.1)
        write_text("1,4216")
        press_tab(wait_time=0.1)
        WAIT(0.3)
        select_all()
        write_text("0,4778")
    if len(Text_infos.city_uf) <= 16:
        press_tab(wait_time=0.1)
        write_text("27,931")
        press_tab(wait_time=0.1)
        write_text("0,7082")
        press_tab(3,wait_time=0.1)
        write_text("0,9406")
        press_tab(wait_time=0.1)
        WAIT(0.3)
        select_all()
        write_text("0,2344")
    press_enter(wait_time=0.5)
