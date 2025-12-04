import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from buildkite.Windows.abrir_documentos import open_document,path_word
from scripts.ajustar_quadrados import Text_infos
from buildkite.interfaces.multiplas_opcoes import criar_interface_opcoes
from buildkite.functions_pyautogui.funcoes_teclado_mouse import (click_center_screen,open_page_margin_Word,select_all,write_text,
                                                                 select_all_in_Word,choose_font_in_Word,copy,paste,press_ctrl_end,press_tab,press_enter)
from buildkite.functions_pyautogui.mause_complexo import click
from buildkite.utils.info_arcgis import kind_maps_options
from buildkite.Windows.manipular_windos import WAIT
from buildkite.interfaces.janelas_dinamicas import BRAKE_WINDOW
from database.coordenadas import coordinates
from buildkite.functions_tkinter.interfaces import exit_checkbox
from database.requests import get_or_set_coordinate


def fazer_parte_legenda():
    Text_infos.current_items = criar_interface_opcoes(
        opcoes_disponiveis=kind_maps_options[Text_infos.kind_mapa]
    )
    Text_infos.requied_quantity_current_map = len(Text_infos.current_items)
    
    open_document(path_word)
    WAIT(0.5)
    click_center_screen()
    WAIT(0.5)
    open_page_margin_Word(4)
    #colocar a borda no word
    press_tab(3, wait_time=0.01)
    write_text("8,75")
    WAIT(0.3)
    press_enter(tempo=0.5)
    WAIT(1)

    #colocar a fonte da letra no word
    select_all_in_Word()
    choose_font_in_Word()
    write_text("Times New Roman")
    WAIT(0.3)
    press_enter(tempo=0.3)

    BRAKE_WINDOW("Faça a descrição do seu texto entre 1100 e 1200 caractes")
    exit_checkbox("Saída")
    click_center_screen()
    WAIT(0.2)
    select_all_in_Word()
    copy()
    WAIT(0.2)

    click(coordinates.x_arcgis,coordinates.y_arcgis)  # foca na janela do ArcGIS
    WAIT(0.5)
    
    
    click(coordinates.x_blank_space,coordinates.y_blank_space,tempo=0.1) # clica em um espaço em branco
    WAIT(0.5)
    paste()
    WAIT(1.5)
    click(coordinates.x_start_point,coordinates.y_start_point,button_side="right")#lugar no arcgis que as coisas vão quando são coladas
    WAIT(0.5)
    press_ctrl_end(tempo=0.2)
    press_enter()
    WAIT(0.5)
    BRAKE_WINDOW("Ative o 'preserve aspect radio' se estiver desativo")
    size_position_coordenadas = get_or_set_coordinate(11,"clique em 'size and position' pra eu entender como fica")
    coordinates.x_size_position = size_position_coordenadas[0]
    coordinates.y_size_position = size_position_coordenadas[1]
    WAIT(0.3)
    # "Size and Position"
    click(coordinates.x_size_position,coordinates.y_size_position, clicks_quant=3)
    press_tab(wait_time=0.1)
    write_text("22,9201 cm")
    press_tab(wait_time=0.1)
    write_text("4,3233 cm")
    press_tab(3, wait_time=0.1)
    write_text("6,475 cm")
    press_tab(wait_time=0.1)
    WAIT(0.3)
    select_all()
    write_text("7,6116 cm")
    press_enter(tempo=0.5)
