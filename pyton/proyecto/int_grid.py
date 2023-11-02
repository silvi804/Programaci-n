import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mssg
import sqlite3


class Inventario:
    def __init__(self, master=None):
        self.path = r'c:/Users/ASUS/Documents/Programacion_propia/pyton/proyecto/intento.py'

        # Crea ventana principal
        self.win = tk.Tk()
        self.win.title("Manejo de Proveedores")
        self.win.iconbitmap(r"f2.ico")
        # self.win.resizable(False, False)

        # Establece dimensiones ventana
        pix_Ancho = self.win.winfo_screenwidth()
        pix_alto = self.win.winfo_screenheight()
        ancho = int(pix_Ancho*0.6)
        alto = int(pix_alto*0.8)
        self.win.geometry(f"{ancho}x{alto}")

        # Centra la pantalla
        self.centra(self.win, ancho, alto)

        # Contenedor de widgets
        self.win = tk.LabelFrame(master)
        self.win.configure(background="#e0e0e0", font="{Arial} 12 {bold}",
                           height=ancho, labelanchor="n", width=alto)
        self.tabs = ttk.Notebook(self.win)
        self.tabs.configure(height=int(alto*0.96), width=int(ancho*0.92))

        # Frame de datos generales
        self.frm1 = ttk.Frame(self.tabs)
        self.frm1.configure(height=int(alto*0.25), width=int(ancho*0.25))

        # Espacio arriba y abajo
        self.frm1.rowconfigure(index=0, weight=2)
        self.frm1.rowconfigure(index=2, weight=1)
        self.frm1.rowconfigure(index=4, weight=2)

        # Configuración columnas
        self.frm1.columnconfigure(index=1, weight=2)
        self.frm1.columnconfigure(index=3, weight=2)
        self.frm1.columnconfigure(index=5, weight=2)

        # Etiqueta IdNit del Proveedor
        self.lblIdNit = ttk.Label(self.frm1)
        self.lblIdNit.configure(text='Id/Nit', width=int(ancho*0.008))
        self.lblIdNit.grid(row=1, column=0, sticky="e")
        # self.lblIdNit.place(anchor="nw", x=10, y=40)

        # Captura IdNit del Proveedor
        self.idNit = ttk.Entry(self.frm1)
        self.idNit.configure(takefocus=True, width=int(ancho*0.03))
        self.idNit.grid(row=1, column=1, sticky="w")
        # self.idNit.place(anchor="nw", x=50, y=40)

        """ Aquí hay que tener en cuenta funciones del entry Id"""
        self.idNit.bind("<Key>")  # self.validaIdNit
        # widget.bind(event, func)
        self.idNit.bind("<BackSpace>", lambda _: self.idNit.delete(
            len(self.idNit.get())), 'end')
        # función que ni idea que hace
        """ Hasta acá """

        # Etiqueta razón social del Proveedor
        self.lblRazonSocial = ttk.Label(self.frm1)
        self.lblRazonSocial.configure(
            text='Razon social', width=int(ancho*0.015))  # rev width
        self.lblRazonSocial.grid(row=1, column=2, sticky="e")
        # self.lblRazonSocial.place(anchor="nw", x=210, y=40)

        # Captura razón social del Proveedor
        self.razonSocial = ttk.Entry(self.frm1)
        self.razonSocial.configure(width=int(ancho*0.04))
        self.razonSocial.grid(row=1, column=3, sticky="w")
        # self.razonSocial.place(anchor="nw", x=290, y=40)

        # Etiqueta ciudad del Proveedor
        self.lblCiudad = ttk.Label(self.frm1)
        self.lblCiudad.configure(text='Ciudad', width=int(ancho*0.01))
        self.lblCiudad.grid(row=1, column=4, sticky="e")
        # self.lblCiudad.place(anchor="nw", x=540, y=40)

        # Captura ciudad del Proveedor
        self.ciudad = ttk.Entry(self.frm1)
        self.ciudad.configure(width=int(ancho*0.03))
        self.ciudad.grid(row=1, column=5, sticky="w")
        # self.ciudad.place(anchor="nw", x=590, y=40)

        # Separador
        self.separador1 = ttk.Separator(self.frm1)
        self.separador1.configure(orient="horizontal")
        self.separador1.grid(row=3, column=0, columnspan=6, sticky="ew")
        # self.separador1.place(anchor="nw", width=800, x=0, y=79)

        # Etiqueta Código del Producto
        self.lblCodigo = ttk.Label(self.frm1)
        self.lblCodigo.configure(text='Código', width=int(ancho*0.008))
        self.lblCodigo.grid(row=5, column=0, sticky="e")
        # self.lblCodigo.place(anchor="nw", x=10, y=120)

        # Captura el código del Producto
        self.codigo = ttk.Entry(self.frm1)
        self.codigo.configure(width=int(ancho*0.02))
        self.codigo.grid(row=5, column=1, sticky="w")
        # self.codigo.place(anchor="nw", x=60, y=120)

        # Etiqueta descripción del Producto
        self.lblDescripcion = ttk.Label(self.frm1)
        self.lblDescripcion.configure(
            text='Descripción', width=int(ancho*0.015))
        self.lblDescripcion.grid(row=5, column=2, sticky="e")
        # self.lblDescripcion.place(anchor="nw", x=220, y=120)

        # Captura la descripción del Producto
        self.descripcion = ttk.Entry(self.frm1)
        self.descripcion.configure(width=int(ancho*0.04))
        self.descripcion.grid(row=5, column=3, sticky="w")

        # self.descripcion.place(anchor="nw", x=290, y=120)

        # Etiqueta unidad o medida del Producto
        self.lblUnd = ttk.Label(self.frm1)
        self.lblUnd.configure(text='Unidad', width=int(ancho*0.01))
        self.lblUnd.grid(row=5, column=4, sticky="e")
        # self.lblUnd.place(anchor="nw", x=540, y=120)

        # Captura la unidad o medida del Producto
        self.unidad = ttk.Entry(self.frm1)
        self.unidad.configure(width=int(ancho*0.01))
        self.unidad.grid(row=5, column=5, sticky="w")
        # self.unidad.place(anchor="nw", x=590, y=120)

        """ Inicia el frame 2 """
        # Frame de datos específicos
        self.frm2 = ttk.Frame(self.win)
        self.frm2.configure(height=int(alto*0.1), width=ancho)

        # Botón para Buscar un Proveedor
        self.btnBuscar = ttk.Button(self.frm2)
        self.btnBuscar.configure(text='Buscar')
        self.btnBuscar.grid(row=0, column=2, sticky="w")
        # self.btnBuscar.place(anchor="nw", width=70, x=200, y=10)

        # Empaquetamiento frm1
        self.frm1.pack(anchor="n")
        self.frm2.pack(anchor="center")
        self.tabs.add(self.frm1, compound="center",
                      text='Ingreso de datos')

        self.tabs.pack(side="top")
        self.win.pack(anchor="center", side="top")

        # widget Principal del sistema
        self.mainwindow = self.win

    def run(self):
        self.mainwindow.mainloop()

    ''' ......... Métodos utilitarios del sistema .............'''
    # Rutina de centrado de pantalla

    def centra(self, win, ancho, alto):
        """ centra las ventanas en la pantalla """
        x = win.winfo_screenwidth() // 2 - ancho // 2
        y = win.winfo_screenheight() // 2 - alto // 2
        win.geometry(f'{ancho}x{alto}+{x}+{y}')
        win.deiconify()  # Se usa para restaurar la ventana


if __name__ == "__main__":
    app = Inventario()
    app.run()
