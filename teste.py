import os


def esperar_aii(shp_path: str,) -> str:
    """
    Fica verificando até encontrar 'aii.shp' na mesma pasta do shapefile informado.

    Parâmetros:
        shp_path (str): Caminho de um shapefile qualquer.
        intervalo (int): Intervalo em segundos entre cada verificação. (default = 5)

    Retorna:
        str: Caminho completo do 'aii.shp' quando for encontrado.
    """
    pasta = os.path.dirname(shp_path)
    caminho_aii = os.path.join(pasta, "aii.shp")

    print(f"Aguardando o arquivo 'aii.shp' aparecer em: {pasta}")

    while not os.path.isfile(caminho_aii):
        print("o shp não esta")  # espera X segundos antes de checar de novo

    print("Arquivo encontrado:", caminho_aii)
    return caminho_aii



meu_shp = r"C:\Users\2mbet\Desktop\automacoes_envimap\shps\Propriedade\APR.shp"

print(esperar_aii(meu_shp))
