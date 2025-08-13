import textwrap

def escala_padrao(escala=25000):
    texto = f"""
        import arcpy

        # Obter o mapa ativo
        mxd = arcpy.mapping.MapDocument("CURRENT")
        df = arcpy.mapping.ListDataFrames(mxd)[0]  # Pega o primeiro data frame

        # Definir a escala para 1:25.000
        df.scale = {escala}

        # Atualizar a visualização
        arcpy.RefreshActiveView()

        print "Escala alterada com sucesso!"
    """
    return textwrap.dedent(texto)

