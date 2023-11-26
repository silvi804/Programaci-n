'''comentaré lo que ya esta'''
# # Fución de manejo de eventos del sistema
#     def run(self):
#         self.mainwindow.mainloop()

#     ''' ......... Métodos utilitarios del sistema .............'''

#     # Rutina de centrado de pantalla
#     def centra(self, win, ancho, alto):
#         """ centra las ventanas en la pantalla """
#         x = win.winfo_screenwidth() // 2 - ancho // 2
#         y = 0  # win.winfo_screenheight() // 2 - alto // 2
#         win.geometry(f'{ancho}x{alto}+{x}+{y}')
#         win.deiconify()  # Se usa para restaurar la ventana

    # Operaciones con la base de datos
    # def run_Query(self, query, parametros=()):
    #     ''' Función para ejecutar los Querys a la base de datos '''
    #     with sqlite3.connect(self.db_name) as conn:
    #         cursor = conn.cursor()
    #         result = cursor.execute(query, parametros)
    #         conn.commit()
    #     return result

    '''....Validaciones del sistema....'''

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
            finally:
                if len(self.fecha.get()) == 2 or len(self.fecha.get()) == 5:
                    self.backslash(len(self.fecha.get()))

                elif len(self.fecha.get()) > 10:
                    mssg.showerror(
                        'Atención!!', '.. Un año no tiene más de 4 dígitos..')
                    self.fecha.delete(10, 'end')

                # contemplar backspace
    # Rutina de limpieza de datos

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
    # Habilita campos
    # self....config(state='normal')
    # Deshabilita campos
    # self....config(state='disabled')

        
    # Rutina para cargar los datos en el árbol
    """ En esta funcion deben ser condiciones las validaciones """
    def tree_seleccion(self,event=None):
        item_seleccionado = self.treeProductos.focus()
        fila = self.treeProductos.item(item_seleccionado)
        val = fila.get('values')
        # pv.Razon_Social,pv.Ciudad
        valProv = self.run_Query(f"""SELECT * FROM Proveedor pv INNER JOIN Productos pd WHERE pd.idNit='{fila.get('text')}' AND pd.Codigo='{val[0]}';""")
        for row in valProv:
            self.limpiaCampos()
            self.idNit.insert(0, row[0])
            self.codigo.insert(0, row[1])
            self.descripcion.insert(0, row[2])
            self.unidad.insert(0, row[3])
            self.cantidad.insert(0, row[4])
            self.precio.insert(0, row[5])
            self.fecha.insert(0, row[6])
            self.razonSocial.insert(0, row[8])
            self.ciudad.insert(0, row[9])
    # Boton grabar
    def guardar_proveedor(self):
        # try except IntegrityError: UNIQUE constraint failed: Productos.idNit, Productos.Codigo
        # if event
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
        self.run_Query(f"""UPDATE Proveedor SET Razon_Social = ?, Ciudad = ? """, (self.razonSocial.get(), self.ciudad.get()))
        
    def graba_Registro(self):
        '''Adiciona un producto a la BD si la validación es True'''
        sameId = self.run_Query(f"""SELECT * from Productos pd WHERE pd.idNit= ?;""",(self.idNit.get()))
        
        if self.idNit.get()=='':
            print('id vacío')
            if self.codigo.get()!='':
                print('advertencia de que falta proveedor')
                mssg.showerror('Atención!!', f'.. el producto debe corresponder con un proveedor si desea grabar')
        else:
            #primero debe buscar si ya existe
            # si no existe
            self.guardar_proveedor()
            #si existe
            self.actualiza_proveedor()
            
            if self.codigo.get()!='':  
                #ahora comprueba si la fecha está vacía             
                if self.fecha.get() == '':
                    mssg.showerror( 'Atención!!', f'.. la fecha no puede estar vacío si desea grabar')
                else:
                    # también que compruebe si existe para ver si guarda o update
                    #si no existe
                    self.guardar_productos()
                    # si existe
                    self.actualiza_productos()
                
    # Boton cancelar
    def borrar_datos(self):
        # if event:
        self.limpiaCampos()

    """ Set('') """

    # Boton buscar
    # try except donde no hay coincidencias
    def lee_treeProductos(self):
        ''' Carga los datos y Limpia la Tabla tablaTreeView '''
        tabla_TreeView = self.treeProductos.get_children()

        for linea in tabla_TreeView:
            self.treeProductos.delete(linea)  # Límpia la filas del TreeView

        # Seleccionando los datos de la BD
        db_rows = self.run_Query("""SELECT * from Proveedor WHERE idNitProv= (?) ;""",(self.idNit.get(),)) 
        # db_rows contine la vista del query

        # # Insertando los datos de la BD en treeProductos de la pantalla
        for row in db_rows:
            print('holi')
            # self.treeProductos.insert('holi')#, row[3], row[4], row[5], row[6]]

    # Ni idea que hace
    def carga_Datos(self):
        self.idNit.insert(0, self.treeProductos.item(
            self.treeProductos.selection())['text'])
        self.idNit.configure(state='readonly')
        self.razonSocial.insert(0, self.treeProductos.item(
            self.treeProductos.selection())['values'][0])
        self.unidad.insert(0, self.treeProductos.item(
            self.treeProductos.selection())['values'][3])

    #     ''' Al final del for row queda con la última tupla
    #     y se usan para cargar las variables de captura
    # '''
    #     self.idNit.insert(0, row[0])
    #     self.razonSocial.insert(0, row[1])
    #     self.ciudad.insert(0, row[2])
    #     self.codigo.insert(0, row[4])
    #     self.descripcion.insert(0, row[5])
    #     self.unidad.insert(0, row[6])
    #     self.cantidad.insert(0, row[7])
    #     self.precio.insert(0, row[8])
    #     self.fecha.insert(0, row[9])

    def adiciona_Registro(self, event=None):
        '''Adiciona un producto a la BD si la validación es True'''
        pass

    def editaTreeProveedores(self, event=None):
        ''' Edita una tupla del TreeView'''
        pass

    def eliminaRegistro(self, event=None):
        '''Elimina un Registro en la BD'''
        pass
