import os
import sys
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(BASE_DIR)

# Scripts principais
from scripts.ajustar_grid import set_grid
from scripts.ajustar_escala import set_scale
from scripts.fazer_legenda_fitoecologias import build_subtitle
from scripts.ajustar_nota_Tecnica import build_techinal_note    
from scripts.ajustar_quadrados import build_squares
from scripts.ajustar_legendas_propriedade import set_info_property
from scripts.selecao_apr import select_apr
from scripts.salvar_mapa import salvar_mapas
from database.text_infos import Text_infos

# Interface e janelas
from buildkite.interfaces.janelas_dinamicas import BrakeWindow
from buildkite.interfaces.initial_form import InitialForm
from buildkite.Windows.abrir_documentos import open_document, choose_kind_mapa, path_word
from buildkite.interfaces.simple_interface import simple_choices , operation_mode

# Ajuste de monitores
from ajustar_monitores import verificar_resolucao


def main_flow():
    """Executa toda a automação na ordem correta."""
    operation_mode(secod_option=lambda: BrakeWindow(mensage ='⚠️ ATENÇÃO: siga as instruções exibidas na tela com atenção.').show())
    operation_mode(secod_option=lambda: BrakeWindow(mensage ='⚙️ Aguarde o carregamento completo dos documentos antes de prosseguir.').show())
    
    InitialForm().run()
    select_apr()
    set_scale()
    set_grid()
    set_info_property()
    build_subtitle()
    build_squares()
    build_techinal_note()
    #salvar_mapas()

# ==========================================
#           Execução principal                      
# ==========================================
if __name__ == "__main__":
    type_operation = simple_choices(title="Escolha o modo de operação", choices_buttons=["rapido","normal"])
    Text_infos.operation_mode = type_operation
    verificar_resolucao()
    start = simple_choices(title="Início",text="Deseja começar o processo?",choices_buttons=["Sim", "Não"])
    if start == 'Sim':
        path_map = choose_kind_mapa()
        open_document(path_map)
        open_document(path_word)
        main_flow()
        print("✅ Processo concluído com sucesso.")
    else:
        print("❌ Processo cancelado pelo usuário.")