import tkinter as tk

def on_close():
    print("Ventana emergente cerrada")

def open_popup():
    popup = tk.Toplevel(root)
    label = tk.Label(popup, text="Ventana emergente")
    label.pack()

    def on_closing():
        on_close()
        popup.destroy()

    popup.protocol("WM_DELETE_WINDOW", on_closing)
    popup.wait_window()

root = tk.Tk()

button = tk.Button(root, text="Abrir ventana emergente", command=open_popup)
button.pack()

root.mainloop()
