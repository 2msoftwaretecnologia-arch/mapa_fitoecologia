import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from buildkite.Windows.abrir_documentos import open_document,path_word
from buildkite.Windows.manipular_windos import WAIT
from buildkite.functions_pyautogui.funcoes_teclado_mouse import (click_center_screen,press_enter,write_text,press_tab,
                                                                 paste,select_all,press_ctrl_end,copy,choose_font_in_Word,
                                                                 open_page_margin_Word,select_all_in_Word,center_text_in_Word,
                                                                 press_ctrl_home)
from buildkite.functions_pyautogui.mause_complexo import click
from database.coordenadas import coordinates
from buildkite.utils.techinal_notes import get_techinal_note_text
from buildkite.interfaces.janelas_dinamicas import BRAKE_WINDOW


def build_techinal_note():
    text_note_techinical = get_techinal_note_text()


    open_document(path_word)
    BRAKE_WINDOW("espere o word abrir e aperte em OK")
    click_center_screen()
    WAIT(0.5)
    open_page_margin_Word(4)
    press_tab(3, wait_time=0.1)
    write_text('7,5')
    press_enter()
    WAIT(0.5)
    select_all_in_Word()
    WAIT(0.5)
    write_text(texto=text_note_techinical,velocidade=0.005)
    WAIT(0.2)
    press_ctrl_home()
    center_text_in_Word()
    select_all_in_Word()
    choose_font_in_Word()
    write_text("Times New Roman")
    press_enter()
    WAIT(0.5)
    copy()
    click(coordinates.x_arcgis,coordinates.y_arcgis)#clicando na janela do arggis
    WAIT(0.7)
    click(coordinates.x_blank_space,coordinates.y_blank_space,tempo=0.1)
    WAIT(0.3)
    paste()
    WAIT(1)
    click(coordinates.x_start_point,coordinates.y_start_point,botao='right')
    WAIT(0.6)
    press_ctrl_end()
    press_enter()
    WAIT(0.3)
    click(coordinates.x_size_position,coordinates.y_size_position, clicks_quant=3)
    press_tab(wait_time=0.1)
    write_text("0,4822 cm")
    press_tab(wait_time=0.1)
    write_text("0,1517 cm")
    press_tab(3,wait_time=0.1)
    write_text("6,3994 cm")
    press_tab(wait_time=0.4)
    select_all()
    write_text("3,7103 cm")
    press_enter(tempo=0.5)
