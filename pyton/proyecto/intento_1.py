# !/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mssg
import sqlite3


class Inventario:
    def __init__(self, master=None):
        """ No olvidar lo de actualiza """
        # Crea ventana principal
        self.win = tk.Tk()
        self.win.title("Manejo de Proveedores")
        self.win.iconbitmap(r"f2.ico")
        self.db_name = 'Inventario.db'
        # self.win.resizable(False, False)

        # creación base de datos
        self.run_Query("""CREATE TABLE IF NOT EXISTS 'Productos'(
            idNit VARCHAR(15),
            Codigo VARCHAR(10),
            Descripcion VARCHAR(100),
            Und VARCHAR(19),
            Cantidad DOUBLE,
            Precio DOUBLE,
            Fecha DATE,
            PRIMARY KEY(idNit,Codigo),
            FOREIGN KEY(idNit) REFERENCES Proveedor(idNitProv)
            );""")
        self.run_Query("""CREATE TABLE IF NOT EXISTS 'Proveedor' (
            idNitProv VARCHAR(15) NOT NULL ,
            Razon_Social VARCHAR(100),
            Ciudad VARCHAR(20)
            );""")

        # PRIMARY KEY(idNitProv)
        # Establece dimensiones ventana
        pix_ancho = self.win.winfo_screenwidth()
        pix_alto = self.win.winfo_screenheight()
        ancho = int(pix_ancho*0.65)
        alto = int(pix_alto*0.9)
        fila1 = int(alto*0.32)
        col1 = int(fila1*0.15)
        col2 = col1*3
        col3 = col1*4
        fil2 = int(alto*0.12)
        col1_2 = int(fil2 * 0.1)
        bwidth = int(ancho*0.084)

        self.win.geometry(f"{ancho}x{alto}")

        # Centra la pantalla
        self.centra(self.win, ancho, alto)

        # Contenedor de widgets
        self.win = tk.LabelFrame(master)
        self.win.configure(background="#e0e0e0", font="{Arial} 12 {bold}",
                           height=ancho, labelanchor="n", width=alto)
        self.tabs = ttk.Notebook(self.win)
        self.tabs.configure(height=int(alto*0.95), width=int(ancho*0.96))

        # Frame de datos
        self.frm1 = ttk.Frame(self.tabs)
        self.frm1.configure(height=fila1, width=ancho)

        # Etiqueta IdNit del Proveedor
        self.lblIdNit = ttk.Label(self.frm1)
        self.lblIdNit.configure(text='Id/Nit', width=6)
        self.lblIdNit.place(anchor="nw", x=0.01*ancho, y=col1)

        """ Ubicar el mouse en el inicio """
        # Captura IdNit del Proveedor
        self.idNit = ttk.Entry(self.frm1)
        self.idNit.configure(takefocus=True)
        self.idNit.place(anchor="nw", x=0.05*ancho, y=col1)
        self.idNit.bind("<KeyRelease>", self.validaIdNit)

        """ No se que hace """
        self.idNit.bind("<BackSpace>", lambda _: self.idNit.delete(
            len(self.idNit.get())), 'end')

        # Etiqueta razón social del Proveedor
        self.lblRazonSocial = ttk.Label(self.frm1)
        self.lblRazonSocial.configure(text='Razon social', width=12)
        self.lblRazonSocial.place(anchor="nw", x=0.25*ancho, y=col1)

        # Captura razón social del Proveedor
        self.razonSocial = ttk.Entry(self.frm1)
        self.razonSocial.configure(width=36)
        self.razonSocial.place(anchor="nw", x=0.35*ancho, y=col1)

        # Etiqueta ciudad del Proveedor
        self.lblCiudad = ttk.Label(self.frm1)
        self.lblCiudad.configure(text='Ciudad', width=7)
        self.lblCiudad.place(anchor="nw", x=0.65*ancho, y=col1)

        # Captura ciudad del Proveedor
        self.ciudad = ttk.Entry(self.frm1)
        self.ciudad.configure(width=30)
        self.ciudad.place(anchor="nw", x=0.71*ancho, y=col1)

        # Separador
        self.separador1 = ttk.Separator(self.frm1)
        self.separador1.configure(orient="horizontal")
        self.separador1.place(anchor="nw", width=ancho, x=0, y=2*col1)

        """ Entre primer y segundo separador"""
        # Etiqueta Código del Producto
        self.lblCodigo = ttk.Label(self.frm1)
        self.lblCodigo.configure(text='Código', width=7)
        self.lblCodigo.place(anchor="nw", x=0.01*ancho, y=col2)

        # Captura el código del Producto
        self.codigo = ttk.Entry(self.frm1)
        self.codigo.configure(width=13)
        self.codigo.place(anchor="nw", x=0.07*ancho, y=col2)

        # Etiqueta descripción del Producto
        self.lblDescripcion = ttk.Label(self.frm1)
        self.lblDescripcion.configure(text='Descripción', width=11)
        self.lblDescripcion.place(anchor="nw", x=0.25*ancho, y=col2)

        # Captura la descripción del Producto
        self.descripcion = ttk.Entry(self.frm1)
        self.descripcion.configure(width=36)
        self.descripcion.place(anchor="nw", x=0.33*ancho, y=col2)

        # Etiqueta unidad o medida del Producto
        self.lblUnd = ttk.Label(self.frm1)
        self.lblUnd.configure(text='Unidad', width=7)
        self.lblUnd.place(anchor="nw", x=0.65*ancho, y=col2)

        # Captura la unidad o medida del Producto
        self.unidad = ttk.Entry(self.frm1)
        self.unidad.configure(width=10)
        self.unidad.place(anchor="nw", x=0.71*ancho, y=col2)

        # Etiqueta cantidad del Producto
        self.lblCantidad = ttk.Label(self.frm1)
        self.lblCantidad.configure(text='Cantidad', width=8)
        self.lblCantidad.place(anchor="nw", x=0.01*ancho, y=col3)

        # Captura la cantidad del Producto
        self.cantidad = ttk.Entry(self.frm1)
        self.cantidad.configure(width=12)
        self.cantidad.place(anchor="nw", x=0.08*ancho, y=col3)

        # Etiqueta precio del Producto
        self.lblPrecio = ttk.Label(self.frm1)
        self.lblPrecio.configure(text='Precio $', width=8)
        self.lblPrecio.place(anchor="nw", x=0.2*ancho, y=col3)

        # Captura el precio del Producto
        self.precio = ttk.Entry(self.frm1)
        self.precio.configure(width=15)
        self.precio.place(anchor="nw", x=0.26*ancho, y=col3)

        # Etiqueta fecha de compra del Producto
        self.lblFecha = ttk.Label(self.frm1)
        self.lblFecha.configure(text='Fecha', width=6)
        self.lblFecha.place(anchor="nw", x=0.4*ancho, y=col3)

        """ La fecha se debe recibir en formato de fecha """
        # Captura la fecha de compra del Producto
        self.fecha = ttk.Entry(self.frm1)
        self.fecha.configure(width=10)
        self.fecha.place(anchor="nw", x=0.45*ancho, y=col3)
        self.fecha.bind("<KeyRelease>", self.validaFecha)
        self.fecha.bind("<BackSpace>", self.borraFecha)

        # Separador
        self.separador2 = ttk.Separator(self.frm1)
        self.separador2.configure(orient="horizontal")
        self.separador2.place(
            anchor="nw", width=int(ancho*0.96), x=0, y=col1*5)

        """ Aquí inicia el Treeview """

        """ No se que hace acá """
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
        self.treeProductos.place(
            anchor="nw", height=int(alto*0.6), width=int(ancho*0.94), x=int(ancho*0.01), y=int(col1*5.5))

        # Etiquetas de las columnas para el TreeView
        self.treeProductos["columns"] = (
            "Codigo", "Descripcion", "Und", "Cantidad", "Precio", "Fecha")
        # Características de las columnas del árbol
        self.treeProductos.column(
            "#0",          anchor="w", stretch=True, width=int(ancho*0.035))
        self.treeProductos.column(
            "Codigo",      anchor="w", stretch=True, width=int(ancho*0.035))
        self.treeProductos.column(
            "Descripcion", anchor="w", stretch=True, width=int(ancho*0.35))
        self.treeProductos.column(
            "Und",         anchor="w", stretch=True, width=int(ancho*0.035))
        self.treeProductos.column(
            "Cantidad",    anchor="w", stretch=True, width=int(ancho*0.035))
        self.treeProductos.column(
            "Precio",      anchor="w", stretch=True, width=int(ancho*0.07))
        self.treeProductos.column(
            "Fecha",       anchor="w", stretch=True, width=int(ancho*0.035))

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
        """  self.scrollbary = ttk.Scrollbar(
            self.treeProductos, orient='vertical', command=self.treeProductos.yview)
        self.treeProductos.configure(yscroll=self.scrollbary.set)
        self.scrollbary.place(x=778, y=25, height=478) """
        
        self.treeProductos.bind('<Double-1>', self.tree_seleccion)

        # Título de la pestaña Ingreso de Datos
        self.frm1.pack(side="top")
        self.tabs.add(self.frm1, compound="center", text='Ingreso de datos')
        self.tabs.pack(side="top")

        # Frame 2 para contener los botones
        self.frm2 = ttk.Frame(self.win)
        self.frm2.configure(height=fil2, width=ancho)

        # Botón para Buscar un Proveedor
        self.btnBuscar = ttk.Button(self.frm2)
        self.btnBuscar.configure(text='Buscar', command=self.lee_treeProductos)
        self.btnBuscar.place(anchor="nw", width=bwidth,
                             x=int(ancho*0.24), y=col1_2)

        """ Cuando se digite el dato que el espacio vuelva a quedar vacío """
        # Botón para Guardar los datos
        self.btnGrabar = ttk.Button(self.frm2)
        self.btnGrabar.configure(text='Grabar',command = self.graba_Registro)
        self.btnGrabar.place(anchor="nw", width=bwidth,
                             x=int(ancho*0.25)+bwidth, y=col1_2)
        # self.btnGrabar.bind('<Button-1>', self.guardar_datos)

        # Botón para Editar los datos
        self.btnEditar = ttk.Button(self.frm2)
        self.btnEditar.configure(text='Editar',command = self.tree_seleccion)
        self.btnEditar.place(anchor="nw", width=bwidth,
                             x=int(ancho*0.26)+2*bwidth, y=col1_2)

        # Botón para Elimnar datos
        self.btnEliminar = ttk.Button(self.frm2)
        self.btnEliminar.configure(text='Eliminar')
        self.btnEliminar.place(anchor="nw", width=bwidth,
                               x=int(ancho*0.27)+3*bwidth, y=col1_2)

        # Botón para cancelar una operación
        self.btnCancelar = ttk.Button(self.frm2)
        self.btnCancelar.configure(
            text='Cancelar', width=int(bwidth*0.12), command=self.limpiaCampos)  # , command=self.limpiaCampos
        self.btnCancelar.place(anchor="nw", width=bwidth,
                               x=int(ancho*0.28)+4*bwidth, y=col1_2)
        # self.btnGrabar.bind('<Button>', self.borrar_datos)

        # Ubicación del Frame 2
        self.frm2.place(anchor="nw", relwidth=1, y=col1*19)
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