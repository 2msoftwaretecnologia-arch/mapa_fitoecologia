import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


caminho_word_nota_tecnica = r'C:\\Users\\USUARIO\\Desktop\\automacoes\\envimap\\mapa_fitofisionomia\\documents\\nota_tecnica_formatacao.docx'
caminho_word_ia = r'C:\\Users\\USUARIO\\Desktop\\automacoes\\mapa_fitoecologia_envimap\\documents\\text_com_ia_formatado.docx'

def abrir_documento(documento):
    os.startfile(documento)