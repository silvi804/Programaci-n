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


        # widget Principal del sistema
        self.mainwindow = self.win

        # Fución de manejo de eventos del sistema
    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = Inventario()
    app.run()
