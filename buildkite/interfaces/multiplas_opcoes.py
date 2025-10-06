import tkinter as tk
from tkinter import messagebox

def criar_interface_opcoes(opcoes_disponiveis):
    """
    ============================================================
    🧠 FUNÇÃO: criar_interface_opcoes(opcoes_disponiveis)
    ============================================================

    📋 DESCRIÇÃO:
        Cria uma interface gráfica (GUI) com Tkinter que permite
        ao usuário selecionar até 4 opções dentre uma lista fornecida.

        A interface possui:
        - Scrollbar (para muitas opções)
        - Contador de seleções (0/4)
        - Botões "Confirmar" e "Cancelar"
        - Bloqueio automático ao atingir o limite de 4 opções

    ⚙️ PARÂMETROS:
        opcoes_disponiveis (list):
            Lista de strings com as opções que o usuário poderá escolher.
            Exemplo: ["Maçã", "Banana", "Uva", "Manga"]

    🎯 RETORNA:
        list:
            Lista com as opções selecionadas.
            Se o usuário clicar em "Cancelar", retorna lista vazia [].
            Se confirmar sem selecionar nada, exibe aviso.

    💡 EXEMPLO DE USO:
        opcoes = ["Banana", "Maçã", "Uva", "Laranja", "Manga"]
        selecionadas = criar_interface_opcoes(opcoes)
        print(selecionadas)  # ['Banana', 'Manga', 'Uva']

    ============================================================
    """

    selecoes = []  # Armazena as opções escolhidas
    root = tk.Tk()
    root.title("Seleção de Opções")
    root.geometry("400x600")

    # Cada opção é controlada por uma variável booleana (tk.BooleanVar)
    var_opcoes = {opcao: tk.BooleanVar() for opcao in opcoes_disponiveis}

    # ------------------------------------------------------------
    # 🧮 Função interna: Atualiza contador e bloqueia checkboxes
    # ------------------------------------------------------------
    def atualizar_contador():
        total_selecionado = sum(var.get() for var in var_opcoes.values())
        contador_label.config(text=f"Selecionadas: {total_selecionado}/4")

        # Se 4 selecionadas → bloqueia as demais
        if total_selecionado >= 4:
            for opcao, var in var_opcoes.items():
                if not var.get():
                    checkboxes[opcao].config(state=tk.DISABLED)
        else:
            # Libera novamente se desmarcar
            for checkbox in checkboxes.values():
                checkbox.config(state=tk.NORMAL)

    # ------------------------------------------------------------
    # 🖱️ Callback: quando um checkbox é clicado
    # ------------------------------------------------------------
    def on_checkbox_click(opcao):
        atualizar_contador()

    # ------------------------------------------------------------
    # ✅ Botão Confirmar
    # ------------------------------------------------------------
    def confirmar():
        nonlocal selecoes
        selecoes = [opcao for opcao, var in var_opcoes.items() if var.get()]

        # Alerta se nenhuma opção for marcada
        if len(selecoes) == 0:
            messagebox.showwarning("Aviso", "Por favor, selecione pelo menos uma opção!")
            return

        root.quit()
        root.destroy()

    # ------------------------------------------------------------
    # ❌ Botão Cancelar
    # ------------------------------------------------------------
    def cancelar():
        nonlocal selecoes
        selecoes = []
        root.quit()
        root.destroy()

    # ------------------------------------------------------------
    # 🧱 Construção da interface
    # ------------------------------------------------------------

    main_frame = tk.Frame(root, padx=20, pady=20)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # 🏷️ Título
    titulo_label = tk.Label(main_frame, text="Selecione até 4 opções:", 
                           font=("Arial", 14, "bold"))
    titulo_label.pack(pady=(0, 20))

    # 🔢 Contador de seleções
    contador_label = tk.Label(main_frame, text="Selecionadas: 0/4", 
                             font=("Arial", 10), fg="blue")
    contador_label.pack(pady=(0, 10))

    # 🧾 Frame com scrollbar para as opções
    frame_opcoes = tk.Frame(main_frame)
    frame_opcoes.pack(fill=tk.BOTH, expand=True, pady=(0, 20))

    # Canvas + Scrollbar
    canvas = tk.Canvas(frame_opcoes)
    scrollbar = tk.Scrollbar(frame_opcoes, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    # Ajusta área de rolagem conforme o tamanho dos widgets
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # ------------------------------------------------------------
    # 🖱️ Suporte ao scroll do mouse
    # ------------------------------------------------------------
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # Windows
    canvas.bind_all("<MouseWheel>", _on_mousewheel)
    # Linux
    canvas.bind_all("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))
    canvas.bind_all("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))

    # ------------------------------------------------------------
    # ☑️ Criação dinâmica dos checkbuttons
    # ------------------------------------------------------------
    checkboxes = {}
    for opcao in opcoes_disponiveis:
        cb = tk.Checkbutton(scrollable_frame, text=opcao, 
                           variable=var_opcoes[opcao],
                           command=lambda o=opcao: on_checkbox_click(o),
                           font=("Arial", 11))
        cb.pack(anchor="w", pady=2)
        checkboxes[opcao] = cb

    # Empacota canvas e scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # ------------------------------------------------------------
    # 🔘 Botões Confirmar e Cancelar
    # ------------------------------------------------------------
    frame_botoes = tk.Frame(main_frame)
    frame_botoes.pack(pady=10)

    btn_confirmar = tk.Button(frame_botoes, text="Confirmar", 
                             command=confirmar, bg="green", fg="white",
                             font=("Arial", 12), width=10)
    btn_confirmar.pack(side=tk.LEFT, padx=10)

    btn_cancelar = tk.Button(frame_botoes, text="Cancelar", 
                            command=cancelar, bg="red", fg="white",
                            font=("Arial", 12), width=10)
    btn_cancelar.pack(side=tk.LEFT, padx=10)

    # Inicializa contador com 0
    atualizar_contador()

    # Centraliza a janela
    root.eval('tk::PlaceWindow . center')

    # Executa o loop principal (interface interativa)
    root.mainloop()

    # ------------------------------------------------------------
    # 📤 Retorna as opções selecionadas
    # ------------------------------------------------------------
    return selecoes
