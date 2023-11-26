# !/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mssg
import sqlite3
from os import path, system, name
""" Módulo os: Proporciona funciones para interactuar con el sistema operativo."""

class Inventario:
    #Creación del constructor, inicializar la clase inventario, self hace referencia a la instancia actual de la clase
    #def es que se está creando/definiendo una función
    #self es la instancia de la clase dentro de sus métodos
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
        
        #Este método se utiliza para especificar si la ventana puede ser redimensionada en el ancho y en el alto. Los dos argumentos que recibe son booleanos que indican si se permite la redimensión en cada dirección.
        #ancho y alto
        self.win.resizable(True, True)

        # creación base de datos
        self.run_query("""CREATE TABLE IF NOT EXISTS 'Productos'(
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
        self.run_query("""CREATE TABLE IF NOT EXISTS 'Proveedor' (
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
        self.idNit.bind("<KeyRelease>", self.valida_idNit)
        
        self.idNit.focus_set()
        self.idNit.icursor(tk.END)

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
        self.cantidad.bind("<KeyRelease>",self.valida_cantidad)

        # Etiqueta precio del Producto
        self.lblPrecio = ttk.Label(self.frm1)
        self.lblPrecio.configure(text='Precio $', width=8)
        self.lblPrecio.place(anchor="nw", x=0.2*ancho, y=col3)

        # Captura el precio del Producto
        self.precio = ttk.Entry(self.frm1)
        self.precio.configure(width=15)
        self.precio.place(anchor="nw", x=0.26*ancho, y=col3)
        self.precio.bind("<KeyRelease>",self.valida_precio)

        # Etiqueta fecha de compra del Producto
        self.lblFecha = ttk.Label(self.frm1)
        self.lblFecha.configure(text='Fecha', width=6)
        self.lblFecha.place(anchor="nw", x=0.4*ancho, y=col3)

        """ La fecha se debe recibir en formato de fecha """
        # Captura la fecha de compra del Producto
        self.fecha = ttk.Entry(self.frm1)
        self.fecha.configure(width=10)
        self.fecha.place(anchor="nw", x=0.45*ancho, y=col3)
        self.fecha.bind("<KeyRelease>", self.entrada_fecha)
        self.fecha.bind("<BackSpace>", self.borra_fecha)

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
            "Descripcion", anchor="w", stretch=True, width=int(ancho*0.28))
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

        # Scrollbar en el eje Y de treeProductos
        self.scrollbary = ttk.Scrollbar(
            self.treeProductos, orient='vertical', command=self.treeProductos.yview)
        self.treeProductos.configure(yscroll=self.scrollbary.set)
        self.scrollbary.place(x=820, y=25, height=478)
        
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
        self.btnBuscar.configure(text='Buscar', command=self.buscar_prov)
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
        self.btnEliminar.configure(text='Eliminar', command = self.elimina_registro)
        self.btnEliminar.place(anchor="nw", width=bwidth,
                               x=int(ancho*0.27)+3*bwidth, y=col1_2)
        

        # Botón para cancelar una operación
        self.btnCancelar = ttk.Button(self.frm2)
        self.btnCancelar.configure(
            text='Cancelar', width=int(bwidth*0.12), command=self.limpia_campos)  
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
        """ Centra la ventana de tkinter
        Args:
            win (tkinter.Tk): La ventana donde se encuentran los frames
            ancho (int): Ancho de la ventana
            alto (int): Alto de la ventana
        """
        x = win.winfo_screenwidth() // 2 - ancho // 2
        y = 0# win.winfo_screenheight() // 2 - alto // 2
        win.geometry(f'{ancho}x{alto}+{x}+{y}')
        win.deiconify()  # Se usa para restaurar la ventana
    # Operaciones con la base de datos
    def run_query(self, query, parametros=()):
        ''' Función para ejecutar los Querys a la base de datos '''
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parametros)
            conn.commit()
        return result
    
    '''..............Validaciones del sistema..................'''

    # Id/Nit
    def valida_idNit(self, event):
        """ Valida que la longitud de Id/Nit no sea mayor a 15 caracteres 
        Args:
            event (tkinter.Event): El evento que recibe el entry"""
        if event.char:
            if len(self.idNit.get()) > 15:
                mssg.showerror('Atención!!', '.. ¡Máximo 15 caracteres! ..')
                self.idNit.delete(15, 'end')
    
    #Cantidad
    def valida_cantidad(self, event):
        """ Permite únicamente la entrada de dígitos a la cantidad
         Args:
            event (tkinter.Event): El evento que recibe el entry """
        if event.keysym == 'Tab':
            # No hacer nada si la tecla presionada es Tab
            return
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
    def valida_precio(self,event):
        """ Permite únicamente la entrada de dígitos al precio 
        Args:
            event (tkinter.Event): El evento que recibe el entry """
        if event.keysym == 'Tab':
            # No hacer nada si la tecla presionada es Tab
            return
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
    
    def entrada_fecha(self, event):
        ''' Le da formato dd/mm/aaaa a la fecha
        Args:
            event (tkinter.Event): El evento que recibe el entry '''
        for index, char in enumerate(self.fecha.get()):
            if index==2 and char != '/' or index == 5 and char != '/' :
                self.fecha.delete(index, 'end')
            elif char.isdigit():
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
             

    def borra_fecha(self, event):
        ''' Si se borra la fecha elimina el backslash junto con el número anterior
        Args:
            event (tkinter.Event): El evento que recibe el entry'''
        if event.char:
            if self.fecha.get()[(len(self.fecha.get())-1)] == "/":
                self.fecha.delete((len(self.fecha.get())-1), 'end')
    
    def es_fecha_valida(self):
        """ Revisa que la fecha exista y este entre los año 1000 hasta 2030

        Returns:
            Boolean : Retorna True si la fecha es válida y False si la fecha no existe
        """
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
    
    '''.................................Botones....................................'''
    def limpia_campos(self):
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

    def lee_treeProductos(self, top_producto = ''):
        if top_producto=='' and self.codigo.get() != '':
            top_producto = self.codigo.get()
        ''' Carga los datos y Limpia la Tabla tablaTreeView '''
        tabla_TreeView = self.treeProductos.get_children()

        for linea in tabla_TreeView:
            self.treeProductos.delete(linea)  # Límpia la filas del TreeView
            
        #Obtener el producto asociado al top_producto
        db_top_product = self.run_query("""
            SELECT * FROM Proveedor pv 
            INNER JOIN Productos pd ON pv.idNitProv = pd.idNit 
            WHERE pv.idNitProv = ? AND pd.Codigo = ?
            """, (self.idNit.get(),top_producto))

        # Obtener el resto de los productos excluyendo el top_producto
        db_rows = self.run_query("""
            SELECT * FROM Proveedor pv 
            INNER JOIN Productos pd ON pv.idNitProv = pd.idNit 
            WHERE pv.idNitProv = ? AND pd.Codigo != ?
            """, (self.idNit.get(),top_producto))
    
        for row in db_top_product:
            self.treeProductos.insert('', 1, text=row[0], values=[
                                      row[4], row[5], row[6], row[7], row[8], row[9]])
        for row in db_rows:
            self.treeProductos.insert('', 1, text=row[0], values=[
                                      row[4], row[5], row[6], row[7], row[8], row[9]])
    
    
    #Buscar
    def buscar_prov(self):
        if self.idNit.get() != '':
            self.existe_prov = self.run_query(f"""SELECT * from Proveedor WHERE idNitProv= ?;""",(self.idNit.get(),)).fetchall() 
            self.existen_prod = self.run_query(f"""SELECT * from Productos WHERE idNit= ?;""",(self.idNit.get(),)).fetchone() 
            if self.existe_prov:
                self.lee_treeProductos()
                self.limpia_campos()
                self.idNit.insert(0,self.existe_prov[0][0])
                self.razonSocial.insert(0,self.existe_prov[0][1])
                self.ciudad.insert(0,self.existe_prov[0][2])
                
            else:
                mssg.showinfo(title='Buscar', message=f'El provedor no existe en la base de datos', icon='info')
       
    # Grabar
    def guardar_proveedor(self):    
        self.run_query(f""" INSERT INTO Proveedor (idNitProv,Razon_Social, Ciudad)
                    VALUES(?,?,?);""", (self.idNit.get(), self.razonSocial.get(), self.ciudad.get()))
        
    def guardar_productos(self):
        self.run_query(f""" INSERT INTO Productos (idNit, Codigo, Descripcion, Und, Cantidad, Precio, Fecha)
                    VALUES(?,?,?,?,?,?,?);""", (self.idNit.get(), self.codigo.get(), self.descripcion.get(), self.unidad.get(), self.cantidad.get(), self.precio.get(), self.fecha.get()))

    def actualiza_productos(self):
        #contemplar que todo sea igual
        self.run_query(f"""UPDATE Productos 
                       SET Descripcion= ?, Und= ?, Cantidad = ?, Precio = ?, Fecha = ? 
                       WHERE idNit = ? AND Codigo=? """,(self.descripcion.get(),self.unidad.get(),self.cantidad.get(),self.precio.get(),self.fecha.get(),self.idNit.get(), self.codigo.get()))
        
    def actualiza_proveedor(self):
        self.run_query(f"""UPDATE Proveedor SET Razon_Social = ?, Ciudad = ? WHERE idNitProv = ?""", (self.razonSocial.get(), self.ciudad.get(),self.idNit.get()))

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
            self.sameIdProv = (self.run_query(f"""SELECT * from Proveedor WHERE idNitProv= ?;""",(self.idNit.get(),))).fetchall() 
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
                            self.lee_treeProductos()
                            self.limpia_campos()
                    elif self.accion == 'guardar':
                        if self.pregunta('¿Desea guardar el proveedor?'):
                            self.guardar_proveedor()
                            mssg.showinfo(title='Grabación exitosa', message=f' {self.mensaje}', icon='info')  
                            self.lee_treeProductos()             
                            self.limpia_campos()   
                             
                else:   
                    mssg.showinfo(title='Grabación no requerida', message=f'Los datos del proveedor ya existen en la base de datos', icon='info')  
                    self.lee_treeProductos()
            else:             
                if self.fecha.get() == '':
                    mssg.showerror( 'Atención!!', f'.. la fecha no puede estar vacía si desea grabar')
                else:
                    if self.es_fecha_valida():
                        precioG = float(self.precio.get()) if self.precio.get()!= '' else self.precio.get()
                        cantidadG = float(self.cantidad.get()) if self.cantidad.get()!='' else self.cantidad.get()
                        # print(float(self.cantidad.get())== self.sameId[0][4])
                        self.sameId = (self.run_query(f"""SELECT * from Productos WHERE idNit= ? AND Codigo= ?;""",(str(self.idNit.get()),str(self.codigo.get())))).fetchall()
                        if self.sameId:      
                            if str(self.descripcion.get()) == str(self.sameId[0][2])  and str(self.unidad.get()) == str(self.sameId[0][3]) and cantidadG == self.sameId[0][4] and precioG == self.sameId[0][5] and str(self.fecha.get())==str(self.sameId[0][6]):
                                if self.mensaje:
                                    if self.accion == 'actualizar':
                                        if self.pregunta('¿Desea actualizar el proveedor y conservar el producto?'):
                                            self.actualiza_proveedor()
                                            mssg.showinfo(title='Grabación exitosa', message=f'{self.mensaje}\nLos datos del producto han sido previamente grabados', icon='info')
                                            self.lee_treeProductos(self.codigo.get())             
                                            self.limpia_campos()  
                                
                                else:
                                    mssg.showinfo(title='Grabación no requerida', message=f'Los datos ingresados han sido previamente grabados', icon='info')
                                    self.lee_treeProductos()
                            else:
                                if self.mensaje:
                                    if self.accion == 'actualizar':
                                        if self.pregunta('¿Desea actualizar el proveedor y el producto?'):
                                            self.actualiza_proveedor()
                                            self.actualiza_productos()           
                                            mssg.showinfo(title='Grabación exitosa', message=f'{self.mensaje}\nEl producto ha sido actualizado', icon='info')
                                            self.lee_treeProductos(self.codigo.get())             
                                            self.limpia_campos()  
                                else:
                                    if self.pregunta('¿Desea actualizar el producto y conservar el proveedor?'):
                                        self.actualiza_productos()
                                        mssg.showinfo(title='Grabación exitosa', message=f'El producto ha sido actualizado', icon='info')
                                        self.lee_treeProductos(self.codigo.get())             
                                        self.limpia_campos()  
                            
                        else:
                            if self.mensaje:
                                if self.accion == 'actualizar':
                                    if self.pregunta('¿Desea actualizar el proveedor y guardar el producto?'):
                                        self.actualiza_proveedor()
                                        self.guardar_productos()
                                        mssg.showinfo(title='Grabación exitosa', message=f'{self.mensaje}\nEl producto ha sido guardado', icon='info')  
                                        self.lee_treeProductos(self.codigo.get())             
                                        self.limpia_campos()  
                                
                                elif self.accion == 'guardar':
                                    if self.pregunta('¿Desea guardar el proveedor y el producto?'):
                                        self.guardar_proveedor()
                                        self.guardar_productos()
                                        mssg.showinfo(title='Grabación exitosa', message=f'{self.mensaje}\nEl producto ha sido guardado', icon='info')     
                                        self.lee_treeProductos(self.codigo.get())             
                                        self.limpia_campos()   
                            else:
                                if self.pregunta('¿Desea guardar el producto y conservar el proveedor?'):
                                    self.guardar_productos()
                                    mssg.showinfo(title='Grabación exitosa', message=f'El producto ha sido guardado', icon='info')
                                    self.lee_treeProductos(self.codigo.get())             
                                    self.limpia_campos()  
                    else:
                        mssg.showerror("Validación", "Fecha no válida")
    #Editar
    def tree_seleccion(self, event=None):
        item_seleccionado = self.treeProductos.focus()
        fila = self.treeProductos.item(item_seleccionado,'text')
        val = self.treeProductos.item(item_seleccionado,'values')
        if item_seleccionado:
            valProv = self.run_query(
                f"""SELECT * FROM Proveedor pv INNER JOIN Productos pd ON pv.idNitProv= pd.idNit WHERE pv.idNitProv = ? AND pd.Codigo= ?;""",(fila,val[0]))
            for row in valProv:
                self.limpia_campos()
                self.idNit.insert(0, row[0])
                self.razonSocial.insert(0, row[1])
                self.ciudad.insert(0, row[2])
                self.codigo.insert(0, row[4])
                self.descripcion.insert(0, row[5])
                self.unidad.insert(0, row[6])
                self.cantidad.insert(0, row[7])
                self.precio.insert(0, row[8])
                self.fecha.insert(0, row[9])
            
    def deshabilitar_botones(self):
        self.btnBuscar.config(state='disabled')
        self.btnGrabar.config(state='disabled')
        self.btnEditar.config(state='disabled')
        self.btnEliminar.config(state='disabled')

    def habilitar_botones(self):
        self.btnBuscar.config(state='normal')
        self.btnGrabar.config(state='normal')
        self.btnEditar.config(state='normal')
        self.btnEliminar.config(state='normal')
    
    # Borrar
    def elimina_registro(self, event=None):
        self.deshabilitar_botones()
        self.ventana1 = tk.Toplevel(self.win)
        self.ventana1.title("Eliminación")
        self.seleccion = tk.IntVar(self.ventana1)
        ancho_ventana = 300 # Ancho en píxeles
        alto_ventana = 300 # Alto en píxeles
        self.ventana1.geometry(f"{ancho_ventana}x{alto_ventana}")

        self.radio1 = tk.Radiobutton(self.ventana1, text="Eliminar proveedor", variable=self.seleccion, value=1)
        self.radio1.grid(column=1, row=0)
        self.radio2 = tk.Radiobutton(self.ventana1, text="Eliminar los productos del proveedor", variable=self.seleccion, value=2)
        self.radio2.grid(column=1, row=1)
        self.radio2 = tk.Radiobutton(self.ventana1, text="Eliminar el producto especificado", variable=self.seleccion, value=3)
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
        self.entryid.bind("<KeyRelease>", self.valida_idNit)
        
        self.lblcod = ttk.Label(self.ventana1)
        self.lblcod.configure(text='Código', width=8, anchor = 'e')
        self.lblcod.grid(column = 0, row = 6)
        
        self.entrycod = tk.Entry(self.ventana1)
        self.entrycod.grid(column=1, row=6)
        self.entrycod.configure(width= 15)
        self.entrycod.insert(0, self.codigo.get())
        
        def on_close():
            self.habilitar_botones()
            self.ventana1.withdraw()

        self.ventana1.protocol("WM_DELETE_WINDOW", on_close)
        self.ventana1.wait_window()
        
    def borrar(self):
        id_nit = self.entryid.get()
        cod = self.entrycod.get()
        self.existe_prov = self.run_query("""SELECT * FROM Proveedor WHERE idNitProv = ?""", (id_nit,)).fetchall()
        self.existen_prod = self.run_query(f"""SELECT * from Productos WHERE idNit= ?;""",(id_nit,)).fetchone()
        self.existe_prod = self.run_query("SELECT * from Productos WHERE idNit= ? AND Codigo= ?;", (id_nit, cod)).fetchall()
        if id_nit == '':
            mssg.showerror('Error', 'Debes ingresar un Id/Nit de proveedor para eliminar.')
        else:
            if self.seleccion.get() == 1:                    
                if self.pregunta('¿Estás seguro de eliminar el proveedor y sus productos?', 'Confirmar acción'):
                    if self.existe_prov:
                        self.run_query("DELETE FROM Proveedor WHERE idNitProv = ?", (id_nit,))
                        self.run_query("DELETE FROM Productos WHERE idNit = ?", (id_nit,))
                        mssg.showinfo('Éxito', 'El proveedor y sus productos se han eliminado con éxito.')
                        self.ventana1.withdraw()  # Withdraw the window
                        self.limpia_campos()
                        self.habilitar_botones()
                    else:
                        mssg.showinfo('Eliminar', 'No existe el proveedor en la base de datos')
                self.ventana1.withdraw()  # Withdraw the window
                self.limpia_campos()
                self.habilitar_botones()
            elif self.seleccion.get() == 2:
                if self.pregunta('¿Estás seguro de eliminar los productos del proveedor?', 'Confirmar acción'):
                    if self.existe_prov:
                        if self.existen_prod:   
                            self.run_query("DELETE FROM Productos WHERE idNit = ? ", (id_nit,))
                            mssg.showinfo('Éxito', 'Los productos del proveedor se han eliminado con éxito.')
                        else: 
                            mssg.showinfo('Eliminar', 'El proveedor no tiene productos')   
                    else:
                        mssg.showinfo('Eliminar', 'No existe el proveedor en la base de datos')
                    
                self.ventana1.withdraw()  # Withdraw the window
                self.limpia_campos()
                self.habilitar_botones()
                
            elif self.seleccion.get() == 3:
                if cod == '':
                    mssg.showerror('Error', 'Debes ingresar un código para eliminar.')
                else:
                    if self.pregunta('¿Estás seguro de eliminar este producto del proveedor?', 'Confirmar acción'):
                        if self.existen_prod:
                            if self.existe_prod:
                                self.run_query("DELETE FROM Productos WHERE idNit = ? AND Codigo = ?", (id_nit, cod))
                                mssg.showinfo('Éxito', 'El producto se ha eliminado con éxito.')
                            else:
                                mssg.showinfo('Eliminar', 'El producto no existe.')
                        else:
                            mssg.showinfo('Eliminar', 'El proveedor no tiene productos')
                    self.ventana1.withdraw()  # Withdraw the window
                    self.limpia_campos()
                    self.habilitar_botones()
   
if __name__ == "__main__":
    app = Inventario()
    app.run()