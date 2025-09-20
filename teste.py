def calcular_linhas_word(texto, margem_direita_cm, margem_esquerda_cm=3.0, 
                         largura_pagina_cm=21.0, fonte_tamanho=11, fonte_nome="Times New Roman"):
    """
    Calcula o número aproximado de linhas que um texto ocupará no Word com fonte Times New Roman 11.
    
    Parâmetros:
    texto (str): Texto a ser analisado
    margem_direita_cm (float): Margem direita em centímetros (pode ser decimal)
    margem_esquerda_cm (float): Margem esquerda em centímetros (padrão 3.0cm)
    largura_pagina_cm (float): Largura total da página (padrão A4 = 21.0cm)
    fonte_tamanho (int): Tamanho da fonte em pontos (padrão 11)
    fonte_nome (str): Nome da fonte (padrão "Times New Roman")
    
    Retorna:
    int: Número aproximado de linhas
    """
    # Fatores de conversão
    CM_POR_POLEGADA = 2.54
    PONTOS_POR_POLEGADA = 72
    
    # Fatores específicos para Times New Roman (empiricamente determinados)
    if fonte_nome.lower() == "times new roman":
        if fonte_tamanho == 11:
            # Para Times New Roman 11, aproximadamente 2.7 caracteres por centímetro
            CARACTERES_POR_CM = 2.7
        else:
            # Fórmula geral para Times New Roman
            CARACTERES_POR_CM = 2.7 * (11 / fonte_tamanho)
    else:
        # Valor padrão para outras fontes
        CARACTERES_POR_CM = 2.5
    
    # Calcula a largura útil da página
    largura_util_cm = largura_pagina_cm - margem_esquerda_cm - margem_direita_cm
    
    # Calcula caracteres por linha
    caracteres_por_linha = int(largura_util_cm * CARACTERES_POR_CM)
    
    # Divide o texto em palavras
    palavras = texto.split()
    linhas = []
    linha_atual = []
    
    # Quebra o texto em linhas considerando o limite de caracteres
    for palavra in palavras:
        # Testa se a palavra cabe na linha atual
        linha_teste = ' '.join(linha_atual + [palavra])
        
        if len(linha_teste) <= caracteres_por_linha:
            linha_atual.append(palavra)
        else:
            if linha_atual:
                linhas.append(' '.join(linha_atual))
            linha_atual = [palavra]
    
    # Adiciona a última linha se houver conteúdo
    if linha_atual:
        linhas.append(' '.join(linha_atual))
    
    return len(linhas)

# Função auxiliar para exibir resultados detalhados
def detalhar_calculo(texto, margem_direita, margem_esquerda=3.0):
    linhas = calcular_linhas_word(texto, margem_direita, margem_esquerda)
    
    print(f"Texto: {texto[:50]}... (total: {len(texto)} caracteres)")
    print(f"Margem esquerda: {margem_esquerda}cm")
    print(f"Margem direita: {margem_direita}cm")
    print(f"Largura útil: {21 - margem_esquerda - margem_direita}cm")
    print(f"Número aproximado de linhas: {linhas}")
    print("-" * 50)
    
    return linhas

# Exemplo de uso
texto_exemplo = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris."


# Você pode testar com seu próprio texto
seu_texto = texto_exemplo
sua_margem = 4  # ou qualquer valor decimal
linhas = calcular_linhas_word(seu_texto, sua_margem)
print(f"Seu texto terá aproximadamente {linhas} linhas")