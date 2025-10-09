import sys
import os

# ============================================================
# 🔧 Ajuste do PATH para permitir imports relativos
# ============================================================
# Este trecho adiciona o diretório-pai ao sys.path, permitindo que
# módulos da pasta superior (ex: buildkite/interfaces) possam ser importados
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa a função personalizada 'janela_pausa'
from buildkite.interfaces.janelas_dinamicas import *


def esperar_aii(shp_path: str) -> str:
    """
    ============================================================
    🧠 FUNÇÃO: esperar_aii(shp_path)
    ============================================================

    📋 DESCRIÇÃO:
        Fica em modo de espera até que o arquivo **'aii.shp'**
        seja encontrado na mesma pasta do shapefile informado.

        Essa função é útil em fluxos de automação GIS (ex: ArcGIS, QGIS),
        onde o arquivo 'aii.shp' pode ser gerado por outro processo
        e o script precisa aguardar até sua criação.

        Enquanto o arquivo não for encontrado:
        → Abre uma janela interativa (janela_pausa)
          pedindo ao usuário para confirmar se o arquivo foi criado.

    ⚙️ PARÂMETROS:
        shp_path (str):
            Caminho absoluto de um shapefile existente (qualquer .shp).
            O script vai procurar o arquivo "aii.shp" na mesma pasta.

    🎯 RETORNA:
        str:
            Caminho completo do arquivo "aii.shp" assim que for encontrado.

    💡 EXEMPLO DE USO:
        caminho = esperar_aii("C:/Projetos/Fazenda_LuaBonita/lotes.shp")
        print(caminho)
        # Saída esperada:
        # "C:/Projetos/Fazenda_LuaBonita/aii.shp"

    ============================================================
    """

    # Extrai a pasta onde o shapefile original está localizado
    pasta = os.path.dirname(shp_path)

    # Define o caminho completo esperado para o arquivo "aii.shp"
    caminho_aii = os.path.join(pasta, "aii.shp")

    # Informa ao usuário que está aguardando o arquivo
    print(f"Aguardando o arquivo 'aii.shp' aparecer em: {pasta}")

    # ============================================================
    # 🔁 LOOP DE ESPERA
    # ============================================================
    # O loop continua até o arquivo "aii.shp" ser encontrado na pasta.
    # Em cada iteração, exibe uma janela pedindo confirmação manual.
    while not os.path.isfile(caminho_aii):
        # Chama a função janela_pausa (interface gráfica)
        # para alertar o usuário e solicitar que ele confirme quando o arquivo existir
        janela_pausa(
            "O 'AII.shp' não foi encontrado na pasta.\n"
            "Confirme se o nome está em CAIXA ALTA e se o arquivo está na pasta\n"
            "antes de clicar em 'OK'."
        )

    # Quando o arquivo for detectado, exibe mensagem e retorna o caminho completo
    print("✅ Arquivo encontrado:", caminho_aii)
    return caminho_aii
