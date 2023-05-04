import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import Modules.Inicio as Inicio

class RootSec(tk.Toplevel):
    en_uso = False
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("325x155")
        self.resizable(0, 0)
        self.title("Ventana Secundaria")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.frm = ttk.Frame(self)
        self.frm.grid(sticky='nesw')
        self.label_intentos = ttk.Label(self.frm, text="Intento número: 0")
        self.label_intentos.grid(column=0, row=0, columnspan=4, pady=5)
        self.label_nombre = ttk.Label(self.frm, text="")
        self.label_nombre.grid(column=0, row=1, pady=5)
        self.label_nombre_turno = ttk.Label(self.frm, text="")
        self.label_nombre_turno.grid(column=1, row=1, pady=5)
        self.label_puntos_nombre = ttk.Label(self.frm, text="Puntos: 0")
        self.label_puntos_nombre.grid(column=2, row=1, pady=5)
        # self.label_contador_nombre = ttk.Label(self.frm, text="0")
        # self.label_contador_nombre.grid(column=3, row=1, pady=5)
        self.label_IA = ttk.Label(self.frm, text="IA:")
        self.label_IA.grid(column=0, row=2, pady=5)
        self.label_IA_turno = ttk.Label(self.frm, text="piedra")
        self.label_IA_turno.grid(column=1, row=2, pady=5)
        self.label_puntos_IA = ttk.Label(self.frm, text="Puntos: 0")
        self.label_puntos_IA.grid(column=2, row=2, pady=5)
        # self.label_contador_IA = ttk.Label(self.frm, text="0")
        # self.label_contador_IA.grid(column=3, row=2, pady=5)
        self.boton_piedra = ttk.Button(self.frm, width=11, text="Piedra", command=self.botonPiedra)
        self.boton_piedra.grid(column=0, row=3, padx=3, pady=2)
        self.boton_papel = ttk.Button(self.frm, width=11, text="Papel", command=self.botonPapel)
        self.boton_papel.grid(column=1, row=3, padx=3, pady=2)
        self.boton_tijeras = ttk.Button(self.frm, width=11, text="Tijeras", command=self.botonTijeras)
        self.boton_tijeras.grid(column=2, row=3, padx=3, pady=2)
        self.boton_cerrar = ttk.Button(self.frm, width=38, text="Cerrar juego", command=self.quit)
        self.boton_cerrar.grid(column=0, row=4, columnspan=3, padx=5, pady=2)
        self.focus()
        self.__class__.en_uso = True
        
    def nombre_ingresado(self, nombre):
        self.label_nombre.config(text=f"{nombre}:")
        
    def numero_intentos(self, intentos):
        self.label_intentos.config(text=f"Intento número: {intentos}")
        
    def botonPiedra(self):
        self.label_nombre_turno.config(text="piedra")
        
    def botonPapel(self):
        self.label_nombre_turno.config(text="papel")
        
    def botonTijeras(self):
        self.label_nombre_turno.config(text="tijeras")
    
    def destroy(self):
        self.__class__.en_uso = False
        self.root_principal = Inicio.RootPrincipal()
        return super().destroy()
    
    """ def piedra_papel_tijeras(self):
        self.bandera = False
        
        while self.bandera == False: """
            
    