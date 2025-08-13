import textwrap

def texto_config_Apr(nome):
    texto_apr = f"""
    import arcpy

    # Configurações
    nome_original = "APR"  # Nome da camada no mapa (ou caminho completo se necessário)
    novo_nome = "{nome} - A.P.R"
    caminho_lyr = r"C:\\Users\\USUARIO\\Desktop\\automacoes\\envimap\\mapa_fitofisionomia\\cores_style\\APR.lyr"

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
        
        if camada_alvo:  # CORREÇÃO: estava escrito "camada_alvo" (erro de digitação)
            # 1. Aplicar o estilo
            estilo = arcpy.mapping.Layer(caminho_lyr)
            arcpy.mapping.UpdateLayer(df, camada_alvo, estilo, True)
            
            # 2. Alterar o nome
            camada_alvo.name = novo_nome
            
            
            
            # Atualizar a visualização
            arcpy.RefreshTOC()
            arcpy.RefreshActiveView()
        else:
            teste =1 

    except Exception as e:
        print("Erro durante a execução:")
        print(str(e))
        """
    return textwrap.dedent(texto_apr)