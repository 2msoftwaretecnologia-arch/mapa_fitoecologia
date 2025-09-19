import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.outras_funcoes.outras_infos import *

def tamano_quadrados(quantidade):
    
    if quantidade == 1:
        return "0,3745 cm" , "7,687 cm"
    if quantidade == 2:
        return "0,3745 cm" , "3,6106 cm"
    if quantidade == 3:
        return "0,3745 cm" , "2,3464 cm"
    if quantidade == 4:
        return "0,3745 cm" , "1,5012 cm"    

    

def posicao_quadrados(quantidade):
    if quantidade == 1:
        return [("22,2462 cm", "4,3233 cm")]
    
    if quantidade == 2:
        return [("22,3185 cm", "8,3997 cm"),("22,3185 cm","4,3233 cm")]
    
    if quantidade == 3:
        return [("22,3185 cm", "9,6639 cm"),("22,3185 cm","6,9771 cm"),("22,3185 cm","4,3233 cm")]
    
    if quantidade == 4:
        return [("22,3185 cm", "10,5091 cm"),("22,3185 cm","8,3997 cm"),("22,3185 cm","6,5792 cm"),("22,3185 cm","4,3233 cm")]
    

def estilos_atuais():
    if Text_infos.tipo_mapa == 'Fitoecologia':
            return {
                "Floresta Estacional" : [59 , 105 , 0],
                "Floresta Ombrófila Aberta" : [255 , 115, 0],
                "Floresta Ombrófila Densa" : [4 , 219 , 0],
                "Savana Gramíneo Lenhosa" : [255 , 235 , 168],
                "Savana Arborizada/Arbórea" : [255 ,192 , 168],
                "Savana Florestada" : [255 , 168 , 168],
                "Savana Parque" : [255 , 214 , 168],
                "Rio" : [168 , 214 , 255]
            }

    if Text_infos.tipo_mapa == 'Geologia':
        return {
            "Cabeceiras do Parnaíba": [0, 128, 255],  # Azul → nascentes / cabeceiras
            "Chapada das Mangabeiras": [139, 69, 19],  # Marrom → chapada rochosa
            "Chapadas e Planos do Rio Farinha": [160, 82, 45],
            "Chapadão Ocidental Baiano": [205, 133, 63],
            "Chapadões do Alto Parnaíba": [222, 184, 135],
            "Complexo Montanhoso Veadeiro - Arrái": [112, 128, 144],  # Cinza montanhoso
            "Depressão de Cristalândia": [244, 164, 96],  # Areia/baixa altitude
            "Depressão de Imperatriz": [210, 180, 140],
            "Depressão do Alto Tocantins": [233, 150, 122],
            "Depressão do Médio Tocantins": [255, 160, 122],
            "Depressão do Médio e Baixo Araguaia": [250, 128, 114],
            "Patamar de Porto Franco -- Fortaleza dos Nogueiras": [189, 183, 107],  # Tom seco/amarelo
            "Patamares das Mangabeiras": [184, 134, 11],
            "Patamares do Araguaia": [218, 165, 32],
            "Patamares do Chapadão Ocidental Baiano": [255, 215, 0],
            "Planalto Dissecado do Tocantins": [85, 107, 47],  # Verde oliva → vegetação dissecada
            "Planalto do Alto Tocantins -- Paranaíba": [34, 139, 34],  # Verde → vegetação
            "Planalto do Interflúvio Tocantins -- Araguaia": [0, 100, 0],
            "Planície do Araguaia -- Javaés": [135, 206, 235],  # Azul claro → planície alagável
            "Planícies Fluviais": [0, 191, 255],
            "Serra Malhada Alta": [105, 105, 105],  # Cinza rochoso
            "Serra da Natividade": [119, 136, 153],
            "Serras das Andorinhas -- Xambioá -- Lontras": [128, 128, 128],
            "Serras de Arraias e da Canoa": [169, 169, 169],
            "Serras de Santo Antônio -- João Damião": [192, 192, 192],
            "Vãos da Bacia do Alto Parnaíba": [72, 209, 204]  # Azul esverdeado → várzeas/vãos
        }

limites_texto_informacoes = {
    "proprietario":29,
    "matricula":14,
    "cidade":17,
}



Regioes_geologicas = [
    "Cabeceiras do Parnaíba",
    "Chapada das Mangabeiras",
    "Chapadas e Planos do Rio Farinha",
    "Chapadão Ocidental Baiano",
    "Chapadões do Alto Parnaíba",
    "Complexo Montanhoso Veadeiro - Arrái",
    "Depressão de Cristalândia",
    "Depressão de Imperatriz",
    "Depressão do Alto Tocantins",
    "Depressão do Médio Tocantins",
    "Depressão do Médio e Baixo Araguaia",
    "Patamar de Porto Franco -- Fortaleza dos Nogueiras",
    "Patamares das Mangabeiras",
    "Patamares do Araguaia",
    "Patamares do Chapadão Ocidental Baiano",
    "Planalto Dissecado do Tocantins",
    "Planalto do Alto Tocantins -- Paranaíba",
    "Planalto do Interflúvio Tocantins -- Araguaia",
    "Planície do Araguaia -- Javaés",
    "Planícies Fluviais",
    "Serra Malhada Alta",
    "Serra da Natividade",
    "Serras das Andorinhas -- Xambioá -- Lontras",
    "Serras de Arraias e da Canoa",
    "Serras de Santo Antônio -- João Damião",
    "Vãos da Bacia do Alto Parnaíba"
]

regioes_fitoecologias = ['Floresta Estacional', 'Floresta Ombrófila Aberta', 
                         'Floresta Ombrófila Densa', 'Savana Gramíneo Lenhosa', 
                         'Savana Arborizada/Arbórea', 'Savana Florestada', 
                         'Savana Parque', 'Rio']