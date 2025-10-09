"""
Módulo responsável por exibir o formulário inicial e capturar informações básicas
sobre a propriedade, além da posição de clique no ArcGIS.

Este módulo integra componentes de diferentes partes do projeto:
- Interface Tkinter para entrada de dados (janela de formulário)
- Função para capturar clique na tela (posição no ArcGIS)
- Módulos de dados globais (`Text_infos` e `coordinates`)

"""
import sys
import os

# Garante que a raiz do projeto esteja no sys.path para permitir imports como 'from buildkite...'
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

# Imports internos do projeto
from buildkite.interfaces.janela_input_propriedade import abrir_janela_input_propriedade
from buildkite.Windows.capturar_click import capturar_clique
from database.coordenadas import coordinates
from database.text_infos import Text_infos


def formulario_incial() -> None:
    """
    Exibe o formulário inicial para entrada de informações da propriedade e captura
    a posição de clique do ArcGIS.

    Esta função serve como ponto de partida para automações de mapas ou geração de relatórios,
    armazenando os dados coletados nas variáveis globais `Text_infos` e `coordinates`.

    Steps
    -----
    1. Abre a janela de formulário para o usuário preencher:
        - Nome da propriedade
        - Nome do proprietário
        - Matrícula
        - Cidade/UF
    2. Salva essas informações no objeto `Text_infos`.
    3. Solicita um clique no ArcGIS para capturar as coordenadas da tela.
    4. Armazena as coordenadas capturadas em `coordinates`.

    Returns
    -------
    None
        Não há retorno — os dados são gravados diretamente nas instâncias globais.

    Examples
    --------
    >>> formulario_incial()
    # (1) Janela de formulário é aberta.
    # (2) Usuário preenche os dados da propriedade.
    # (3) Script pede: "clique no ArcGIS pra eu saber onde fica".
    # (4) Após o clique, as informações são armazenadas em:
    #     Text_infos.nome_propriedade, Text_infos.proprietario, etc.
    #     coordinates.x_arcgis, coordinates.y_arcgis
    """
    # ===============================
    # 1. Abre janela de entrada Tkinter
    # ===============================
    campos = abrir_janela_input_propriedade()

    # ===============================
    # 2. Armazena os dados textuais
    # ===============================
    # Suporta cancelamento/fechamento da janela sem confirmar
    campos = campos or {}
    Text_infos.nome_propriedade = campos.get('nome_propriedade', '')
    Text_infos.proprietario = campos.get('proprietario', '')
    Text_infos.matricula = campos.get('matricula', '')
    Text_infos.cidade_uf = campos.get('cidade_uf', '')

    # ===============================
    # 3. Captura coordenadas via clique (ou simulação em modo de teste)
    # ===============================
    if os.getenv("FORM_INICIAL_TEST", "0") == "1":
        # Em modo de teste, gera coordenadas simuladas
        x_arcgis, y_arcgis = (123.45, 67.89)
    else:
        x_arcgis, y_arcgis = capturar_clique("Clique no ArcGIS para eu saber onde fica")

    # ===============================
    # 4. Armazena coordenadas globais
    # ===============================
    coordinates.x_arcgis = x_arcgis
    coordinates.y_arcgis = y_arcgis
