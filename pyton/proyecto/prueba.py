import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mssg
import sqlite3


class Inventario:
    def __init__(self, master=None):
        self.path = r'X:/Users/ferna/Documents/UNal/Alumnos/2023_S2/ProyInventario'
        self.db_name = self.path + r'/Inventario.db'
        ancho = 630
        alto = 640  # Dimensione de la pantalla
        actualiza = None  # nos lo puso para algo

        # Crea ventana principal
        self.win = tk.Tk()
        self.win.geometry(f"{ancho}x{alto}")
        # self.win.iconbitmap("f2.ico")
        # no deja que se ajuste la pantalla, tener en cuenta
        self.win.resizable(False, False)
        self.win.title("Manejo de Proveedores")

        # Centra la pantalla
        self.centra(self.win, ancho, alto)

        # Contenedor de widgets
        self.win = tk.LabelFrame(master)
        self.win.configure(background="#e0e0e0", font="{Arial} 12 {bold}",
                           height=ancho, labelanchor="n", width=alto)
        self.tabs = ttk.Notebook(self.win)
        self.tabs.configure(height=800, width=799)

        # Frame de datos
        self.frm1 = ttk.Frame(self.tabs)
        self.frm1.configure(height=200, width=200)

        # Etiqueta IdNit del Proveedor
        self.lblIdNit = ttk.Label(self.frm1)
        self.lblIdNit.configure(text='Id/Nit', width=6)
        self.lblIdNit.place(anchor="nw", x=10, y=40)

        # Captura IdNit del Proveedor
        self.idNit = ttk.Entry(self.frm1)
        self.idNit.configure(takefocus=True)
        # cambiar fuente en configure
        self.idNit.place(anchor="nw", x=50, y=40)
        self.idNit.bind("<Key>")  # self.validaIdNit
        self.idNit.bind("<BackSpace>", lambda _: self.idNit.delete(
            len(self.idNit.get())), 'end')

        """ quiza con grid lo podemos hacer adaptable  """
        # Etiqueta razón social del Proveedor
        self.lblRazonSocial = ttk.Label(self.frm1)
        self.lblRazonSocial.configure(text='Razon social', width=12)
        self.lblRazonSocial.place(anchor="nw", x=210, y=40)

        # Captura razón social del Proveedor
        self.razonSocial = ttk.Entry(self.frm1)
        self.razonSocial.configure(width=36)
        self.razonSocial.place(anchor="nw", x=290, y=40)

        # Etiqueta ciudad del Proveedor
        self.lblCiudad = ttk.Label(self.frm1)
        self.lblCiudad.configure(text='Ciudad', width=7)
        self.lblCiudad.place(anchor="nw", x=540, y=40)

        # Captura ciudad del Proveedor
        self.ciudad = ttk.Entry(self.frm1)
        self.ciudad.configure(width=30)
        self.ciudad.place(anchor="nw", x=590, y=40)

        # Separador
        self.separador1 = ttk.Separator(self.frm1)
        self.separador1.configure(orient="horizontal")
        self.separador1.place(anchor="nw", width=800, x=0, y=79)

        """ Podemos crear 4 frames en vez de solo 1 """
        """ Estos son los titulos de la tabla """
        # Etiqueta Código del Producto
        self.lblCodigo = ttk.Label(self.frm1)
        self.lblCodigo.configure(text='Código', width=7)
        self.lblCodigo.place(anchor="nw", x=10, y=120)

        # Captura el código del Producto
        self.codigo = ttk.Entry(self.frm1)
        self.codigo.configure(width=13)
        self.codigo.place(anchor="nw", x=60, y=120)

        # Etiqueta descripción del Producto
        self.lblDescripcion = ttk.Label(self.frm1)
        self.lblDescripcion.configure(text='Descripción', width=11)
        self.lblDescripcion.place(anchor="nw", x=220, y=120)

        # Captura la descripción del Producto
        self.descripcion = ttk.Entry(self.frm1)
        self.descripcion.configure(width=36)
        self.descripcion.place(anchor="nw", x=290, y=120)

        # Etiqueta unidad o medida del Producto
        self.lblUnd = ttk.Label(self.frm1)
        self.lblUnd.configure(text='Unidad', width=7)
        self.lblUnd.place(anchor="nw", x=540, y=120)

        # Captura la unidad o medida del Producto
        self.unidad = ttk.Entry(self.frm1)
        self.unidad.configure(width=10)
        self.unidad.place(anchor="nw", x=590, y=120)

        # Etiqueta cantidad del Producto
        self.lblCantidad = ttk.Label(self.frm1)
        self.lblCantidad.configure(text='Cantidad', width=8)
        self.lblCantidad.place(anchor="nw", x=10, y=170)

        # Captura la cantidad del Producto
        self.cantidad = ttk.Entry(self.frm1)
        self.cantidad.configure(width=12)
        self.cantidad.place(anchor="nw", x=70, y=170)

        # Etiqueta precio del Producto
        self.lblPrecio = ttk.Label(self.frm1)
        self.lblPrecio.configure(text='Precio $', width=8)
        self.lblPrecio.place(anchor="nw", x=170, y=170)

        # Captura el precio del Producto
        self.precio = ttk.Entry(self.frm1)
        self.precio.configure(width=15)
        self.precio.place(anchor="nw", x=220, y=170)

        # Etiqueta fecha de compra del Producto
        self.lblFecha = ttk.Label(self.frm1)
        self.lblFecha.configure(text='Fecha', width=6)
        self.lblFecha.place(anchor="nw", x=350, y=170)

        """ La fecha se debe recibir en formato de fecha """
        # Captura la fecha de compra del Producto
        self.fecha = ttk.Entry(self.frm1)
        self.fecha.configure(width=10)
        self.fecha.place(anchor="nw", x=390, y=170)

        # Separador
        self.separador2 = ttk.Separator(self.frm1)
        self.separador2.configure(orient="horizontal")
        self.separador2.place(anchor="nw", width=800, x=0, y=220)

        """ Podemos crear función separador """
        """ Aquí inicia el tercer frame """

        # tablaTreeView
        self.style = ttk.Style()
        self.style.configure("estilo.Treeview", highlightthickness=0,
                             bd=0, background="#e0e0e0", font=('Calibri Light', 10))
        self.style.configure("estilo.Treeview.Heading", background='Azure', font=(
            'Calibri Light', 10, 'bold'))
        self.style.layout("estilo.Treeview", [
                          ('estilo.Treeview.treearea', {'sticky': 'nswe'})])

        # Árbol para mosrtar los datos de la B.D.
        self.treeProductos = ttk.Treeview(self.frm1, style="estilo.Treeview")

        self.treeProductos.configure(selectmode="extended")

        # Etiquetas de las columnas para el TreeView
        self.treeProductos["columns"] = (
            "Codigo", "Descripcion", "Und", "Cantidad", "Precio", "Fecha")
        # Características de las columnas del árbol
        self.treeProductos.column(
            "#0",          anchor="w", stretch=True, width=3)
        self.treeProductos.column(
            "Codigo",      anchor="w", stretch=True, width=3)
        self.treeProductos.column(
            "Descripcion", anchor="w", stretch=True, width=150)
        self.treeProductos.column(
            "Und",         anchor="w", stretch=True, width=3)
        self.treeProductos.column(
            "Cantidad",    anchor="w", stretch=True, width=3)
        self.treeProductos.column(
            "Precio",      anchor="w", stretch=True, width=8)
        self.treeProductos.column(
            "Fecha",       anchor="w", stretch=True, width=3)

        # Etiquetas de columnas con los nombres que se mostrarán por cada columna
        self.treeProductos.heading(
            "#0",          anchor="center", text='ID / Nit')
        self.treeProductos.heading(
            "Codigo",      anchor="center", text='Código')
        self.treeProductos.heading(
            "Descripcion", anchor="center", text='Descripción')
        self.treeProductos.heading(
            "Und",         anchor="center", text='Unidad')
        self.treeProductos.heading(
            "Cantidad",    anchor="center", text='Cantidad')
        self.treeProductos.heading(
            "Precio",      anchor="center", text='Precio')
        self.treeProductos.heading(
            "Fecha",       anchor="center", text='Fecha')

        # Carga los datos en treeProductos
        # self.lee_treeProductos()
        self.treeProductos.place(
            anchor="nw", height=560, width=790, x=2, y=230)

        # Scrollbar en el eje Y de treeProductos
        self.scrollbary = ttk.Scrollbar(
            self.treeProductos, orient='vertical', command=self.treeProductos.yview)
        self.treeProductos.configure(yscroll=self.scrollbary.set)
        self.scrollbary.place(x=778, y=25, height=478)

        """ No sabemos por que recién hizo el título """
        # Título de la pestaña Ingreso de Datos
        self.frm1.pack(side="top")
        self.tabs.add(self.frm1, compound="center", text='Ingreso de datos')
        self.tabs.pack(side="top")

        # widget Principal del sistema
        self.mainwindow = self.win
    # Fución de manejo de eventos del sistema

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
