import sys
import os

# Garante que a raiz do projeto esteja no sys.path para permitir imports como 'from buildkite...'
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

# Imports internos do projeto
from buildkite.interfaces.build.build_initial_form import PropertyInfosWindowBuild    
from buildkite.Windows.capturar_click import capturar_clique
from database.coordenadas import coordinates



class InitialForm:
    """
    Exibe o formulário inicial para entrada de informações da propriedade e captura
    a posição do clique no ArcGIS.

    Esta classe serve como ponto de partida para automações de mapas ou geração de relatórios,
    armazenando os dados coletados nas variáveis globais `Text_infos` e `coordinates`.

    Passos
    -----
    1. Abre a janela do formulário para o usuário preencher:
        - Nome da propriedade
        - Nome do proprietário
        - Matrícula
        - Cidade/UF
    2. Salva essas informações no objeto `Text_infos`.
    3. Solicita um clique no ArcGIS para capturar as coordenadas da tela.
    4. Armazena as coordenadas capturadas em `coordinates`.

    Exemplos
    --------
    >>> InitialForm.run()
    # (1) A janela do formulário abre.
    # (2) O usuário preenche os dados da propriedade.
    # (3) O script solicita: "Clique na janela do ArcGIS para que eu saiba onde fica".
    # (4) Após o clique, as informações são armazenadas em:
    #     Text_infos.nome_propriedade, Text_infos.proprietario, etc.
    #     coordinates.x_arcgis, coordinates.y_arcgis
    """

    @staticmethod
    def run() -> None:
        """
        Executes the form workflow.

        Returns
        -------
        None
            No return — data is written directly to global instances.
        """
        print("abriu a janela de entrada Tkinter")
        form = PropertyInfosWindowBuild()
        form.open()
    
        # ===============================
        # 3. Captura coordenadas via clique (ou simulação em modo teste)
        # ===============================
        x_arcgis, y_arcgis = InitialForm._get_arcgis_coordinates()
        print("pegou as coordenadas do arcgis")
        # ===============================
        # 4. Armazena coordenadas globais
        # ===============================
        InitialForm._save_arcgis_coordinates(x_arcgis, y_arcgis)

    # ----------------------------------------------------------
    # Métodos auxiliares (separados para melhor organização)
    # ----------------------------------------------------------

    

    @staticmethod
    def _get_arcgis_coordinates() -> tuple[float, float]:
        """Captura coordenadas via clique ou gera valores simulados em modo teste."""
        return capturar_clique("clique na janela do arcgis para eu saber onde fica")

    @staticmethod
    def _save_arcgis_coordinates(x: float, y: float) -> None:
        """Armazena as coordenadas capturadas no objeto global coordinates."""
        coordinates.x_arcgis = x
        coordinates.y_arcgis = y
