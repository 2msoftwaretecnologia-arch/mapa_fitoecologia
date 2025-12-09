import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from buildkite.functions_pyautogui.funcoes_teclado_mouse import KeyboardBasicFunctions
from buildkite.functions_pyautogui.arrows_keyboard import ArrowsKeyboard
from buildkite.functions_pyautogui.mause_complexo import click ,click_center_screen
from buildkite.interfaces.janelas_dinamicas import BRAKE_WINDOW,dynamic_text_input
from buildkite.interfaces.simple_interface import simple_choices
from database.requests import get_or_set_coordinate
from buildkite.Windows.manipular_windos import WAIT
from database.coordenadas import coordinates
import pyautogui

def set_grid():
    try:
        blank_space_coordinates = get_or_set_coordinate(2,"clique em um espaço vazio fora do mapa para eu saber onde fica")
        coordinates.x_blank_space = blank_space_coordinates[0]
        coordinates.y_blank_space = blank_space_coordinates[1]
        click_center_screen()
        WAIT(0.3)
        click(blank_space_coordinates[0],blank_space_coordinates[1])
        WAIT(1)
        build_grid = simple_choices(text_content="Deseja substituir o grid?", choices_buttons=["sim", "não"])
        while build_grid == 'sim':
            click_center_screen()
            KeyboardBasicFunctions._press_insert()
            click_center_screen()
            WAIT(0.5)
            click(button_side="right")
            WAIT(0.5)
            ArrowsKeyboard._press_up()
            KeyboardBasicFunctions._press_enter()
            
            BRAKE_WINDOW("espere a janela de propriedades abrir")
            BRAKE_WINDOW(mensagem='ATENÇÃO!!!, aperte no grid ate que ele fique embaixo antes de apertar Entendi')
            grid_coordinates = get_or_set_coordinate(8,"aperte no grid")
            WAIT(0.3)
            click(grid_coordinates[0] , grid_coordinates[1],ammount_click=3)
            KeyboardBasicFunctions._press_tab(5,tempo_espera=0.01)
            KeyboardBasicFunctions._press_enter()   
            
            WAIT(0.5)
            
            grid_atual = dynamic_text_input("Digite o valor do grid lembrando\n que esse valor vai ser multiplicado por 100")
            
            KeyboardBasicFunctions._press_tab(1)
            grid_atual = int(grid_atual)*100
            KeyboardBasicFunctions._write_text(str(grid_atual))
            KeyboardBasicFunctions._write_text(str(".000000"))
            WAIT(0.2)
            KeyboardBasicFunctions._press_tab(1)
            KeyboardBasicFunctions._write_text(str(grid_atual))
            KeyboardBasicFunctions._write_text(str(".000000"))
            KeyboardBasicFunctions._press_enter()
            WAIT(0.5)
            KeyboardBasicFunctions._press_tab(2,tempo_espera=0.01)
            KeyboardBasicFunctions._press_enter()
            WAIT(0.5)
            click(blank_space_coordinates[0],blank_space_coordinates[1])
            build_grid = pyautogui.confirm(text="Deseja substituir o grid?", buttons=["sim", "não"])
    except Exception as e:
        print(f"Erro ao ajustar o grid: {e}")