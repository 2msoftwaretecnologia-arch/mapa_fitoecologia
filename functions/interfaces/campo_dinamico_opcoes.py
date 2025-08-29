import pyautogui

def selecionar_resposta(options_list, multi_select=False, title="Seleção"):
    if multi_select:
        resposta = pyautogui.confirm(text="Selecione todas as opções desejadas:", title=title, buttons=options_list + ["Concluir"])
        selecionadas = []
        while resposta != "Concluir":
            if resposta and resposta not in selecionadas:
                selecionadas.append(resposta)
            resposta = pyautogui.confirm(text="Selecione todas as opções desejadas:", title=title, buttons=options_list + ["Concluir"])
        return selecionadas
    else:
        resposta = pyautogui.confirm(text="Selecione uma opção:", title=title, buttons=options_list)
        return resposta
    

