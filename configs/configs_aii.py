import textwrap

def texto_config_Aii():
    texto_aii = """
    import arcpy

    # Configurações
    nome_original = "AII"  # Nome da camada no mapa (ou caminho completo se necessário)
    novo_nome = "Área de Influência Indireta - AII"
    caminho_lyr = r"C:\\Users\\USUARIO\\Desktop\\automacoes\\mapa_fitoecologia_envimap\\cores_style\\AII.lyr"

    try:
        # Acessar o mapa atual
        mxd = arcpy.mapping.MapDocument("CURRENT")
        df = arcpy.mapping.ListDataFrames(mxd)[0]  # Primeiro data frame
        
        # Procurar pela camada
        camada_alvo = None
        for lyr in arcpy.mapping.ListLayers(mxd, "", df):
            if lyr.name == nome_original or lyr.name.startswith(nome_original):
                camada_alvo = lyr
                break
        
        if camada_alvo:
            # 1. Aplicar o estilo
            estilo = arcpy.mapping.Layer(caminho_lyr)
            arcpy.mapping.UpdateLayer(df, camada_alvo, estilo, True)
            
            # 2. Alterar o nome
            camada_alvo.name = novo_nome
            
            # 3. Zoom para a extensão da camada
            df.extent = camada_alvo.getExtent()
            
            
            
            # Atualizar a visualização
            arcpy.RefreshTOC()
            arcpy.RefreshActiveView()
        else:
            print("Erro: Camada não encontrada no mapa!".format(nome_original))

    except Exception as e:
        print("Erro durante a execução:")
        print(str(e))"""
    
    return textwrap.dedent(texto_aii)