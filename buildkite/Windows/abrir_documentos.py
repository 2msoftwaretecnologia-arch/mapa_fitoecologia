from typing import Optional, Sequence
import pyautogui
from database.text_infos import Text_infos
import os

# ============================================================
# 🗂️ Caminhos fixos de arquivos usados pelo sistema
# ============================================================
# Esses caminhos apontam para documentos e modelos padrão
# utilizados no processo de automação de mapas e notas técnicas.

# 📄 Documento modelo da Nota Técnica
path_word = (
    r"C:\\Users\\V1CT0R\\Downloads\\softwares\\envimap\\mapa_fitoecologia\\documents\\nota_tecnica_formatacao.docx"
)
# 🗺️ Mapas em formato MXD (ArcGIS) — modelos base de layout
path_fitoecoclogia_map = (
    r"C:\\Users\\V1CT0R\\Downloads\\softwares\\envimap\\tipos_mapas\\Mapa A4- Fitofisionomias.mxd"
)
path_geologia_map = (
    r"C:\\Users\\V1CT0R\\Downloads\\softwares\\envimap\\tipos_mapas\\Mapa A4- Geofomologia.mxd"
)
path_pedologia_map = (
    r"C:\\Users\\V1CT0R\\Downloads\\softwares\\envimap\\tipos_mapas\\Mapa A4- Pedolgia.mxd"
)
path_regioes_climaticas_map = (
    r"C:\\Users\\V1CT0R\\Downloads\\softwares\\envimap\\tipos_mapas\\Mapa A4- Regioes_climaticas.mxd"
)
path_declividade_map = (
    r"C:\\Users\\V1CT0R\\Downloads\\softwares\\envimap\\tipos_mapas\\Mapa A4- Declividade.mxd"
)

path_erodibilidade_map = (
    r"C:\\Users\\V1CT0R\\Downloads\\softwares\\envimap\\tipos_mapas\\Mapa A4- Erodibilidade.mxd"
)

def choose_kind_mapa(
    opcoes: Sequence[str] = ("Fitoecologia", "Geologia","Pedologia","Regioes_climaticas","Declividade","Erodibilidade"),
    title: str = "Tipo de Mapa",
    text: str = "Qual o tipo do mapa?",
    definir_em_text_infos: bool = True,
) -> Optional[str]:
    """Abre o seletor, salva via setters e retorna o caminho do modelo do mapa."""
    tipo = pyautogui.confirm(title=title, text=text, buttons=list(opcoes))  # type: ignore
    if not tipo:
        return None
    if definir_em_text_infos:
        Text_infos.kind_mapa = tipo
    mapas = {
        "Fitoecologia": path_fitoecoclogia_map,
        "Geologia": path_geologia_map,
        "Pedologia": path_pedologia_map,
        "Regioes_climaticas": path_regioes_climaticas_map,
        "Declividade": path_declividade_map,
        "Erodibilidade": path_erodibilidade_map,
    }
    caminho = mapas.get(tipo)
    if caminho and definir_em_text_infos:
        Text_infos.current_map_path = caminho
    return caminho


def open_document(document: str) -> None:
    """
    ============================================================
    🧠 FUNÇÃO: open_document(document)  
    ============================================================

    📋 DESCRIÇÃO:
        Abre um arquivo local utilizando o programa padrão do Windows
        (Word, ArcMap, etc.), equivalente a clicar duas vezes no arquivo.

        É usada para abrir automaticamente:
        - Notas técnicas (.docx)
        - Mapas (.mxd)
        - Outros arquivos associados ao projeto

    ⚙️ PARÂMETROS:
        document (str):
            Caminho completo do arquivo a ser aberto.

    🎯 RETORNA:
        None (não há retorno).

    💡 EXEMPLO DE USO:
        open_document(path_word)
        # → Abre o Word com o modelo de Nota Técnica
    ============================================================
    """
    os.startfile(document)
