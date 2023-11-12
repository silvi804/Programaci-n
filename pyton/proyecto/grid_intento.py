'''Este es un intento opcional que se editará en simultáeo con el que teníamos'''
# !/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mssg
import sqlite3


class Inventario:
    def __init__(self, master=None):
        # Crea ventana principal
         # Crea ventana principal
        self.win = tk.Tk()
        ancho = self.win.winfo_screenwidth() * 60 // 100 #Ancho de la pantalla
        alto = self.win.winfo_screenheight() * 90 // 100 # Alto de la pantalla
        self.win.geometry(f"{ancho}x{alto}")
        self.win.resizable(False, False)
        self.win.title("Manejo de Proveedores")
        self.db_name = 'Inventario.db'
        
        # creación base de datos
        self.run_Query("""CREATE TABLE IF NOT EXISTS 'Productos'(
            idNit VARCHAR(15),
            Codigo VARCHAR(10),
            Descripcion VARCHAR(100),
            Und VARCHAR(19),
            Cantidad DOUBLE,
            Precio DOUBLE,
            Fecha DATE,
            FOREIGN KEY(idNit) REFERENCES Proveedor(idNitProv),
            PRIMARY KEY(idNit,Codigo)         
            );""")
        self.run_Query("""CREATE TABLE IF NOT EXISTS 'Proveedor' (
            idNitProv VARCHAR(15) NOT NULL ,
            Razon_Social VARCHAR(100),
            Ciudad VARCHAR(20),
            PRIMARY KEY(idNitProv)
            );""")

        # Centra la pantalla
        self.centra(self.win, ancho, alto)

        # Contenedor de widgets
        self.win = tk.LabelFrame(self.win)
        self.win.configure(background="#e0e0e0", font="{Arial} 12 {bold}",
                           height=alto, labelanchor="n", width=ancho)
        self.tabs = ttk.Notebook(self.win)
        self.tabs.configure(height=alto, width=ancho)

        # Frame de datos
        self.main_frame = ttk.Frame(self.tabs)

        self.frm1 = ttk.Frame(self.main_frame)
        self.frm1.configure(height=alto * 80//100, width=ancho)
        self.frm2 = ttk.Frame(self.main_frame)
        self.frm2.configure(height=alto * 20 // 100, width= 25)

        # Etiqueta IdNit del Proveedor
        self.lblIdNit = ttk.Label(self.frm1)
        self.lblIdNit.configure(text='Id/Nit', width= ancho // 100)
        self.lblIdNit.grid(column=0,  padx=20, pady=20, row=0)

        # Captura IdNit del Proveedor
        self.idNit = ttk.Entry(self.frm1)
        self.idNit.configure(takefocus=True)#, width=
        self.idNit.grid(column=1, row=0)
        self.idNit.bind("<KeyRelease>", self.validaIdNit)
        self.idNit.bind("<BackSpace>", lambda _: self.idNit.delete(
            len(self.idNit.get())), 'end')
        self.idNit.focus_set()

        # Etiqueta razón social del Proveedor
        self.lblRazonSocial = ttk.Label(self.frm1)
        self.lblRazonSocial.configure(text='Razon social', width= ancho * 12 // 1000)
        self.lblRazonSocial.grid(column=2, padx=20, pady=20 ,row=0)

        # Captura razón social del Proveedor
        self.razonSocial = ttk.Entry(self.frm1)
        self.razonSocial.configure(width= ancho * 24 // 1000)
        self.razonSocial.grid(column=3, padx=20, pady=20, row=0)

        # Etiqueta ciudad del Proveedor
        self.lblCiudad = ttk.Label(self.frm1)
        self.lblCiudad.configure(text='Ciudad', width= ancho * 10 // 1000)
        self.lblCiudad.grid(column=4, padx=20, pady=20, row=0)

        # Captura ciudad del Proveedor
        self.ciudad = ttk.Entry(self.frm1)
        self.ciudad.configure(width= ancho * 23 // 1000)
        self.ciudad.grid(column=5, padx=20, pady=20, row=0)

        # Separador
        self.separador1 = ttk.Separator(self.frm1)
        self.separador1.configure(orient="horizontal")
        self.separador1.grid(columnspan=6, padx=20, pady=20, row=1, sticky="ew")

        # Etiqueta Código del Producto
        self.lblCodigo = ttk.Label(self.frm1)
        self.lblCodigo.configure(text='Código', width=7)
        self.lblCodigo.grid(row=2, padx=20, pady=20 ,column=0)

        # Captura el código del Producto
        self.codigo = ttk.Entry(self.frm1)
        self.codigo.configure(width=13)
        self.codigo.grid(row=2, padx=20, pady=20 ,column=1)

        # Etiqueta descripción del Producto
        self.lblDescripcion = ttk.Label(self.frm1)
        self.lblDescripcion.configure(text='Descripción', width=11)
        self.lblDescripcion.grid(row=2, padx=20, pady=20 ,column=2)

        # Captura la descripción del Producto
        self.descripcion = ttk.Entry(self.frm1)
        self.descripcion.configure(width=36)
        self.descripcion.grid(row=2, padx=20, pady=20 ,column=3)

        # Etiqueta unidad o medida del Producto
        self.lblUnd = ttk.Label(self.frm1)
        self.lblUnd.configure(text='Unidad', width=7)
        self.lblUnd.grid(row=2, padx=20, pady=20 ,column=4)

        # Captura la unidad o medida del Producto
        self.unidad = ttk.Entry(self.frm1)
        self.unidad.configure(width=10)
        self.unidad.grid(row=2, padx=20, pady=20 ,column=5)

        # Etiqueta cantidad del Producto
        self.lblCantidad = ttk.Label(self.frm1)
        self.lblCantidad.configure(text='Cantidad', width=8)
        self.lblCantidad.grid(row=3, padx=20, pady=20 ,column=0)

        # Captura la cantidad del Producto
        self.cantidad = ttk.Entry(self.frm1)
        self.cantidad.configure(width=12)
        self.cantidad.grid(row=3, padx=20, pady=20 ,column=1)

        # Etiqueta precio del Producto
        self.lblPrecio = ttk.Label(self.frm1)
        self.lblPrecio.configure(text='Precio $', width=8)
        self.lblPrecio.grid(row=3, padx=20, pady=20 ,column=2)

        # Captura el precio del Producto
        self.precio = ttk.Entry(self.frm1)
        self.precio.configure(width=15)
        self.precio.grid(row=3, padx=20, pady=20 ,column=3)

        # Etiqueta fecha de compra del Producto
        self.lblFecha = ttk.Label(self.frm1)
        self.lblFecha.configure(text='Fecha', width=6)
        self.lblFecha.grid(row=3, padx=20, pady=20 ,column=4)

        # Captura la fecha de compra del Producto
        self.fecha = ttk.Entry(self.frm1)
        self.fecha.configure(width=10)
        self.fecha.grid(row=3, padx=20, pady=20 ,column=5)
        self.fecha.bind("<KeyRelease>", self.validaFecha)
        self.fecha.bind("<BackSpace>", self.borraFecha)

        # Separador
        self.separador2 = ttk.Separator(self.frm1)
        self.separador2.configure(orient="horizontal")
        self.separador2.grid(columnspan=6,padx=20, pady=20, row=4, sticky="nsew")

        # tablaTreeView
        self.style = ttk.Style()
        self.style.configure("estilo.Treeview", highlightthickness=0,
                             bd=0, background="#e0e0e0", font=('Calibri Light', 10))
        self.style.configure("estilo.Treeview.Heading",
                             background='Azure', font=('Calibri Light', 10, 'bold'))
        self.style.layout("estilo.Treeview", [
                          ('estilo.Treeview.treearea', {'sticky': 'nswe'})])

        # Árbol para mostrar los datos de la B.D.
        self.treeProductos = ttk.Treeview(self.frm1, style="estilo.Treeview")
        self.treeProductos.grid(row = 5, column = 0, columnspan= 6)
        self.treeProductos.configure(height=alto * 2 //100, selectmode="extended")


        # Etiquetas de las columnas para el TreeView
        self.treeProductos["columns"] = (
            "Codigo", "Descripcion", "Und", "Cantidad", "Precio", "Fecha")
        # Características de las columnas del árbol
        self.treeProductos.column(
            "#0",          anchor="w", stretch=True, width =ancho // 9)
        self.treeProductos.column(
            "Codigo",      anchor="w", stretch=True, width =ancho // 9)
        self.treeProductos.column(
            "Descripcion", anchor="w", stretch=True, width =ancho // 3)
        self.treeProductos.column(
            "Und",         anchor="w", stretch=True, width = ancho // 7)
        self.treeProductos.column(
            "Cantidad",    anchor="w", stretch=True, width = ancho // 12)
        self.treeProductos.column(
            "Precio",      anchor="w", stretch=True, width = ancho // 10)
        self.treeProductos.column(
            "Fecha",       anchor="w", stretch=True, width = ancho // 8)

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

        # Scrollbar en el eje Y de treeProductos
        # self.scrollbary = ttk.Scrollbar(
        #     self.treeProductos, orient='vertical', command=self.treeProductos.yview)
        # self.treeProductos.configure(yscroll=self.scrollbary.set)
        # self.scrollbary.grid(row=5, column=7)

        self.treeProductos.bind('<Double-1>', self.tree_seleccion)
        # Botón para Buscar un Proveedor
        self.btnBuscar = ttk.Button(self.frm2)
        self.btnBuscar.configure(text='Buscar',command=self.lee_treeProductos)
        self.btnBuscar.grid(row=6, column=0)

        # Botón para Guardar los datos
        self.btnGrabar = ttk.Button(self.frm2)
        self.btnGrabar.configure(text='Grabar',command = self.graba_Registro)
        self.btnGrabar.grid(row=6, column=1)

        # Botón para Editar los datos
        self.btnEditar = ttk.Button(self.frm2)
        self.btnEditar.configure(text='Editar',command = self.tree_seleccion)
        self.btnEditar.grid(row=6, column=2)

        # Botón para Elimnar datos
        self.btnEliminar = ttk.Button(self.frm2)
        self.btnEliminar.configure(text='Eliminar')
        self.btnEliminar.grid(row=6, column=3)

        # Botón para cancelar una operación
        self.btnCancelar = ttk.Button(self.frm2)
        self.btnCancelar.configure(
            text='Cancelar')
        self.btnCancelar.grid(row=6, column=4)

        self.frm1.pack()
        self.frm2.pack(padx=20, pady=20)
        self.main_frame.pack()
        self.tabs.pack()
        self.tabs.add(self.main_frame, compound="center", text="Ingreso de datos")

        self.win.pack(fill="both", expand="yes")
        # widget Principal del sistema
        self.mainwindow = self.win
            # widget Principal del sistema
        self.mainwindow = self.win

    def run(self):
        self.mainwindow.mainloop()

    ''' ......... Métodos utilitarios del sistema .............'''
    # Rutina de centrado de pantalla

    def centra(self, win, ancho, alto):
        """ centra las ventanas en la pantalla """
        x = win.winfo_screenwidth() // 2 - ancho // 2
        y = 0# win.winfo_screenheight() // 2 - alto // 2
        win.geometry(f'{ancho}x{alto}+{x}+{y}')
        win.deiconify()  # Se usa para restaurar la ventana
    # Operaciones con la base de datos
    def run_Query(self, query, parametros=()):
        ''' Función para ejecutar los Querys a la base de datos '''
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parametros)
            conn.commit()
        return result
    
    '''..............Validaciones del sistema..................'''

    # fecha, campos llenos
    def validaIdNit(self, event):
        ''' Valida que la longitud no sea mayor a 15 caracteres'''
        if event.char:
            if len(self.idNit.get()) > 15:
                mssg.showerror('Atención!!', '.. ¡Máximo 15 caracteres! ..')
                self.idNit.delete(15, 'end')
        # Tener en cuenta caso de copypast """
    
    def backslash(self, indice):
        self.fecha.insert(indice, "/")
        
    def validaFecha(self, event):
        ''' Valida la fecha'''
        if event:
            try:
                val = int(self.fecha.get()[(len(self.fecha.get())-1)])
            except ValueError:
                if self.fecha.get()[(len(self.fecha.get())-1)] == "/":
                    pass
                else:
                    mssg.showerror(
                        'Atención!!', '..Solo números en la fecha...')
                    self.fecha.delete((len(self.fecha.get())-1), 'end')
            # except IndexError:
            #     pass
            finally:
                if len(self.fecha.get()) == 2 or len(self.fecha.get()) == 5:
                    self.backslash(len(self.fecha.get()))

                elif len(self.fecha.get()) > 10:
                    mssg.showerror(
                        'Atención!!', '.. Un año no tiene más de 4 dígitos..')
                    self.fecha.delete(10, 'end')

    def borraFecha(self, event):
        ''' Si se borra la fecha elimina el backslash junto con el número anterior'''
        if event.char:
            if self.fecha.get()[(len(self.fecha.get())-1)] == "/":
                self.fecha.delete((len(self.fecha.get())-1), 'end')
    
    '''.................................No se....................................'''
    def limpiaCampos(self):
        ''' Limpia todos los campos de captura'''
        # Inventario.actualiza = None
        # self.idNit.config(state='normal')
        self.idNit.delete(0, 'end')
        self.razonSocial.delete(0, 'end')
        self.ciudad.delete(0, 'end')
        self.codigo.delete(0, 'end')
        self.descripcion.delete(0, 'end')
        self.unidad.delete(0, 'end')
        self.cantidad.delete(0, 'end')
        self.precio.delete(0, 'end')
        self.fecha.delete(0, 'end')
    '''.................................Botones....................................'''
    #Buscar
    def lee_treeProductos(self):
        ''' Carga los datos y Limpia la Tabla tablaTreeView '''
        tabla_TreeView = self.treeProductos.get_children()

        for linea in tabla_TreeView:
            self.treeProductos.delete(linea)  # Límpia la filas del TreeView

        # Seleccionando los datos de la BD
        db_rows = self.run_Query("""SELECT * FROM Proveedor pv INNER JOIN Productos pd ON pv.idNitProv= pd.idNit WHERE pv.idNitProv = ?""",(self.idNit.get(),))  #WHERE pv.idNitProv = 'hola';,(self.idNit.get(),)) db_rows contine la vista del query

        # # Insertando los datos de la BD en treeProductos de la pantalla
        for row in db_rows:
            self.treeProductos.insert('', 0, text=row[0], values=[
                                      row[4], row[5], row[6], row[7], row[8], row[9]])
    # Grabar
    def guardar_proveedor(self):
        # try except IntegrityError: UNIQUE constraint failed: Productos.idNit, Productos.Codigo
        self.run_Query(f""" INSERT INTO Proveedor (idNitProv,Razon_Social, Ciudad)
                    VALUES(?,?,?);""", (self.idNit.get(), self.razonSocial.get(), self.ciudad.get()))
        self.limpiaCampos()
        
    def guardar_productos(self):
        self.run_Query(f""" INSERT INTO Productos (idNit, Codigo, Descripcion, Und, Cantidad, Precio, Fecha)
                    VALUES(?,?,?,?,?,?,?);""", (self.idNit.get(), self.codigo.get(), self.descripcion.get(), self.unidad.get(), self.cantidad.get(), self.precio.get(), self.fecha.get()))
        self.limpiaCampos()

    def actualiza_productos(self):
        #contemplar que todo sea igual
        self.run_Query(f"""UPDATE Productos 
                       SET Descripcion= ?, Und= ?, Cantidad = ?, Precio = ?, Fecha = ? 
                       WHERE idNit = ? AND Codigo=? """,(self.descripcion.get(),self.unidad.get(),self.cantidad.get(),self.precio.get(),self.fecha.get(),self.idNit.get(), self.codigo.get()))
        
    def actualiza_proveedor(self):
        self.run_Query(f"""UPDATE Proveedor SET Razon_Social = ?, Ciudad = ? WHERE idNitProv = ?""", (self.razonSocial.get(), self.ciudad.get(),self.idNit.get()))
        
    def graba_Registro(self):
        '''Adiciona un producto a la BD si la validación es True'''        
        if self.idNit.get()=='':
            print('id vacío')
            if self.codigo.get()!='':
                print('advertencia de que falta proveedor')
                mssg.showerror('Atención!!', f'El producto debe corresponder con un proveedor si desea grabar')
            else:
                mssg.showerror('Atención!!', f'Id/Nit y código deben contener información si desea grabar')
        else:
            sameIdProv = (self.run_Query(f"""SELECT * from Proveedor WHERE idNitProv= ?;""",(self.idNit.get(),))).fetchall()
            print(sameIdProv)
            if sameIdProv:
                print('si hay')
                self.actualiza_proveedor()
                self.mensaje = 'actualizado'
            else: 
                print('pues no')
                self.guardar_proveedor()
                self.mensaje = 'guardado'
            
            if self.codigo.get() == '':
                mssg.showinfo(title='Grabación exitosa', message=f'El proveedor ha sido {self.mensaje}', icon='info')    
                self.limpiaCampos()
            else:  
                #ahora comprueba si la fecha está vacía             
                if self.fecha.get() == '':
                    mssg.showerror( 'Atención!!', f'.. la fecha no puede estar vacía si desea grabar')
                else:
                    sameId = (self.run_Query(f"""SELECT * from Productos WHERE idNit= ? AND Codigo= ?;""",(self.idNit.get(),self.codigo.get()))).fetchall()
                    print(sameId)
                    if sameId:
                        self.actualiza_productos()
                        mssg.showinfo(title='Grabación exitosa', message=f'El producto ha sido actualizado y el proveedor ha sido {self.mensaje}', icon='info')
                        
                    else:
                        self.guardar_productos()
                        mssg.showinfo(title='Grabación exitosa', message=f'El producto ha sido grabado y el proveedor ha sido {self.mensaje}', icon='info')
            


    #Editar
    def tree_seleccion(self, event=None):
        item_seleccionado = self.treeProductos.focus()
        fila = self.treeProductos.item(item_seleccionado)
        val = fila.get('values')
        # pv.Razon_Social,pv.Ciudad
        valProv = self.run_Query(
            f"""SELECT * FROM Proveedor pv INNER JOIN Productos pd ON pv.idNitProv= pd.idNit WHERE pv.idNitProv = ? AND pd.Codigo= ?;""",(fila.get('text'),val[0]))
        for row in valProv:
            print(row)
            self.limpiaCampos()
            self.idNit.insert(0, row[0])
            self.razonSocial.insert(0, row[1])
            self.ciudad.insert(0, row[2])
            self.codigo.insert(0, row[4])
            self.descripcion.insert(0, row[5])
            self.unidad.insert(0, row[6])
            self.cantidad.insert(0, row[7])
            self.precio.insert(0, row[8])
            self.fecha.insert(0, row[9])

if __name__ == "__main__":
    app = Inventario()
    app.run()