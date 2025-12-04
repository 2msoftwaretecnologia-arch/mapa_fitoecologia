import os
import sys
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(BASE_DIR)

# Scripts principais
from scripts.ajustar_grid import set_grid
from scripts.ajustar_escala import set_scale
from scripts.fazer_legenda_fitoecologias import fazer_parte_legenda
from scripts.ajustar_nota_Tecnica import fazer_nota_tencnica
from scripts.ajustar_quadrados import ajustar_quadrados_mapa
from scripts.ajustar_legendas_propriedade import set_info_property
from scripts.selecao_apr import select_apr
from scripts.salvar_mapa import salvar_mapas

# Interface e janelas
from buildkite.interfaces.janelas_dinamicas import BRAKE_WINDOW, confirmar_inicio, escolher_tipo_mapa
from buildkite.interfaces.initial_form import InitialForm
from buildkite.Windows.abrir_documentos import abrir_documento, caminho_atual_mapa, caminho_word_nota_tecnica

# Ajuste de monitores
from ajustar_monitores import verificar_resolucao


def main_flow():
    """Executa toda a automação na ordem correta."""
    BRAKE_WINDOW(mensage ='⚠️ ATENÇÃO: siga as instruções exibidas na tela com atenção.')
    BRAKE_WINDOW(mensage ='⚙️ Aguarde o carregamento completo dos documentos antes de prosseguir.')
    
    InitialForm().run()#inicializar o formulário
    select_apr()
    set_scale()
    set_grid()
    set_info_property()
    fazer_parte_legenda()
    ajustar_quadrados_mapa()
    fazer_nota_tencnica()
    #salvar_mapas()

# ==========================================
#           Execução principal                      
# ==========================================
if __name__ == "__main__":
    verificar_resolucao()
    
    if confirmar_inicio():
        tipo = escolher_tipo_mapa()
        caminho = caminho_atual_mapa()
        abrir_documento(caminho)
        abrir_documento(caminho_word_nota_tecnica)
        main_flow()
        print("✅ Processo concluído com sucesso.")
    else:
        print("❌ Processo cancelado pelo usuário.")