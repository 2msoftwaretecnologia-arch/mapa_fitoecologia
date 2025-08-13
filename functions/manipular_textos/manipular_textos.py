import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

def adicionar_quebras_de_linha(texto, intervalo):
    resultado = []
    for i in range(0, len(texto), intervalo):
        parte = texto[i:i + intervalo]
        resultado.append(parte)
    return '\n'.join(resultado)

def sem_quebras(texto, intervalo):
    resultado = []
    i = 0
    while i < len(texto):
        # Pega o bloco do texto começando em i com tamanho 'intervalo'
        parte = texto[i:i + intervalo]
        
        # Se estamos no final do texto, adiciona e sai
        if i + intervalo >= len(texto):
            resultado.append(parte)
            break
            
        # Se o próximo caractere após o bloco é um espaço, podemos quebrar aqui
        if texto[i + intervalo] == ' ':
            resultado.append(parte)
            i += intervalo + 1  # +1 para pular o espaço
        else:
            # Encontra o último espaço dentro do bloco
            ultimo_espaco = parte.rfind(' ')
            
            if ultimo_espaco == -1:
                # Não há espaços, quebra no intervalo mesmo (quebra palavra)
                resultado.append(parte)
                i += intervalo
            else:
                # Quebra no último espaço
                parte_quebrada = parte[:ultimo_espaco]
                resultado.append(parte_quebrada)
                i += ultimo_espaco + 1  # +1 para pular o espaço
                
    return '\n'.join(resultado)

