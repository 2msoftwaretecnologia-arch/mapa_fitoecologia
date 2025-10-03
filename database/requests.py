import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.outras_funcoes.coordenadas import *
from functions.manipular_windos.capturar_click import *
import json


ARQUIVO = "config/coordinates.json"

def request(action: str, objeto_id: int,x: int = None, y: int = None, default=(0, 0)):
    """
    Função única para GET e SET de coordenadas em um JSON multi-resoluções.

    Params:
        action (str): "get" ou "set"
        objeto_id (int): ID do objeto no JSON
        largura (int): largura da resolução
        altura (int): altura da resolução
        x (int): novo valor de X (obrigatório para SET)
        y (int): novo valor de Y (obrigatório para SET)
        default (tuple): valor retornado se não houver coordenadas
    """
    largura = coordinates.largura_atual
    altura = coordinates.altura_atual
    # Carregar dados
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        dados = json.load(f)

    # Procurar a resolução correspondente
    resolucao = None
    for r in dados.get("resolucoes", []):
        if r.get("largura") == largura and r.get("altura") == altura:
            resolucao = r
            break

    if not resolucao:
        return {"status": "erro", "message": f"Resolução {largura}x{altura} não encontrada"}

    # Procurar objeto dentro da resolução encontrada
    for obj in resolucao.get("objetos", []):
        if obj["id"] == objeto_id:
            if action == "get":
                coords = obj.get("coordenadas")
                if coords is None:
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
                    # salvar alterações
                    with open(ARQUIVO, "w", encoding="utf-8") as f:
                        json.dump(dados, f, indent=4, ensure_ascii=False)
                    return {"status": "ok", "message": f"Coordenadas do objeto {objeto_id} atualizadas em {largura}x{altura}"}
                else:
                    return {"status": "erro", "message": "Para SET é necessário passar x e y"}

    return {"status": "erro", "message": f"Objeto {objeto_id} não encontrado na resolução {largura}x{altura}"}


def get_or_set_coordinate(objeto_id: int, mensagem: str) -> tuple[int, int]:
    """Busca coordenada no JSON. Se não existir, captura clique e grava."""
    coords = request("get", objeto_id=objeto_id)
    if coords == (0, 0):
        x, y = capturar_clique(mensagem)
        request("set", objeto_id=objeto_id, x=x, y=y)
        coords = request("get", objeto_id=objeto_id)
    return coords