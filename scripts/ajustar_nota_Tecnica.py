import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from buildkite.Windows.abrir_documentos import open_document,path_word
from buildkite.Windows.manipular_windos import WAIT
from buildkite.functions_pyautogui.funcoes_teclado_mouse import KeyboardBasicFunctions,WordKeyboardFunctions,ArcGISKeyboardFunctions
from buildkite.functions_pyautogui.mause_complexo import click, click_center_screen
from database.coordenadas import coordinates
from buildkite.utils.techinal_notes import get_techinal_note_text
from buildkite.interfaces.janelas_dinamicas import BRAKE_WINDOW


def build_techinal_note():
    text_note_techinical = get_techinal_note_text()
    open_document(path_word)
    BRAKE_WINDOW("espere o word abrir e aperte em OK")
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
    WordKeyboardFunctions._select_all_in_Word()
    WordKeyboardFunctions._choose_font_in_Word()
    KeyboardBasicFunctions._write_text("Times New Roman")
    KeyboardBasicFunctions._press_enter()
    WAIT(0.5)
    KeyboardBasicFunctions._copy()
    click(coordinates.x_arcgis,coordinates.y_arcgis)#clicando na janela do arggis
    WAIT(0.7)
    click(coordinates.x_blank_space,coordinates.y_blank_space,tempo=0.1)
    WAIT(0.3)
    KeyboardBasicFunctions._paste()
    WAIT(1)
    click(coordinates.x_start_point,coordinates.y_start_point,botao='right')
    WAIT(0.6)
    ArcGISKeyboardFunctions._press_ctrl_end()
    KeyboardBasicFunctions._press_enter()
    WAIT(0.3)
    click(coordinates.x_size_position,coordinates.y_size_position, ammount_click=3)
    KeyboardBasicFunctions._press_tab(wait_time=0.1)
    KeyboardBasicFunctions._write_text("0,4822 cm")
    KeyboardBasicFunctions._press_tab(wait_time=0.1)
    KeyboardBasicFunctions._write_text("0,1517 cm")
    KeyboardBasicFunctions._press_tab(3,wait_time=0.1)
    KeyboardBasicFunctions._write_text("6,3994 cm")
    KeyboardBasicFunctions._press_tab(wait_time=0.4)
    WordKeyboardFunctions._select_all_in_Word()
    KeyboardBasicFunctions._write_text("3,7103 cm")
    KeyboardBasicFunctions._press_enter(tempo=0.5)
