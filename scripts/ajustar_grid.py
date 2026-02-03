import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from buildkite.functions_pyautogui.funcoes_teclado_mouse import KeyboardBasicFunctions,ArcGISKeyboardFunctions
from buildkite.functions_pyautogui.mause_complexo import click ,click_center_screen
from buildkite.interfaces.janelas_dinamicas import BrakeWindow,dynamic_text_input
from buildkite.interfaces.simple_interface import simple_choices,operation_mode
from database.requests import get_or_set_coordinate
from buildkite.Windows.manipular_windos import WAIT



def set_grid():
    try:
        blank_space_coordinates = get_or_set_coordinate(2,"clique em um espaço vazio fora do mapa para eu saber onde fica")
        layers_coordinates = get_or_set_coordinate(1, "clique na camada")
        WAIT(0.3)
        build_grid = simple_choices(text="Deseja substituir o grid?", choices_buttons=["sim", "não"])
        while build_grid == 'sim':
            click_center_screen()
            KeyboardBasicFunctions._press_insert()
            WAIT(0.5)
            click(layers_coordinates[0],layers_coordinates[1])
            WAIT(0.5)
            ArcGISKeyboardFunctions._press_ctrl_home()
            WAIT(0.5)
            KeyboardBasicFunctions._press_enter()
            operation_mode(secod_option=lambda: BrakeWindow("espere a janela de propriedades abrir").show())
            operation_mode(secod_option=lambda: BrakeWindow(mensage='ATENÇÃO!!!, aperte no grid ate que ele fique embaixo antes de apertar Entendi').show())
            grid_coordinates = get_or_set_coordinate(8,"aperte no grid")
            WAIT(0.3)
            click(grid_coordinates[0] , grid_coordinates[1],ammount_click=3)
            KeyboardBasicFunctions._press_tab(5,wait_time=0.01)
            KeyboardBasicFunctions._press_enter()   
            
            WAIT(0.5)
            
            grid_eixo_x = dynamic_text_input("Digite o valor do grid (eixo X) lembrando\n que esse valor vai ser multiplicado por 100")
            grid_eixo_y = dynamic_text_input("Digite o valor do grid (eixo Y) lembrando\n que esse valor vai ser multiplicado por 100")
            
            KeyboardBasicFunctions._press_tab(1)
            grid_eixo_x = int(grid_eixo_x)*100
            grid_eixo_y = int(grid_eixo_y)*100
            KeyboardBasicFunctions._write_text(str(grid_eixo_x))
            KeyboardBasicFunctions._write_text(str(".000000"))
            WAIT(0.2)
            KeyboardBasicFunctions._press_tab(2)
            KeyboardBasicFunctions._write_text(str(grid_eixo_y))
            KeyboardBasicFunctions._write_text(str(".000000"))
            KeyboardBasicFunctions._press_enter()
            WAIT(0.5)
            KeyboardBasicFunctions._press_tab(2,wait_time=0.01)
            KeyboardBasicFunctions._press_enter()
            WAIT(0.5)
            click(blank_space_coordinates[0],blank_space_coordinates[1])
            build_grid = simple_choices(text="Deseja substituir o grid?", choices_buttons=["sim", "não"])
    except Exception as e:
        print(f"Erro ao ajustar o grid: {e}")