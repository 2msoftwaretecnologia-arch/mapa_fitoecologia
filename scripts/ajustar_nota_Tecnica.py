import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from buildkite.Windows.abrir_documentos import open_document,path_word
from buildkite.Windows.manipular_windos import WAIT
from buildkite.functions_pyautogui.funcoes_teclado_mouse import KeyboardBasicFunctions,WordKeyboardFunctions,ArcGISKeyboardFunctions
from buildkite.functions_pyautogui.mause_complexo import click, click_center_screen, select_text_with_mouse
from database.coordenadas import coordinates
from database.requests import get_or_set_coordinate
from buildkite.utils.techinal_notes import get_techinal_note_text
from buildkite.interfaces.janelas_dinamicas import BrakeWindow
from buildkite.interfaces.simple_interface import  operation_mode


def build_techinal_note():
    blank_space_coordinates = get_or_set_coordinate(2,"clique em um espaço vazio fora do mapa para eu saber onde fica")
    start_point_coordinators = get_or_set_coordinate(9,"clique sobre texto")
    text_note_techinical = get_techinal_note_text()
    open_document(path_word)
    operation_mode(secod_option=lambda: BrakeWindow("espere o word abrir e aperte em OK").show())
    click_center_screen()
    WAIT(0.5)
    WordKeyboardFunctions._open_page_margin_Word(4)
    KeyboardBasicFunctions._press_tab(3, wait_time=0.1)
    KeyboardBasicFunctions._write_text('7,5')
    KeyboardBasicFunctions._press_enter()
    WAIT(0.5)
    WordKeyboardFunctions._select_all_in_Word()
    WAIT(0.5)
    KeyboardBasicFunctions._write_text(text=text_note_techinical,speed=0.005)
    WAIT(0.2)
    ArcGISKeyboardFunctions._press_ctrl_home()
    WordKeyboardFunctions._center_text_in_Word()
    coordinate_inicial_select_texto_with_mouse = get_or_set_coordinate(17,"clique sobre o texto inicial")
    coordinate_final_select_texto_with_mouse = get_or_set_coordinate(18,"clique sobre o texto final")
    select_text_with_mouse(
        x_inifical=coordinate_inicial_select_texto_with_mouse[0]
        ,y_inicial=coordinate_inicial_select_texto_with_mouse[1]
        ,x_final=coordinate_final_select_texto_with_mouse[0]
        ,y_final=coordinate_final_select_texto_with_mouse[1]
    )
    WordKeyboardFunctions._make_bold()
    WordKeyboardFunctions._select_all_in_Word()
    WordKeyboardFunctions._choose_font_in_Word()
    KeyboardBasicFunctions._write_text("Times New Roman")
    KeyboardBasicFunctions._press_enter()
    WAIT(0.5)
    KeyboardBasicFunctions._copy()
    click(coordinates.x_arcgis,coordinates.y_arcgis)#clicando na janela do arggis
    WAIT(0.7)
    click(blank_space_coordinates[0],blank_space_coordinates[1],wait_time=0.1)
    WAIT(0.3)
    KeyboardBasicFunctions._paste()
    WAIT(1)
    click(start_point_coordinators[0],start_point_coordinators[1],button_side='right')
    WAIT(0.6)
    ArcGISKeyboardFunctions._press_ctrl_end()
    KeyboardBasicFunctions._press_enter()
    WAIT(0.3)
    size_position_coordenadas = get_or_set_coordinate(11,"clique em size and position")
    click(size_position_coordenadas[0],size_position_coordenadas[1], ammount_click=3)
    KeyboardBasicFunctions._press_tab(wait_time=0.1)
    KeyboardBasicFunctions._write_text("0,4822 cm")
    KeyboardBasicFunctions._press_tab(wait_time=0.1)
    KeyboardBasicFunctions._write_text("0,1517 cm")
    KeyboardBasicFunctions._press_tab(3,wait_time=0.1)
    KeyboardBasicFunctions._write_text("6,3994 cm")
    KeyboardBasicFunctions._press_tab(wait_time=0.4)
    WordKeyboardFunctions._select_all_in_Word()
    KeyboardBasicFunctions._write_text("3,7103 cm")
    KeyboardBasicFunctions._press_enter(wait_time=0.5)
