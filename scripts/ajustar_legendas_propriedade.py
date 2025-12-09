import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from buildkite.functions_pyautogui.funcoes_teclado_mouse import KeyboardBasicFunctions ,ArcGISKeyboardFunctions
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
        click(coordinates.x_blank_space,coordinates.y_blank_space,wait_time=0.1)
        WAIT(0.2)
        ArcGISKeyboardFunctions._create_text()
        WAIT(0.3)
        KeyboardBasicFunctions._select_all()
        KeyboardBasicFunctions._write_text(info)
        KeyboardBasicFunctions._press_enter(wait_time=0.5)
        start_point_coordinators = get_or_set_coordinate(9,"clique sobre texto para eu enteder onde fica")
        coordinates.x_start_point = start_point_coordinators[0]
        coordinates.y_start_point = start_point_coordinators[1]
        WAIT(0.3)
        click(coordinates.x_start_point,coordinates.y_start_point)
        WAIT(0.3)
        click(coordinates.x_blank_space,coordinates.y_blank_space,wait_time=0.1)
        WAIT(0.3)
        click(coordinates.x_start_point,coordinates.y_start_point,botao='right')
        WAIT(0.6)
        ArcGISKeyboardFunctions._press_ctrl_end()
        KeyboardBasicFunctions._press_enter(wait_time=0.5)
        BRAKE_WINDOW("espere abrir e aperte 'OK'")
        text_coordinators = get_or_set_coordinate(13,"clique em 'Text' pra eu entender como fica")
        WAIT(0.3)
        click(coordinates.x_start_point,coordinates.y_start_point,ammount_click=3)
        ArrowsKeyboard._press_right()
        KeyboardBasicFunctions._press_tab(wait_time=0.1)
        KeyboardBasicFunctions._write_text(position[0])
        KeyboardBasicFunctions._press_tab(wait_time=0.1)
        KeyboardBasicFunctions._write_text(position[1])
        KeyboardBasicFunctions._press_tab(3,wait_time=0.1)
        KeyboardBasicFunctions._write_text(position[2])
        KeyboardBasicFunctions._press_tab(wait_time=0.1)
        WAIT(0.3)
        KeyboardBasicFunctions._select_all()
        KeyboardBasicFunctions._write_text(position[3])
        KeyboardBasicFunctions._press_enter(wait_time=0.7)


    if len(Text_infos.city_uf) > 16:
        p1,p2 = quebrar_texto(Text_infos.city_uf,16,multi=False,duas_variaveis=True)
    click(coordinates.x_blank_space,coordinates.y_blank_space,wait_time=0.1)
    ArcGISKeyboardFunctions._create_text(wait_time=0.3)
    KeyboardBasicFunctions._select_all()
    if len(Text_infos.city_uf) > 16:
        KeyboardBasicFunctions._write_text(p1)
        pyautogui.hotkey("ctrl","enter")
        KeyboardBasicFunctions._write_text(p2)
    if len(Text_infos.city_uf) <= 16:
        KeyboardBasicFunctions._write_text(Text_infos.city_uf)
    KeyboardBasicFunctions._press_enter(wait_time=0.5)
    click(coordinates.x_blank_space,coordinates.y_blank_space,wait_time=0.1)
    WAIT(0.3)
    click(start_point_coordinators[0],start_point_coordinators[1],botao='right')
    WAIT(0.6)
    ArcGISKeyboardFunctions._press_ctrl_end()
    KeyboardBasicFunctions._press_enter(wait_time=0.5)  
    click(text_coordinators[0],text_coordinators[1],ammount_click=3)
    ArrowsKeyboard._press_right()
    if len(Text_infos.city_uf) > 16: 
        KeyboardBasicFunctions._press_tab(wait_time=0.1)
        KeyboardBasicFunctions._write_text("27,965")
        KeyboardBasicFunctions._press_tab(wait_time=0.1)
        KeyboardBasicFunctions._write_text("0,5747")
        KeyboardBasicFunctions._press_tab(3,wait_time=0.1)
        KeyboardBasicFunctions._write_text("1,4216")
        KeyboardBasicFunctions._press_tab(wait_time=0.1)
        WAIT(0.3)
        KeyboardBasicFunctions._select_all()
        KeyboardBasicFunctions._write_text("0,4778")
    if len(Text_infos.city_uf) <= 16:
        KeyboardBasicFunctions._press_tab(wait_time=0.1)
        KeyboardBasicFunctions._write_text("27,931")
        KeyboardBasicFunctions._press_tab(wait_time=0.1)
        KeyboardBasicFunctions._write_text("0,7082")
        KeyboardBasicFunctions._press_tab(3,wait_time=0.1)
        KeyboardBasicFunctions._write_text("0,9406")
        KeyboardBasicFunctions._press_tab(wait_time=0.1)
        WAIT(0.3)
        KeyboardBasicFunctions._select_all()
        KeyboardBasicFunctions._write_text("0,2344")
    KeyboardBasicFunctions._press_enter(wait_time=0.5)
