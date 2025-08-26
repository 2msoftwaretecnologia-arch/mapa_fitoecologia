import tkinter as tk

def show_alert_dinamic(message):
    def flash():
        nonlocal current_color_index
        current_color_index = 1 - current_color_index
        cor = colors[current_color_index]
        root.config(bg=cor)
        label.config(bg=cor)
        root.after(1000, flash)

    colors = ["yellow", "red"]
    current_color_index = 0

    root = tk.Tk()
    root.withdraw()  # evita mostrar antes de configurar tudo
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
                       command=root.destroy)
    button.pack(pady=(0, 20))

    root.update_idletasks()
    largura = label.winfo_reqwidth() + 40
    altura = label.winfo_reqheight() + button.winfo_reqheight() + 60

    sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
    x = (sw // 2) - (largura // 2)
    y = (sh // 2) - (altura // 2)
    root.geometry(f"{largura}x{altura}+{x}+{y}")
    root.deiconify()

    flash()
    root.mainloop()
