import json

ARQUIVO = "config/coordinates.json"

def coordenadas(action: str, objeto_id: int, x: int = None, y: int = None, default=(0, 0)):
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

# Suponha que objeto 3 existe mas não tem "coordenadas"
teste = coordenadas("get", 3)

if teste == (0,0):
    print("deu certo")


"""# Saída: (0, 0)   ← veio o valor padrão

# Se quiser mudar o padrão pra None
print(coordenadas("get", 3, default=(None, None)))
# Saída: (None, None)

# Se depois você fizer SET
coordenadas("set", 3, 111, 222)
print(coordenadas("get", 3))
# Saída: (111, 222)


"""