import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from buildkite.functions_pyautogui.funcoes_teclado_mouse import KeyboardBasicFunctions
from buildkite.functions_pyautogui.mause_complexo import click                                                           
from buildkite.interfaces.janelas_dinamicas import BrakeWindow
from buildkite.functions_tkinter.interfaces import ExitCheckboxWindow,select_folder
from buildkite.Windows.manipular_windos import WAIT
from database.requests import get_or_set_coordinate
from database.text_infos import Text_infos

def save_map():
    
    folder_save = select_folder(Text_infos.current_map_path)
    file_cordinates = get_or_set_coordinate(15,"Clique em 'file'")
    save_as_cordiantes = get_or_set_coordinate(20,"Clique em 'save as'")
    click(file_cordinates[0],file_cordinates[1])
    WAIT(0.2)
    click(save_as_cordiantes[0],save_as_cordiantes[1])
    WAIT(0.3)
    #click(input_fild_salvar_mxd_coordenadas[0],input_fild_salvar_mxd_coordenadas[1])
    KeyboardBasicFunctions._select_all(wait_time=0.3)
    KeyboardBasicFunctions._write_text(folder_save,speed=0.002)
    WAIT(0.2)
    if Text_infos.kind_mapa == 'Pedologia':
        KeyboardBasicFunctions._write_text("Mapa A4- Pedologia.mxd",speed=0.002)
    if Text_infos.kind_mapa == 'Geologia':
        KeyboardBasicFunctions._write_text("Mapa A4- Geofomologia.mxd",speed=0.002)
    if Text_infos.kind_mapa == 'Fitoecologia':
        KeyboardBasicFunctions._write_text("Mapa A4- Fitofisionomias.mxd",speed=0.002)
    if Text_infos.kind_mapa == 'Regioes_climaticas':
        KeyboardBasicFunctions._write_text("Mapa A4- Regioes Climaticas.mxd",speed=0.002)
    if Text_infos.kind_mapa == 'Declividade':
        KeyboardBasicFunctions._write_text("Mapa A4- Declividade.mxd",speed=0.002)
    if Text_infos.kind_mapa == 'Erodibilidade':
        KeyboardBasicFunctions._write_text("Mapa A4- Erodibilidade.mxd",speed=0.002)
    WAIT(0.5)
    KeyboardBasicFunctions._press_key("enter",ammount=2,wait_time=0.2)
    BrakeWindow("espere o globo no canto esquerdo finalizar e aperte ok").show()
    click(file_cordinates[0],file_cordinates[1])
    WAIT(0.2)
    export_map_coordinates = get_or_set_coordinate(21,"Clique em 'export map'")
    click(export_map_coordinates[0],export_map_coordinates[1])
    BrakeWindow("espere abrir e aperte ok").show()
    input_fild_save_pdf_jpeg_coordinators = get_or_set_coordinate(16,"Clique onde digita o caminho pra eu entender onde fica")
    click(input_fild_save_pdf_jpeg_coordinators[0],input_fild_save_pdf_jpeg_coordinators[1],ammount_click=3)   
    KeyboardBasicFunctions._select_all(wait_time=0.3)
    KeyboardBasicFunctions._write_text(folder_save,speed=0.002)        
    WAIT(0.2)
    if Text_infos.kind_mapa == 'Pedologia':
        KeyboardBasicFunctions._write_text("Mapa A4- Pedologia.jpg",speed=0.002)
    if Text_infos.kind_mapa == 'Geologia':
        KeyboardBasicFunctions._write_text("Mapa A4- Geofomologia.jpg",speed=0.002)
    if Text_infos.kind_mapa == 'Fitoecologia':
        KeyboardBasicFunctions._write_text("Mapa A4- Fitofisionomias.jpg",speed=0.002)
    if Text_infos.kind_mapa == 'Regioes_climaticas':
        KeyboardBasicFunctions._write_text("Mapa A4- Regioes Climaticas.jpg",speed=0.002)
    if Text_infos.kind_mapa == 'Declividade':
        KeyboardBasicFunctions._write_text("Mapa A4- Declividade.jpg",speed=0.002)
    if Text_infos.kind_mapa == 'Erodibilidade':
        KeyboardBasicFunctions._write_text("Mapa A4- Erodibilidade.jpg",speed=0.002)
    
    KeyboardBasicFunctions._press_key("tab",wait_time=0.1)
    KeyboardBasicFunctions._press_key("j",wait_time=0.3)
    KeyboardBasicFunctions._press_key("enter")
    BrakeWindow("espere o globo no canto esquerdo finalizar e aperte ok").show()
    click(file_cordinates[0],file_cordinates[1])
    WAIT(0.2)
    click(export_map_coordinates[0],export_map_coordinates[1])
    BrakeWindow("espere abrir e aperte ok").show()
    click(input_fild_save_pdf_jpeg_coordinators[0],input_fild_save_pdf_jpeg_coordinators[1],ammount_click=3)
    KeyboardBasicFunctions._select_all(wait_time=0.3)
    KeyboardBasicFunctions._write_text(folder_save,speed=0.002)
    WAIT(0.2)
    if Text_infos.kind_mapa == 'Pedologia':
        KeyboardBasicFunctions._write_text("Mapa A4- Fitofisionomias.pdf",speed=0.002)
    if Text_infos.kind_mapa == 'Geologia':
        KeyboardBasicFunctions._write_text("Mapa A4- Geofomologia.pdf",speed=0.002)
    if Text_infos.kind_mapa == 'Fitoecologia':
        KeyboardBasicFunctions._write_text("Mapa A4- Fitofisionomias.pdf",speed=0.002)
    if Text_infos.kind_mapa == 'Regioes_climaticas':
        KeyboardBasicFunctions._write_text("Mapa A4- Regioes Climaticas.pdf",speed=0.002)
    if Text_infos.kind_mapa == 'Declividade':
        KeyboardBasicFunctions._write_text("Mapa A4- Declividade.pdf",speed=0.002)
    if Text_infos.kind_mapa == 'Erodibilidade':
        KeyboardBasicFunctions._write_text("Mapa A4- Erodibilidade.pdf",speed=0.002)
    
    KeyboardBasicFunctions._press_key("tab",wait_time=0.1)
    KeyboardBasicFunctions._press_key("j",wait_time=0.2)
    KeyboardBasicFunctions._press_key("p",ammount=2,wait_time=0.2)
    KeyboardBasicFunctions._press_key("enter")
