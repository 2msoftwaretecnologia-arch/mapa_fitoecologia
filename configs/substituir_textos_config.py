import textwrap

def substituir_textos(text,tag="tag"):
    # Processa o texto de entrada para escapar quebras de linha e aspas
    processed_text = text.replace('\n', '\\n').replace('"', '\\"')
    
    texto = f"""
    import arcpy

    # Dicionário de substituições (chave: valor antigo, valor: novo texto)
    substitutions = {{
        "#{tag}": u"{processed_text}",
    }}

    mxd = arcpy.mapping.MapDocument("CURRENT")  # Trabalha no MXD atual

    # Função para substituir texto em elementos gráficos
    def replace_text(element):
        if element.type == "TEXT_ELEMENT":
            for old_text, new_text in substitutions.items():
                if old_text in element.text:
                    element.text = element.text.replace(old_text, new_text)
        elif element.type == "GROUP_ELEMENT":
            for sub_element in element:
                replace_text(sub_element)

    # Processa todos os elementos do layout
    for el in arcpy.mapping.ListLayoutElements(mxd):
        replace_text(el)

    # Atualiza a visualização e limpa recursos
    arcpy.RefreshActiveView()
    del mxd
    """
    return textwrap.dedent(texto)