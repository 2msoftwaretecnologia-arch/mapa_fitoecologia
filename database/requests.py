import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ============================================================
# 🔧 IMPORTAÇÕES INTERNAS
# ============================================================
# Módulo que permite capturar um clique do usuário (X,Y)
from buildkite.Windows.capturar_click import *
# Objeto 'coordinates' com informações sobre a resolução atual
from database.coordenadas import *
import json


# ============================================================
# 🗂️ ARQUIVO DE BANCO DE DADOS JSON
# ============================================================
# Estrutura JSON multi-resolução, contendo para cada resolução
# (largura x altura) uma lista de objetos e suas coordenadas.
ARQUIVO = "database/coordinates.json"


def request(action: str, objeto_id: int, x: int = None, y: int = None, default=(0, 0)) -> dict | tuple:
    """
    ============================================================
    🧠 FUNÇÃO: request(action, objeto_id, x=None, y=None, default=(0,0))
    ============================================================

    📋 DESCRIÇÃO:
        Função genérica que gerencia a leitura e escrita de coordenadas
        de objetos em um arquivo JSON multi-resoluções.

        - Se `action == "get"` → busca coordenadas de um objeto.
        - Se `action == "set"` → grava novas coordenadas no JSON.

        Cada resolução de tela (largura x altura) tem seu próprio
        conjunto de objetos e coordenadas, permitindo que o sistema
        funcione corretamente em múltiplos monitores diferentes.

    ⚙️ PARÂMETROS:
        action (str):
            Tipo da operação. Pode ser:
            - `"get"` → buscar coordenadas salvas.
            - `"set"` → atualizar ou salvar novas coordenadas.

        objeto_id (int):
            Identificador único do objeto no JSON (ex: botão, campo, etc.).

        x (int, opcional):
            Valor da coordenada X (necessário apenas para SET).

        y (int, opcional):
            Valor da coordenada Y (necessário apenas para SET).

        default (tuple, opcional):
            Valor padrão retornado quando não há coordenadas registradas.
            Padrão: `(0, 0)`.

    🎯 RETORNA:
        - Para `"get"`: tupla `(x, y)` com as coordenadas encontradas.
        - Para `"set"`: dicionário com `status` e `message`.
        - Caso ocorra erro: dicionário informando o tipo do erro.

    💡 EXEMPLO DE USO:
        >>> request("get", objeto_id=1)
        (125, 370)

        >>> request("set", objeto_id=2, x=500, y=620)
        {'status': 'ok', 'message': 'Coordenadas do objeto 2 atualizadas em 1920x1080'}
    ============================================================
    """

    # Obtém a resolução atual da tela a partir do objeto coordinates
    largura = coordinates.largura_atual
    altura = coordinates.altura_atual

    # Carrega o arquivo JSON contendo as resoluções e objetos
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        dados = json.load(f)

    # ============================================================
    # 🔍 LOCALIZA A RESOLUÇÃO ATUAL DENTRO DO JSON
    # ============================================================
    resolucao = None
    for r in dados.get("resolucoes", []):
        if r.get("largura") == largura and r.get("altura") == altura:
            resolucao = r
            break

    # Se a resolução não estiver cadastrada no JSON
    if not resolucao:
        return {"status": "erro", "message": f"Resolução {largura}x{altura} não encontrada"}

    # ============================================================
    # 🔍 PROCURA O OBJETO DENTRO DESSA RESOLUÇÃO
    # ============================================================
    for obj in resolucao.get("objetos", []):
        if obj["id"] == objeto_id:

            # -----------------------------------
            # Modo GET → Retornar coordenadas
            # -----------------------------------
            if action == "get":
                coords = obj.get("coordenadas")
                if coords is None:
                    return default
                return (
                    coords.get("x", default[0]),
                    coords.get("y", default[1])
                )

            # -----------------------------------
            # Modo SET → Gravar novas coordenadas
            # -----------------------------------
            elif action == "set":
                if x is not None and y is not None:
                    if "coordenadas" not in obj:
                        obj["coordenadas"] = {}
                    obj["coordenadas"]["x"] = x
                    obj["coordenadas"]["y"] = y

                    # Salva alterações no arquivo JSON
                    with open(ARQUIVO, "w", encoding="utf-8") as f:
                        json.dump(dados, f, indent=4, ensure_ascii=False)

                    return {
                        "status": "ok",
                        "message": f"Coordenadas do objeto {objeto_id} atualizadas em {largura}x{altura}"
                    }

                # Caso falte X ou Y
                else:
                    return {"status": "erro", "message": "Para SET é necessário passar x e y"}

    # Caso o objeto não exista dentro da resolução atual
    return {"status": "erro", "message": f"Objeto {objeto_id} não encontrado na resolução {largura}x{altura}"}


def get_or_set_coordinate(objeto_id: int, mensagem: str) -> tuple[int, int]:
    """
    ============================================================
    🧠 FUNÇÃO: get_or_set_coordinate(objeto_id, mensagem)
    ============================================================

    📋 DESCRIÇÃO:
        Verifica se as coordenadas de um objeto estão salvas no JSON.
        Se não existirem (ou forem (0,0)), solicita que o usuário clique
        na tela para capturar as coordenadas e grava o resultado.

    ⚙️ PARÂMETROS:
        objeto_id (int):
            Identificador do objeto dentro do JSON.

        mensagem (str):
            Texto exibido na janela para orientar o usuário
            (ex: "Clique sobre o botão da legenda no ArcGIS").

    🎯 RETORNA:
        tuple[int, int]:
            As coordenadas (x, y) do objeto, obtidas do JSON ou capturadas
            em tempo real.

    💡 EXEMPLO DE USO:
        >>> get_or_set_coordinate(3, "Clique no canto superior do mapa.")
        (512, 410)
    ============================================================
    """

    # Tenta buscar as coordenadas já salvas
    coords = request("get", objeto_id=objeto_id)

    # Se ainda não existirem, solicita clique e salva no JSON
    if coords == (0, 0):
        x, y = capturar_clique(mensagem)
        request("set", objeto_id=objeto_id, x=x, y=y)
        coords = request("get", objeto_id=objeto_id)

    return coords
