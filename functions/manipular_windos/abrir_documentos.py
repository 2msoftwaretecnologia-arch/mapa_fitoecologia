import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


caminho_word_nota_tecnica = r"C:\\Users\\Daniel Menezes\\Documents\\projeto-envimap\\mapa_fitoecologia\\documents\\nota_tecnica_formatacao.docx"
caminho_mapa_fitoecologia = r"C:\\Users\\Daniel Menezes\\Documents\\projeto-envimap\\tipos_mapas\\Mapa A4- Fitofisionomias.mxd"
caminho_mapa_geologia = r"C:\\Users\\Daniel Menezes\\Documents\\projeto-envimap\\tipos_mapas\\Mapa A4- Geofomologia.mxd"
def abrir_documento(documento):
    os.startfile(documento)