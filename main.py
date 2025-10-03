import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.manipular_arcgis.ajustar_grid import *
from functions.manipular_arcgis.ajustar_escala import *
from functions.manipular_arcgis.fazer_legenda_fitoecologias import *
from functions.manipular_arcgis.ajustar_nota_Tecnica import *
from functions.manipular_arcgis.ajustar_quadrados import *
from functions.manipular_arcgis.ajustar_legendas_propriedade import *
from functions.interfaces.alerta_simples import *
from functions.interfaces.formulario_inicial import *
from functions.manipular_arcgis.selecao_apr import *


#ver qual o monitor correto a se utilizar
from ajustar_monitores import *

# ============================
# Execução
# ============================
if __name__ == "__main__":
    largura_atual, altura_atual = pyautogui.size()
    coordinates.largura_atual = largura_atual
    coordinates.altura_atual = altura_atual
    dados = carregar_dados()

    # Verifica se já existe a resolução atual
    existe = any(r.get("largura") == largura_atual and r.get("altura") == altura_atual for r in dados["resolucoes"])

    if not existe:
        root = tk.Tk()
        app = App(root)
        root.mainloop()
    else:
        print(f"✅ Resolução atual {largura_atual}x{altura_atual} já está cadastrada. Interface não aberta.")

Fechar = pyautogui.confirm(title="Confirmação",text="começar??",buttons=["sim","Não"])
if Fechar == "sim":
    tipo_mapa = pyautogui.confirm(title="Confirmação",text="Qual o tipo do mapa?",buttons=["Fitoecologia","Geologia"])
    Text_infos.tipo_mapa = tipo_mapa                        
    

    if Text_infos.tipo_mapa == 'Fitoecologia':
        abrir_documento(caminho_mapa_fitoecologia)
    if Text_infos.tipo_mapa == 'Geologia':
        abrir_documento(caminho_mapa_geologia)

    abrir_documento(caminho_word_nota_tecnica)
    janela_dinamica(texto='ATENÇÃO!!!,\n se atente a todos as mensagens de texto que ira aparecer na sua tela')
    janela_dinamica(texto='ATENÇÃO!!!,\n espere carregar todos os documentos e depois aperte ok')
    formulario_incial()
    selecionar_apr()
    ajustar_escala()
    fazer_grid()
    ajustar_info_propriedade()
    fazer_parte_legenda()
    ajustar_quadrados_mapa()
    fazer_nota_tencnica()