from database.requests import *
import pyautogui


camada_cordenadas = get_or_set_coordinate(objeto_id=1,mensagem="Clique na lista onde fica a Layer principal do mapa")
print(camada_cordenadas)
esperar(0.2)
#pyautogui.moveTo(camada_cordenadas[0],camada_cordenadas[1])