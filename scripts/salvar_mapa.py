import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from buildkite.functions_pyautogui.funcoes_teclado_mouse import KeyboardBasicFunctions,ArcGISKeyboardFunctions
from buildkite.functions_pyautogui.mause_complexo import click_center_screen, click                                                           
from buildkite.interfaces.janelas_dinamicas import BrakeWindow
from buildkite.functions_tkinter.interfaces import ExitCheckboxWindow,select_folder
from buildkite.Windows.manipular_windos import WAIT
from database.requests import get_or_set_coordinate
from database.text_infos import Text_infos

def salvar_mapas():
    ExitCheckboxWindow().show()
    click_center_screen()
    ArcGISKeyboardFunctions._save_mxj(wait_time=1)
    folder_save = select_folder(Text_infos.caminho_mapa_atual)
    input_fild_salvar_mxd_coordenadas = get_or_set_coordinate(15,"Clique onde digita o caminho pra eu entender onde fica")
    blank_space_coordinates = get_or_set_coordinate(2,"clique em um espaço vazio fora do mapa para eu saber onde fica")
    click(blank_space_coordinates[0],blank_space_coordinates[1])
    WAIT(0.2)
    click(input_fild_salvar_mxd_coordenadas[0],input_fild_salvar_mxd_coordenadas[1])
    KeyboardBasicFunctions._select_all(wait_time=0.3)
    KeyboardBasicFunctions._write_text(folder_save,velocidade=0.002)
    WAIT(0.2)
    if Text_infos.kind_mapa == 'Pedologia':
        KeyboardBasicFunctions._write_text("Mapa A4- Fitofisionomias.mxd",velocidade=0.002)
    if Text_infos.kind_mapa == 'Geologia':
        KeyboardBasicFunctions._write_text("Mapa A4- Geofomologia.mxd",velocidade=0.002)
    if Text_infos.kind_mapa == 'Fitofisionomias':
        KeyboardBasicFunctions._write_text("Mapa A4- Fitofisionomias.mxd",velocidade=0.002)
    if Text_infos.kind_mapa == 'Regioes_climaticas':
        KeyboardBasicFunctions._write_text("Mapa A4- Regioes Climaticas.mxd",velocidade=0.002)
    if Text_infos.kind_mapa == 'Declividade':
        KeyboardBasicFunctions._write_text("Mapa A4- Declividade.mxd",velocidade=0.002)
    if Text_infos.kind_mapa == 'Erodibilidade':
        KeyboardBasicFunctions._write_text("Mapa A4- Erodibilidade.mxd",velocidade=0.002)
    KeyboardBasicFunctions._press_key("enter")
    WAIT(0.2)
    BrakeWindow("espere o globo no canto esquerdo finalizar e aperte ok").show()
    ArcGISKeyboardFunctions._save_mapa_export()
    BrakeWindow("espere abrir e aperte ok").show()
    input_fild_save_pdf_jpeg_coordinators = get_or_set_coordinate(16,"Clique onde digita o caminho pra eu entender onde fica")
    click(input_fild_save_pdf_jpeg_coordinators[0],input_fild_save_pdf_jpeg_coordinators[1],ammount_click=3)   
    KeyboardBasicFunctions._select_all(wait_time=0.3)
    KeyboardBasicFunctions._write_text(folder_save,velocidade=0.002)        
    WAIT(0.2)
    if Text_infos.kind_mapa == 'Pedologia':
        KeyboardBasicFunctions._write_text("Mapa A4- Fitofisionomias.jpg")
    if Text_infos.kind_mapa == 'Geologia':
        KeyboardBasicFunctions._write_text("Mapa A4- Geofomologia.jpg")
    if Text_infos.kind_mapa == 'Fitofisionomias':
        KeyboardBasicFunctions._write_text("Mapa A4- Fitofisionomias.jpg")
    if Text_infos.kind_mapa == 'Regioes_climaticas':
        KeyboardBasicFunctions._write_text("Mapa A4- Regioes Climaticas.jpg")
    if Text_infos.kind_mapa == 'Declividade':
        KeyboardBasicFunctions._write_text("Mapa A4- Declividade.jpg")
    if Text_infos.kind_mapa == 'Erodibilidade':
        KeyboardBasicFunctions._write_text("Mapa A4- Erodibilidade.jpg")
    
    KeyboardBasicFunctions._press_key("tab",wait_time_espera=0.1)
    KeyboardBasicFunctions._press_key("j",wait_time=0.3)
    KeyboardBasicFunctions._press_key("enter")
    BrakeWindow("espere o globo no canto esquerdo finalizar e aperte ok").show()
    ArcGISKeyboardFunctions._save_mapa_export()
    BrakeWindow("espere abrir e aperte ok").show()
    click(input_fild_save_pdf_jpeg_coordinators[0],input_fild_save_pdf_jpeg_coordinators[1],ammount_click=3)
    KeyboardBasicFunctions._select_all(wait_time=0.3)
    KeyboardBasicFunctions._write_text(folder_save,velocidade=0.002)
    WAIT(0.2)
    if Text_infos.kind_mapa == 'Pedologia':
        KeyboardBasicFunctions._write_text("Mapa A4- Fitofisionomias.pdf")
    if Text_infos.kind_mapa == 'Geologia':
        KeyboardBasicFunctions._write_text("Mapa A4- Geofomologia.pdf")
    if Text_infos.kind_mapa == 'Fitofisionomias':
        KeyboardBasicFunctions._write_text("Mapa A4- Fitofisionomias.pdf")
    if Text_infos.kind_mapa == 'Regioes_climaticas':
        KeyboardBasicFunctions._write_text("Mapa A4- Regioes Climaticas.pdf")
    if Text_infos.kind_mapa == 'Declividade':
        KeyboardBasicFunctions._write_text("Mapa A4- Declividade.pdf")
    if Text_infos.kind_mapa == 'Erodibilidade':
        KeyboardBasicFunctions._write_text("Mapa A4- Erodibilidade.pdf")
    
    KeyboardBasicFunctions._press_key("tab",wait_time_espera=0.1)
    KeyboardBasicFunctions._press_key("j",wait_time=0.2)
    KeyboardBasicFunctions._press_key("p",quantidade=2,wait_time=0.2)
    KeyboardBasicFunctions._press_key("enter")
