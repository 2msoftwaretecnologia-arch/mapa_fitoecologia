import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from buildkite.interfaces.janelas_dinamicas import BrakeWindow
from database.requests import request
from mouseinfo import mouseInfo


def verificar_cordenadas():
    """
    Verifica as coordenadas dos botoes 'file', 'save as', 'export map'
    """

    file_cordinates = request('get',15)
    save_as_cordiantes = request('get',20)
    export_map_cordiantes = request('get',21)

    if any(coord == (0, 0) for coord in (file_cordinates, save_as_cordiantes, export_map_cordiantes)):
        BrakeWindow(mensage ='⚠️ ATENÇÃO: configure manualmente no arquivos jsn as cordenadas de id 15, 20 e 21.').show()
        mouseInfo()
        
    else:
        print("As coordenadas dos botoes 'file', 'save as', 'export map' foram verificadas com sucesso!")
        
