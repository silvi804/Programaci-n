# !/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mssg
import sqlite3
from os import path, system, name
""" Módulo os: Proporciona funciones para interactuar con el sistema operativo."""

class Inventario:
    def __init__(self, master=None):
        """ No olvidar lo de actualiza """
        self.mpath = r'X:/Users/ferna/Documents/UNal/Alumnos/2023_S2/ProyInventario'
        # Crea ventana principal
        self.win = tk.Tk()
        self.win.title("Manejo de Proveedores")
        
        absFilePath = path.abspath(__file__)
        mpath, filename = path.split(absFilePath)
        self.win.iconbitmap(mpath+r'/f2.ico')
        self.db_name = mpath+r'/Inventario.db'
            
        self.win.resizable(True, True)

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
        self.cantidad.bind("<KeyRelease>",self.validaCantidad)

        # Etiqueta precio del Producto
        self.lblPrecio = ttk.Label(self.frm1)
        self.lblPrecio.configure(text='Precio $', width=8)
        self.lblPrecio.place(anchor="nw", x=0.2*ancho, y=col3)

        # Captura el precio del Producto
        self.precio = ttk.Entry(self.frm1)
        self.precio.configure(width=15)
        self.precio.place(anchor="nw", x=0.26*ancho, y=col3)
        self.precio.bind("<KeyRelease>",self.validaPrecio)

        # Etiqueta fecha de compra del Producto
        self.lblFecha = ttk.Label(self.frm1)
        self.lblFecha.configure(text='Fecha', width=6)
        self.lblFecha.place(anchor="nw", x=0.4*ancho, y=col3)

        """ La fecha se debe recibir en formato de fecha """
        # Captura la fecha de compra del Producto
        self.fecha = ttk.Entry(self.frm1)
        self.fecha.configure(width=10)
        self.fecha.place(anchor="nw", x=0.45*ancho, y=col3)
        self.fecha.bind("<KeyRelease>", self.entradaFecha)
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
        self.btnEliminar.configure(text='Eliminar', command = self.eliminaRegistro)
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

    # Id/Nit
    def validaIdNit(self, event):
        ''' Valida que la longitud no sea mayor a 15 caracteres'''
        if event.char:
            if len(self.idNit.get()) > 15:
                mssg.showerror('Atención!!', '.. ¡Máximo 15 caracteres! ..')
                self.idNit.delete(15, 'end')
        # Tener en cuenta caso de copypast """
    
    #Unidad
    def validaCantidad(self,event):
        try:
            valC = float(self.cantidad.get())
        except ValueError:
            mssg.showerror('Atención!!','...Solo números en la cantidad...')
            for index, char in enumerate(self.cantidad.get()):
                if char.isdigit() or char == '.':
                    pass
                else:
                    self.cantidad.delete(index,'end')            
                
    #Precio
    def validaPrecio(self,event):
        try:
            valP = float(self.precio.get())
        except ValueError:
            mssg.showerror('Atención!!','...Solo números en el precio...')
            for index, char in enumerate(self.precio.get()):
                if char.isdigit() or char == '.':
                    pass
                else:
                    self.cantidad.delete(index,'end')            
                     
    #Fecha
    def backslash(self, indice):
        self.fecha.insert(indice, "/")
    
    def entradaFecha(self, event):
        ''' Valida la fecha'''
        for index, char in enumerate(self.fecha.get()):
                if char.isdigit():
                    if len(self.fecha.get()) == 2 or len(self.fecha.get()) == 5:
                        self.backslash(len(self.fecha.get()))
                    elif len(self.fecha.get()) > 10:
                        mssg.showerror(
                            'Atención!!', '.. Un año no tiene más de 4 dígitos..')
                        self.fecha.delete(10, 'end')
                elif char == '/':
                    if index== 2 or index== 5:
                        pass
                    else:
                        mssg.showerror("Atención!!","El símbolo '/' solo debe ingresarlo el programa")
                        self.fecha.delete(index,'end')
                else:
                    mssg.showerror(
                    'Atención!!', '..Solo números en la fecha...')
                    self.fecha.delete(index, 'end')
             
                    
  
                    
    # def entradaFecha(self, event):
    #     ''' Valida la fecha'''
    #     if event:
    #         try:
    #             val = int(self.fecha.get()[(len(self.fecha.get())-1)])
    #         except ValueError:
    #             if self.fecha.get()[(len(self.fecha.get())-1)] == "/":
    #                 pass
    #             else:
    #                 mssg.showerror(
    #                     'Atención!!', '..Solo números en la fecha...')
    #                 self.fecha.delete((len(self.fecha.get())-1), 'end')
    #         # except IndexError:
    #         #     pass
    #         finally:
    #             if len(self.fecha.get()) == 2 or len(self.fecha.get()) == 5:
    #                 self.backslash(len(self.fecha.get()))

    #             elif len(self.fecha.get()) > 10:
    #                 mssg.showerror(
    #                     'Atención!!', '.. Un año no tiene más de 4 dígitos..')
    #                 self.fecha.delete(10, 'end')

    def borraFecha(self, event):
        ''' Si se borra la fecha elimina el backslash junto con el número anterior'''
        if event.char:
            if self.fecha.get()[(len(self.fecha.get())-1)] == "/":
                self.fecha.delete((len(self.fecha.get())-1), 'end')
    
    def es_fecha_valida(self):
        try:
            date_str = self.fecha.get()
            dia, mes, año = map(int, date_str.split('/'))
            fechaValida = False
            if 1 <= mes <= 12:
                if mes in [1, 3, 5, 7, 8, 10, 12]:
                    if 1 <= dia <= 31 and 1000 <= año <= 2030:
                        fechaValida= True
                elif mes in [4, 6, 9, 11]:
                    if 1 <= dia <= 30 and 1000 <= año <= 2030:
                        fechaValida= True
                elif mes == 2:
                    if (año % 4 == 0 and año % 100 != 0) or (año % 4 == 0 and año % 400 == 0):
                        if 1 <= dia <= 29 and 1000 <= año <= 2030:
                            fechaValida= True
                    elif 1 <= dia <=28 and 1000 <= año <= 2030:
                        fechaValida= True
        except ValueError:
            fechaValida = False
        finally:
            return fechaValida
            
            
    
    '''.................................No se....................................'''
    def limpiaCampos(self):
        ''' Limpia todos los campos de captura'''
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
                                      str(row[4]), row[5], row[6], row[7], row[8], row[9]])
    # Grabar
    def guardar_proveedor(self):
        # try except IntegrityError: UNIQUE constraint failed: Productos.idNit, Productos.Codigo
        self.run_Query(f""" INSERT INTO Proveedor (idNitProv,Razon_Social, Ciudad)
                    VALUES(?,?,?);""", (self.idNit.get(), self.razonSocial.get(), self.ciudad.get()))
        
    def guardar_productos(self):
        self.run_Query(f""" INSERT INTO Productos (idNit, Codigo, Descripcion, Und, Cantidad, Precio, Fecha)
                    VALUES(?,?,?,?,?,?,?);""", (self.idNit.get(), self.codigo.get(), self.descripcion.get(), self.unidad.get(), self.cantidad.get(), self.precio.get(), self.fecha.get()))

    def actualiza_productos(self):
        #contemplar que todo sea igual
        self.run_Query(f"""UPDATE Productos 
                       SET Descripcion= ?, Und= ?, Cantidad = ?, Precio = ?, Fecha = ? 
                       WHERE idNit = ? AND Codigo=? """,(self.descripcion.get(),self.unidad.get(),self.cantidad.get(),self.precio.get(),self.fecha.get(),self.idNit.get(), self.codigo.get()))
        
    def actualiza_proveedor(self):
        self.run_Query(f"""UPDATE Proveedor SET Razon_Social = ?, Ciudad = ? WHERE idNitProv = ?""", (self.razonSocial.get(), self.ciudad.get(),self.idNit.get()))

    def pregunta(self, texto , titulo='Grabación'):
        self.preguntar = mssg.askquestion(f'{titulo}',f'{texto}')
        self.respuesta = True if self.preguntar == 'yes' else False
        return self.respuesta

    
    def graba_Registro(self):
        '''Adiciona un producto a la BD si la validación es True'''        
        if self.idNit.get()=='':
            if self.codigo.get()!='':
                print('advertencia de que falta proveedor')
                mssg.showerror('Atención!!', f'El producto debe corresponder con un proveedor si desea grabar')
            else:
                mssg.showerror('Atención!!', f'Id/Nit y código deben contener información si desea grabar')
                
        else:
            self.sameIdProv = (self.run_Query(f"""SELECT * from Proveedor WHERE idNitProv= ?;""",(self.idNit.get(),))).fetchall() 
            self.mensaje = ''
            self.accion = ''
            if self.sameIdProv:    
                if str(self.razonSocial.get()) == str(self.sameIdProv[0][1]) and str(self.ciudad.get()) == str(self.sameIdProv[0][2]):
                    pass  
                else:
                    self.accion = 'actualizar'
                    self.mensaje = 'El proveedor ha sido actualizado'
            else: 
                self.accion = 'guardar'
                self.mensaje = 'El proveedor ha sido guardado'
        
            if self.codigo.get() == '':
                if self.mensaje:
                    if self.accion == 'actualizar':
                        if self.pregunta('¿Desea actualizar el proveedor?'):
                            self.actualiza_proveedor()
                            mssg.showinfo(title='Grabación exitosa', message=f' {self.mensaje}', icon='info')
                            self.limpiaCampos()
                    elif self.accion == 'guardar':
                        if self.pregunta('¿Desea guardar el proveedor?'):
                            self.guardar_proveedor()
                            mssg.showinfo(title='Grabación exitosa', message=f' {self.mensaje}', icon='info')  
                            self.limpiaCampos()                 
                else:   
                    mssg.showinfo(title='Grabación no requerida', message=f'Los datos del proveedor ya existen en la base de datos', icon='info')  
            else:             
                if self.fecha.get() == '':
                    mssg.showerror( 'Atención!!', f'.. la fecha no puede estar vacía si desea grabar')
                else:
                    if self.es_fecha_valida():
                        self.sameId = (self.run_Query(f"""SELECT * from Productos WHERE idNit= ? AND Codigo= ?;""",(str(self.idNit.get()),str(self.codigo.get())))).fetchall()
                        if self.sameId:
                            if str(self.descripcion.get()) == str(self.sameId[0][2])  and str(self.unidad.get()) == str(self.sameId[0][3]) and float(self.cantidad.get()) == float(self.sameId[0][4]) and float(self.precio.get()) == float(self.sameId[0][5]) and str(self.fecha.get())==str(self.sameId[0][6]):
                                if self.mensaje:
                                    if self.accion == 'actualizar':
                                        if self.pregunta('¿Desea actualizar el proveedor y conservar el producto?'):
                                            self.actualiza_proveedor()
                                            mssg.showinfo(title='Grabación exitosa', message=f'{self.mensaje}\nLos datos del producto han sido previamente grabados', icon='info')
                                            self.limpiaCampos()
                                
                                else:
                                    mssg.showinfo(title='Grabación no requerida', message=f'Los datos ingresados han sido previamente grabados', icon='info')
                            else:
                                if self.mensaje:
                                    if self.accion == 'actualizar':
                                        if self.pregunta('¿Desea actualizar el proveedor y el producto?'):
                                            self.actualiza_proveedor()
                                            self.actualiza_productos()           
                                            mssg.showinfo(title='Grabación exitosa', message=f'{self.mensaje}\nEl producto ha sido actualizado', icon='info')
                                            self.limpiaCampos()
                                else:
                                    if self.pregunta('¿Desea actualizar el producto y conservar el proveedor?'):
                                        self.actualiza_productos()
                                        mssg.showinfo(title='Grabación exitosa', message=f'El producto ha sido actualizado', icon='info')
                                        self.limpiaCampos()
                            
                        else:
                            if self.mensaje:
                                if self.accion == 'actualizar':
                                    if self.pregunta('¿Desea actualizar el proveedor y guardar el producto?'):
                                        self.actualiza_proveedor()
                                        self.guardar_productos()
                                        mssg.showinfo(title='Grabación exitosa', message=f'{self.mensaje}\nEl producto ha sido guardado', icon='info')  
                                        self.limpiaCampos()     
                                
                                elif self.accion == 'guardar':
                                    if self.pregunta('¿Desea guardar el proveedor y el producto?'):
                                        self.guardar_proveedor()
                                        self.guardar_productos()
                                        mssg.showinfo(title='Grabación exitosa', message=f'{self.mensaje}\nEl producto ha sido guardado', icon='info')     
                                        self.limpiaCampos()  
                            
                            
                            else:
                                if self.pregunta('¿Desea guardar el producto y conservar el proveedor?'):
                                    self.guardar_productos()
                                    mssg.showinfo(title='Grabación exitosa', message=f'El producto ha sido guardado', icon='info')
                                    self.limpiaCampos()
                    else:
                        mssg.showerror("Validación", "Fecha no válida")
    #Editar
    def tree_seleccion(self, event=None):
        item_seleccionado = self.treeProductos.focus()
        fila = self.treeProductos.item(item_seleccionado)
        val = fila.get('values')
        # pv.Razon_Social,pv.Ciudad
        if fila:
            valProv = self.run_Query(
                f"""SELECT * FROM Proveedor pv INNER JOIN Productos pd ON pv.idNitProv= pd.idNit WHERE pv.idNitProv = ? AND pd.Codigo= ?;""",(fila.get('text'),val[0]))
            for row in valProv:
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
            
    # Borrar
    def eliminaRegistro(self, event=None):

        self.ventana1 = tk.Tk()
        self.seleccion = tk.IntVar(self.ventana1, 2)
        ancho_ventana = 300 # Ancho en píxeles
        alto_ventana = 300 # Alto en píxeles
        self.ventana1.geometry(f"{ancho_ventana}x{alto_ventana}")

        self.radio1 = tk.Radiobutton(self.ventana1, text="Eliminar proveedor", variable=self.seleccion, value=1 ,anchor='w')
        self.radio1.grid(column=1, row=0)
        self.radio2 = tk.Radiobutton(self.ventana1, text="Eliminar los productos del proveedor", variable=self.seleccion, value=2 ,anchor='w')
        self.radio2.grid(column=1, row=1)
        self.radio2 = tk.Radiobutton(self.ventana1, text="Eliminar el producto especificado", variable=self.seleccion, value=3 ,anchor='w')
        self.radio2.grid(column=1, row=2)
        
        self.botonEliminar1 = tk.Button(self.ventana1, text="Eliminar", command=self.borrar)
        self.botonEliminar1.grid(column=1, row= 8)
        
        self.lblId = ttk.Label(self.ventana1)
        self.lblId.configure(text='Id/Nit', width=6, anchor = 'e')
        self.lblId.grid(column = 0, row = 5)
        self.entryid = tk.Entry(self.ventana1)
        self.entryid.grid(column=1, row=5)
        self.entryid.configure(width= 15)
        self.entryid.insert(0, self.idNit.get())
        self.entryid.bind("<KeyRelease>", self.validaIdNit)
        
        self.lblcod = ttk.Label(self.ventana1)
        self.lblcod.configure(text='Código', width=8, anchor = 'e')
        self.lblcod.grid(column = 0, row = 6)
        
        self.entrycod = tk.Entry(self.ventana1)
        self.entrycod.grid(column=1, row=6)
        self.entrycod.configure(width= 15)
        self.entrycod.insert(0, self.codigo.get())

    def borrar(self):
        id_nit = self.entryid.get()
        cod = self.entrycod.get()
        self.existe_prov = self.run_Query("""SELECT * FROM Proveedor WHERE idNitProv = ?""",(id_nit,)).fetchall()
        self.existe_prod = self.run_Query("SELECT * from Productos WHERE idNit= ? AND Codigo= ?;",(id_nit,cod)).fetchall()
        
        if id_nit == '':
            mssg.showerror('Error', 'Debes ingresar un Id/Nit de proveedor para eliminar.')
        else:
            if self.seleccion.get() == 1:
                if self.existe_prov:
                    if self.pregunta('¿Estás seguro de eliminar el proveedor y sus productos?', 'Confirmar acción'):
                        self.run_Query("DELETE FROM Proveedor WHERE idNitProv = ?", (id_nit,))
                        self.run_Query("DELETE FROM Productos WHERE idNit = ?", (id_nit,))
                        mssg.showinfo('Éxito', 'El proveedor y sus productos se han eliminado con éxito.')
                        self.ventana1.quit()
                        self.limpiaCampos()
                else:
                    mssg.showinfo('Eliminar', 'El proveedor no existe en la base de datos.')
                    self.ventana1.quit()
            elif self.seleccion.get() == 2:
                if self.existe_prov:
                    if self.pregunta('¿Estás seguro de eliminar los productos del proveedor?', 'Confirmar acción'):
                        self.run_Query("DELETE FROM Productos WHERE idNit = ? ", (id_nit,))
                        mssg.showinfo('Éxito', 'Los productos del proveedor se han eliminado con éxito.')
                        self.ventana1.quit()
                        self.limpiaCampos()
                else:
                    mssg.showinfo('Eliminar', 'El proveedor no existe en la base de datos.')
                    self.ventana1.quit()
            elif self.seleccion.get() == 3:
                if cod == '':
                    mssg.showerror('Error', 'Debes ingresar un código para eliminar.')
                else:
                    if self.existe_prov:
                        if self.existe_prod:
                            if self.pregunta('¿Estás seguro de eliminar los productos del proveedor?', 'Confirmar acción'):
                                self.run_Query("DELETE FROM Productos WHERE idNit = ? AND Codigo = ?", (id_nit,cod))
                                mssg.showinfo('Éxito', 'El producto se ha eliminado con éxito.')
                                self.ventana1.quit()
                                self.limpiaCampos()
                        else:
                            mssg.showinfo('Eliminar', 'El código de el producto no existe en la base de datos.')
                            self.ventana1.quit()
                    else:
                        mssg.showinfo('Eliminar', 'El proveedor no existe en la base de datos.')
                        self.ventana1.quit()
                        
                
            

if __name__ == "__main__":
    app = Inventario()
    app.run()