# ==========================================
# Imports organizados por responsabilidade
# ==========================================

# ==========================================
# Configurações de caminho dinâmico do projeto
# ==========================================
import os
import sys
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(BASE_DIR)

# Scripts principais
from scripts.ajustar_grid import fazer_grid
from scripts.ajustar_escala import ajustar_escala
from scripts.fazer_legenda_fitoecologias import fazer_parte_legenda
from scripts.ajustar_nota_Tecnica import fazer_nota_tencnica
from scripts.ajustar_quadrados import ajustar_quadrados_mapa
from scripts.ajustar_legendas_propriedade import ajustar_info_propriedade
from scripts.selecao_apr import selecionar_apr
from scripts.salvar_mapa import salvar_mapas

# Interface e janelas
from buildkite.interfaces.janelas_dinamicas import *
from buildkite.interfaces.formulario_inicial import formulario_incial
from buildkite.Windows.abrir_documentos import *

# Ajuste de monitores
from ajustar_monitores import *


def executar_fluxo_principal():
    """Executa toda a automação na ordem correta."""
    janela_pausa(mensagem ='⚠️ ATENÇÃO: siga as instruções exibidas na tela com atenção.')
    janela_pausa(mensagem ='⚙️ Aguarde o carregamento completo dos documentos antes de prosseguir.')
    
    formulario_incial()
    selecionar_apr()
    ajustar_escala()
    fazer_grid()
    ajustar_info_propriedade()
    fazer_parte_legenda()
    ajustar_quadrados_mapa()
    fazer_nota_tencnica()
    salvar_mapas()

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
        executar_fluxo_principal()
        print("✅ Processo concluído com sucesso.")
    else:
        print("❌ Processo cancelado pelo usuário.")