import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


caminho_word_nota_tecnica = r'C:\\Users\\Daniel Menezes\\Documents\\projeto-envimap\\mapa_fitoecologia\\documents\\nota_tecnica_formatacao.docx'

def abrir_documento(documento):
    os.startfile(documento)