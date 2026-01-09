import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.text_infos import Text_infos
from buildkite.Windows.manipular_windos import WAIT
from buildkite.functions_tkinter.interfaces import find_shp_file
from buildkite.functions_pyautogui.funcoes_teclado_mouse import KeyboardBasicFunctions,ArcGISKeyboardFunctions
from buildkite.functions_pyautogui.arrows_keyboard import ArrowsKeyboard                                                                 
from buildkite.manipular_textos.fast_formatter import format_path                                                                 
from buildkite.functions_pyautogui.mause_complexo import click, click_center_screen                                                                 
from buildkite.utils.helpers import find_aii,BrakeWindow
from database.requests import get_or_set_coordinate
from buildkite.utils.small_utils import kinds_maps


def select_apr():
    
    var_apr = find_shp_file("escolha o shp da apr")
    var_aii = find_aii(var_apr)
    var_apr = format_path(var_apr)
    var_aii = format_path(var_aii)
    Text_infos.caminho_mapa_atual = var_apr
    layers_coordinates = get_or_set_coordinate(objeto_id=1,mensagem="Clique na lista onde fica a Layer principal do mapa")
    click_center_screen()
    WAIT(0.2)
    click(layers_coordinates[0],layers_coordinates[1])
    WAIT(0.5)
    ArcGISKeyboardFunctions._press_ctrl_home()
    WAIT(0.5)
    ArrowsKeyboard._press_down()
    WAIT(0.2)
    KeyboardBasicFunctions._press_enter()
    WAIT(0.5)
    BrakeWindow("Espere a seleção ser concluída e aperte Entendi").show()
    source_cordenadas = get_or_set_coordinate(objeto_id=12,mensagem="Clique no botão 'Source'")
    click(source_cordenadas[0],source_cordenadas[1],ammount_click=3)
    WAIT(0.3)
    KeyboardBasicFunctions._press_tab(6,wait_time=0.01)
    KeyboardBasicFunctions._press_enter()
    BrakeWindow("Espere a seleção ser concluída e aperte Entendi").show()
    WAIT(0.3)
    path_input_codinator = get_or_set_coordinate(14,"Clique no campo onde digitamos o caminho do shp")
    WAIT(0.3)
    click(path_input_codinator[0],path_input_codinator[1])
    KeyboardBasicFunctions._write_text(var_apr,speed=0.002)
    KeyboardBasicFunctions._press_enter()
    WAIT(0.2)
    KeyboardBasicFunctions._press_tab(1)
    WAIT(0.2)
    KeyboardBasicFunctions._press_enter()
    WAIT(0.2)
    KeyboardBasicFunctions._press_key("f2",wait_time=0.4)
    KeyboardBasicFunctions._write_text(f'{Text_infos.property_name} - A.P.R',speed=0.002)
    KeyboardBasicFunctions._press_enter(wait_time=0.5)
    ArrowsKeyboard._press_down(ammount=2,wait_time=0.002)
    WAIT(0.2)
    KeyboardBasicFunctions._press_enter()
    WAIT(0.5)
    BrakeWindow("Espere a seleção ser concluída e aperte Entendi").show()
    click(source_cordenadas[0],source_cordenadas[1],ammount_click=3)
    WAIT(0.5)
    KeyboardBasicFunctions._press_tab(6,wait_time=0.01)
    KeyboardBasicFunctions._press_enter()
    WAIT(0.5)
    KeyboardBasicFunctions._write_text(var_aii,speed=0.002)
    KeyboardBasicFunctions._press_enter()
    WAIT(0.2)
    KeyboardBasicFunctions._press_tab(1)
    WAIT(0.2)
    KeyboardBasicFunctions._press_enter()
    WAIT(1)
    #modificando a camada de baixo
    if Text_infos.kind_mapa in kinds_maps:
        ArrowsKeyboard._press_down(ammount=10,wait_time=0.002)
    else:
        if Text_infos.kind_mapa == 'Fitoecologia':
            ArrowsKeyboard._press_down(ammount=18,wait_time=0.002)
    
    WAIT(0.2)
    KeyboardBasicFunctions._press_enter()
    BrakeWindow("Espere a seleção ser concluída e aperte Entendi").show()
    click(source_cordenadas[0],source_cordenadas[1],ammount_click=3)
    WAIT(0.5)
    KeyboardBasicFunctions._press_tab(6,wait_time=0.01)
    KeyboardBasicFunctions._press_enter()
    WAIT(1)
    KeyboardBasicFunctions._write_text(var_apr,speed=0.002)
    KeyboardBasicFunctions._press_enter()
    WAIT(0.2)
    KeyboardBasicFunctions._press_tab(1)
    WAIT(0.2)
    KeyboardBasicFunctions._press_enter()
    WAIT(0.2)
    KeyboardBasicFunctions._press_key("f2",wait_time=0.4)
    KeyboardBasicFunctions._write_text(f'{Text_infos.property_name} - A.P.R',speed=0.002)
    KeyboardBasicFunctions._press_enter(wait_time=0.5)
    ArrowsKeyboard._press_down(ammount=2,wait_time=0.002)
    WAIT(0.2)
    KeyboardBasicFunctions._press_enter()
    BrakeWindow("Espere a seleção ser concluída e aperte Entendi").show()
    click(source_cordenadas[0],source_cordenadas[1],ammount_click=3)
    WAIT(0.2)
    KeyboardBasicFunctions._press_tab(6,wait_time=0.01)
    KeyboardBasicFunctions._press_enter()
    WAIT(0.5)
    KeyboardBasicFunctions._write_text(var_aii,speed=0.002)
    KeyboardBasicFunctions._press_enter()
    WAIT(0.2)
    KeyboardBasicFunctions._press_tab(1)
    WAIT(0.2)
    KeyboardBasicFunctions._press_enter()
    WAIT(1)