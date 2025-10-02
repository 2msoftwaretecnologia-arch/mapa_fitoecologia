import json
from functions.manipular_windos.capturar_click import *


ARQUIVO = "config/coordinates.json"

def request(action: str, objeto_id: int, x: int = None, y: int = None, default=(0, 0)):
    """
    Função única para GET e SET de coordenadas em um JSON.

    Params:
        action (str): "get" ou "set"
        objeto_id (int): ID do objeto no JSON
        x (int): novo valor de X (obrigatório para SET)
        y (int): novo valor de Y (obrigatório para SET)
        default (tuple): valor retornado se não houver coordenadas
    """
    # Carregar dados
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        dados = json.load(f)

    # Procurar objeto
    for obj in dados["objetos"]:
        if obj["id"] == objeto_id:
            if action == "get":
                coords = obj.get("coordenadas")
                if coords is None:  # se não existe campo "coordenadas"
                    return default
                return (
                    coords.get("x", default[0]),
                    coords.get("y", default[1])
                )
            elif action == "set":
                if x is not None and y is not None:
                    if "coordenadas" not in obj:
                        obj["coordenadas"] = {}
                    obj["coordenadas"]["x"] = x
                    obj["coordenadas"]["y"] = y
                    with open(ARQUIVO, "w", encoding="utf-8") as f:
                        json.dump(dados, f, indent=4, ensure_ascii=False)
                    return {"status": "ok", "message": f"Coordenadas do objeto {objeto_id} atualizadas"}
                else:
                    return {"status": "erro", "message": "Para SET é necessário passar x e y"}
    
    return {"status": "erro", "message": f"Objeto {objeto_id} não encontrado"}


def get_or_set_coordinate(objeto_id: int, mensagem: str) -> tuple[int, int]:
    """Busca coordenada no JSON. Se não existir, captura clique e grava."""
    coords = request("get", objeto_id=objeto_id)
    if coords == (0, 0):
        x, y = capturar_clique(mensagem)
        request("set", objeto_id=objeto_id, x=x, y=y)
        coords = request("get", objeto_id=objeto_id)
    return coords