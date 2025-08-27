import tkinter as tk

def show_alert_dinamic(message):
    colors = ["yellow", "red"]
    current_color_index = 0
    job_id = None         # ID do after agendado
    closing = False       # flag para parar o loop de piscar

    def flash():
        nonlocal current_color_index, job_id
        if closing or not root.winfo_exists():
            return  # não reagendar se já está fechando

        # alterna a cor
        current_color_index = 1 - current_color_index
        cor = colors[current_color_index]

        try:
            root.config(bg=cor)
            label.config(bg=cor)
        except tk.TclError:
            return  # widgets já foram destruídos

        # reagenda
        job_id = root.after(1000, flash)

    def on_close():
        nonlocal closing, job_id
        closing = True
        if job_id is not None:
            try:
                root.after_cancel(job_id)
            except tk.TclError:
                pass
        root.destroy()

    root = tk.Tk()
    root.withdraw()
    root.title("!!! ALERTA !!!")
    root.attributes("-topmost", True)
    root.config(bg=colors[current_color_index])

    label = tk.Label(
        root, text=message, font=("Helvetica", 18, "bold"),
        bg=colors[current_color_index], fg="black",
        justify="center", wraplength=600
    )
    label.pack(padx=20, pady=(20, 10))

    button = tk.Button(root, text="Entendi", font=("Helvetica", 14, "bold"),
                       command=on_close)
    button.pack(pady=(0, 20))

    # Fechar pela borda da janela também passa por on_close
    root.protocol("WM_DELETE_WINDOW", on_close)

    root.update_idletasks()
    largura = label.winfo_reqwidth() + 40
    altura = label.winfo_reqheight() + button.winfo_reqheight() + 60
    sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
    x = (sw // 2) - (largura // 2)
    y = (sh // 2) - (altura // 2)
    root.geometry(f"{largura}x{altura}+{x}+{y}")
    root.deiconify()

    # Começa o piscar via after (em vez de chamar flash() direto)
    job_id = root.after(0, flash)
    root.mainloop()
