import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from buildkite.functions_pyautogui.mause_complexo import desenhar_quadrado
from buildkite.utils.info_arcgis import style_itens,position_squares,size_squares
from buildkite.functions_pyautogui.funcoes_teclado_mouse import KeyboardBasicFunctions
from buildkite.functions_pyautogui.arrows_keyboard import ArrowsKeyboard
from buildkite.functions_pyautogui.mause_complexo import click
from buildkite.Windows.manipular_windos import WAIT
from buildkite.interfaces.janelas_dinamicas import BRAKE_WINDOW
from database.requests import get_or_set_coordinate
from database.text_infos import Text_infos
from database.coordenadas import coordinates


def build_squares():
    BRAKE_WINDOW("espere o arcgis se normalizar e parte ok")
    current_style = style_itens()
    x_size_square,y_size_square = size_squares(Text_infos.requied_quantity_current_map)
    position_list = position_squares(Text_infos.requied_quantity_current_map)
    click(coordinates.x_blank_space,coordinates.y_blank_space,tempo=0.1)
    WAIT(0.5)
    rectangle_coordinates = get_or_set_coordinate(3,"Clique na seta do retangulo pra eu saber onde fica") #local que pega a forma geometrica  do retangulo
    square_coordinates = get_or_set_coordinate(4,"Clique em um lugar para desenhar o quadrado") #local que vai ser desenhado o quadrado
    for position,type in zip(position_list,Text_infos.current_items):
        click(rectangle_coordinates[0],rectangle_coordinates[1])
        KeyboardBasicFunctions._press_key('r')
        desenhar_quadrado(square_coordinates[0],square_coordinates[1],largura=80)
        WAIT(0.5)
        click(square_coordinates[0]+10,square_coordinates[1]+10,ammount_click=2)#aqui to colocando alguns pixels a mais pra ele conseguir clicar mais ou menos no centro do quadrado
        symbol_coordinates = get_or_set_coordinate(5,"Clique em 'symbol'")
        WAIT(0.2)
        click(symbol_coordinates[0],symbol_coordinates[1],tempo=0.1, ammount_click=3)
        fill_color_coordinates =  get_or_set_coordinate(6,"Clique em 'fill color'")
        click(symbol_coordinates[0],symbol_coordinates[1],tempo=0.1)
        click(fill_color_coordinates[0],fill_color_coordinates[1],tempo=0.1)
        ArrowsKeyboard()._press_up(2)
        WAIT(0.5)
        KeyboardBasicFunctions._press_enter()
        write_text(str(current_style[type][0]))
        KeyboardBasicFunctions._press_tab(wait_time=0.1)
        write_text(str(current_style[type][1]))
        KeyboardBasicFunctions._press_tab(wait_time=0.1)
        write_text(str(current_style[type][2]))
        KeyboardBasicFunctions._press_enter()
        outline_cordenadas =  get_or_set_coordinate(7,"Clique em 'fill color'")
        click(symbol_cordenadas[0],symbol_cordenadas[1],tempo=0.1)
        click(outline_cordenadas[0],outline_cordenadas[1],tempo=0.1)
        ArrowsKeyboard()._press_up(1)
        WAIT(0.5)
        KeyboardBasicFunctions._press_enter()
        KeyboardBasicFunctions._press_tab(wait_time=0.1)
        write_text("0,40")
        click(symbol_cordenadas[0],symbol_cordenadas[1],tempo=0.1, ammount_click=3)
        ArrowsKeyboard()._press_right(2)
        WAIT(0.5)
        KeyboardBasicFunctions._press_tab(wait_time=0.1)
        write_text(position[0])
        KeyboardBasicFunctions._press_tab(wait_time=0.1)
        write_text(position[1])
        KeyboardBasicFunctions._press_tab(wait_time=0.1)
        write_text(str(x_size_square))
        KeyboardBasicFunctions._press_tab(wait_time=0.1)
        write_text(str(y_size_square))
        WAIT(0.5)
        KeyboardBasicFunctions._press_enter()
