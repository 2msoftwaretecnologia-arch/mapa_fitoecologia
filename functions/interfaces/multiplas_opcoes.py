import tkinter as tk
from tkinter import messagebox

def criar_interface_opcoes(opcoes_disponiveis):
    """
    Cria uma interface gráfica para selecionar até 4 opções
    
    Args:
        opcoes_disponiveis (list): Lista de opções disponíveis para seleção
    
    Returns:
        list: Lista com as opções selecionadas pelo usuário
    """
    selecoes = []
    root = tk.Tk()
    root.title("Seleção de Opções")
    root.geometry("400x500")
    
    # Variáveis para os checkbuttons
    var_opcoes = {opcao: tk.BooleanVar() for opcao in opcoes_disponiveis}
    
    def atualizar_contador():
        """Atualiza o contador de seleções"""
        total_selecionado = sum(var.get() for var in var_opcoes.values())
        contador_label.config(text=f"Selecionadas: {total_selecionado}/4")
        
        # Desabilita checkboxes se já selecionou 4
        if total_selecionado >= 4:
            for opcao, var in var_opcoes.items():
                if not var.get():
                    checkboxes[opcao].config(state=tk.DISABLED)
        else:
            for checkbox in checkboxes.values():
                checkbox.config(state=tk.NORMAL)
    
    def on_checkbox_click(opcao):
        """Callback quando um checkbox é clicado"""
        atualizar_contador()
    
    def confirmar():
        """Função chamada quando o botão Confirmar é pressionado"""
        nonlocal selecoes
        selecoes = [opcao for opcao, var in var_opcoes.items() if var.get()]
        
        if len(selecoes) == 0:
            messagebox.showwarning("Aviso", "Por favor, selecione pelo menos uma opção!")
            return
        
        root.quit()
        root.destroy()
    
    def cancelar():
        """Função chamada quando o botão Cancelar é pressionado"""
        nonlocal selecoes
        selecoes = []
        root.quit()
        root.destroy()
    
    # Frame principal
    main_frame = tk.Frame(root, padx=20, pady=20)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Título
    titulo_label = tk.Label(main_frame, text="Selecione até 4 opções:", 
                           font=("Arial", 14, "bold"))
    titulo_label.pack(pady=(0, 20))
    
    # Contador
    contador_label = tk.Label(main_frame, text="Selecionadas: 0/4", 
                             font=("Arial", 10), fg="blue")
    contador_label.pack(pady=(0, 10))
    
    # Frame para as opções com scrollbar
    frame_opcoes = tk.Frame(main_frame)
    frame_opcoes.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
    
    # Canvas e Scrollbar
    canvas = tk.Canvas(frame_opcoes)
    scrollbar = tk.Scrollbar(frame_opcoes, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Criar checkboxes
    checkboxes = {}
    for opcao in opcoes_disponiveis:
        cb = tk.Checkbutton(scrollable_frame, text=opcao, 
                           variable=var_opcoes[opcao],
                           command=lambda o=opcao: on_checkbox_click(o),
                           font=("Arial", 11))
        cb.pack(anchor="w", pady=2)
        checkboxes[opcao] = cb
    
    # Frame para botões
    frame_botoes = tk.Frame(main_frame)
    frame_botoes.pack(pady=20)
    
    # Botões
    btn_confirmar = tk.Button(frame_botoes, text="Confirmar", 
                             command=confirmar, bg="green", fg="white",
                             font=("Arial", 12), width=10)
    btn_confirmar.pack(side=tk.LEFT, padx=10)
    
    btn_cancelar = tk.Button(frame_botoes, text="Cancelar", 
                            command=cancelar, bg="red", fg="white",
                            font=("Arial", 12), width=10)
    btn_cancelar.pack(side=tk.LEFT, padx=10)
    
    # Empacotar canvas e scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Inicializar contador
    atualizar_contador()
    
    # Centralizar janela
    root.eval('tk::PlaceWindow . center')
    
    # Executar interface
    root.mainloop()
    
    return selecoes