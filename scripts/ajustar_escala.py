import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from buildkite.functions_pyautogui.funcoes_teclado_mouse import KeyboardBasicFunctions
from buildkite.functions_pyautogui.mause_complexo import click,click_center_screen
from buildkite.interfaces.janelas_dinamicas import dynamic_text_input
from buildkite.interfaces.simple_interface import simple_choices
from buildkite.Windows.manipular_windos import WAIT , clear_clipboard
from database.requests import get_or_set_coordinate

def set_scale():

    do_scale = simple_choices(text="Deseja substituir a escala?",choices_buttons=["sim", "não"])
    if do_scale == "sim":
        scale_coordinator = get_or_set_coordinate(10,"clique em escala para eu saber onde fica")
        WAIT(0.3)
        click_center_screen()
        do_again = None

        while do_again != "não":
            set_scale_number = dynamic_text_input(message="digite sua escla\nse voce não digitar nada e confirmar com 'ok' ou 'enter'\nvamos confirmar que voce não quer mais ajustar\na escala")
            if set_scale_number.strip() == "":
                do_again = "não"
            else:
                WAIT(1)
                click(scale_coordinator[0],scale_coordinator[1])
                KeyboardBasicFunctions._select_all()
                KeyboardBasicFunctions._write_text(str(set_scale_number))
                KeyboardBasicFunctions._press_enter(1)
                clear_clipboard()
                WAIT(1.5)
                click_center_screen()