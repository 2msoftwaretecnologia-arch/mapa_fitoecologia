import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


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
    

estilos_fitoecologias = {
    "Floresta Estacional" : [59 , 105 , 0],
    "Floresta Ombrófila Aberta" : [255 , 115, 0],
    "Floresta Ombrófila Densa" : [4 , 219 , 0],
    "Savana Gramíneo Lenhosa" : [255 , 235 , 168],
    "Savana Arborizada/Arbórea" : [255 ,192 , 168],
    "Savana Florestada" : [255 , 168 , 168],
    "Savana Parque" : [255 , 214 , 168],
    "Rio" : [168 , 214 , 255]
}

estilos_regioes_geologicas = {
    "Cráton Amazônico" : [112, 128, 144],
    "Faixa Brasília" : [70, 130, 180],
    "Grupo Bambuí" : [245, 222, 179],
    "Bacia do Parnaíba" : [205, 133, 63],
    "Coberturas Cenozóicas" : [218, 165, 32],
    "Província Aurífera" : [255, 215, 0],
    "Províncias de Níquel e Cromo" : [34, 139, 34],
    "Depósitos de Fosfato e Calcário" : [245, 245, 245]
}

limites_texto_informacoes = {
    "proprietario":29,
    "matricula":14,
    "cidade":17,
}



