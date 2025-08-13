import textwrap

def texto_config_estados(estado):
    texto = f"""
    import arcpy

    # Configurações
    nome_original = "LimiteEstado" 
    novo_nome = "{estado} - SEPLAN (2012)"
    caminho_lyr = r"C:\\Users\\USUARIO\\Desktop\\automacoes\\envimap\\mapa_fitofisionomia\\cores_style\\LimiteEstado.lyr"

    try:
        # Acessar o mapa atual
        mxd = arcpy.mapping.MapDocument("CURRENT")
        
        # Procurar pela camada em todos os data frames
        camada_alvo = None
        data_frame_alvo = None
        
        # Percorrer todos os data frames
        for df in arcpy.mapping.ListDataFrames(mxd):
            # Procurar em todas as camadas do data frame atual
            for lyr in arcpy.mapping.ListLayers(mxd, "", df):
                if lyr.name == nome_original or lyr.name.startswith(nome_original):
                    camada_alvo = lyr
                    data_frame_alvo = df
                    break
            if camada_alvo:  # Se encontrou a camada, sair do loop
                break
        
        if camada_alvo:
            # 1. Aplicar o estilo
            estilo = arcpy.mapping.Layer(caminho_lyr)
            arcpy.mapping.UpdateLayer(data_frame_alvo, camada_alvo, estilo, True)
            
            # 2. Alterar o nome
            camada_alvo.name = novo_nome
            
            
            # Atualizar a visualização
            arcpy.RefreshTOC()
            arcpy.RefreshActiveView()
        else:
            teste = 1

    except Exception as e:
        print("Erro durante a execução:")
        print(str(e))
        """
    return textwrap.dedent(texto)