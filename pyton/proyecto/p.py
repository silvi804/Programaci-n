import tkinter as tk
from tkinter import messagebox

def show_custom_info(message):
    global custom_info  # Para poder acceder a la ventana emergente desde la función

    custom_info = tk.Toplevel()
    custom_info.title("Mensaje Informativo")

    label = tk.Label(custom_info, text=message)
    label.pack()

#    Botón para cerrar solo la ventana emergente
    close_button = tk.Button(custom_info, text="Cerrar", command=custom_info.quit)
    close_button.pack()

# Función para cerrar la ventana emergente sin destruirla
def cerrar_ventana_emergente():
    global custom_info  # Accede a la ventana emergente creada
    custom_info.destroy()

# Ejemplo de uso
root = tk.Tk()
root.geometry("300x200")

def show_info_message():
    show_custom_info("Este es un mensaje informativo personalizado.")

info_button = tk.Button(root, text="Mostrar Info Personalizado", command=show_info_message)
info_button.pack()

# Botón en la ventana principal para cerrar la ventana emergente
btn_cancelar = tk.Button(root, text="Cancelar", command=cerrar_ventana_emergente)
btn_cancelar.pack()

root.mainloop() 
