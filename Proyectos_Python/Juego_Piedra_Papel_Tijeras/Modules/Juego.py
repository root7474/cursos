import random
import Modules.Inicio as Inicio
import tkinter as tk
from tkinter import (ttk, messagebox)

class RootSec(tk.Toplevel):
    en_uso = False
    opciones = None
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.puntos_usuario = 0
        self.puntos_IA = 0
        self.geometry("315x155")
        self.resizable(0, 0)
        self.title("Juego Piedra Papel o Tijeras")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.frm = ttk.Frame(self)
        self.frm.grid(sticky='nesw')
        
        self.label_intentos = ttk.Label(self.frm, text="")
        self.label_intentos.grid(column=0, row=0, columnspan=4, pady=5)
            
        self.label_nombre = ttk.Label(self.frm, text="")
        self.label_nombre.grid(column=0, row=1, pady=5)
        self.label_nombre_turno = ttk.Label(self.frm, text="")
        self.label_nombre_turno.grid(column=1, row=1, pady=5)
        self.label_puntos_nombre = ttk.Label(self.frm, text="Puntos: 0")
        self.label_puntos_nombre.grid(column=2, row=1, pady=5)
        
        self.label_IA = ttk.Label(self.frm, text="IA:")
        self.label_IA.grid(column=0, row=2, pady=5)
        self.label_IA_turno = ttk.Label(self.frm, text="")
        self.label_IA_turno.grid(column=1, row=2, pady=5)
        self.label_puntos_IA = ttk.Label(self.frm, text="Puntos: 0")
        self.label_puntos_IA.grid(column=2, row=2, pady=5)
        
        self.boton_piedra = ttk.Button(self.frm, width=11, text="Piedra", command=lambda: self.boton("piedra"))
        self.boton_piedra.grid(column=0, row=3, padx=3, pady=2)
        self.boton_papel = ttk.Button(self.frm, width=11, text="Papel", command=lambda: self.boton("papel"))
        self.boton_papel.grid(column=1, row=3, padx=3, pady=2)
        self.boton_tijeras = ttk.Button(self.frm, width=11, text="Tijeras", command=lambda: self.boton("tijeras"))
        self.boton_tijeras.grid(column=2, row=3, padx=3, pady=2)
        self.boton_atras = ttk.Button(self.frm, width=11, text="Atrás", command=self.destroy)
        self.boton_atras.grid(column=0, row=4, padx=3, pady=2)
        self.boton_cerrar = ttk.Button(self.frm, width=24, text="Cerrar juego", command=self.quit)
        self.boton_cerrar.grid(column=1, row=4, columnspan=2, pady=2)
        
        self.focus()
        self.__class__.en_uso = True
        
    def nombre_ingresado(self, nombre):
        self.nombre = nombre
        self.label_nombre.config(text=f"{self.nombre}:")
    
    def my_dialog(self, intentos):
        self.intentos = intentos
        self.label_intentos.config(text=f"Intento número: {self.intentos}")
        
    def boton(self, opcion):
        self.opciones = opcion
        self.piedra_papel_tijeras(self.opciones)

    def piedra_papel_tijeras(self, opciones_usuario):
        opciones_IA = ["piedra", "papel", "tijeras"]
        opciones_IA = random.choice(opciones_IA)
        
        self.intentos -= 1
        self.label_intentos.config(text=f"Número intentos: {self.intentos}")
        self.puntos_mayor = self.puntos_usuario > self.puntos_IA
        self.puntos_menor = self.puntos_usuario < self.puntos_IA
    
        if opciones_usuario == "piedra" and opciones_IA == "tijeras":
            self.puntos_usuario += 1
            messagebox.showinfo(message=f"La IA ha elegido {opciones_IA}")
            messagebox.showinfo(message=f"Has elegido {opciones_usuario}. \nTienes +1 punto")
            self.label_nombre_turno.config(text=opciones_usuario)
            self.label_IA_turno.config(text=opciones_IA)
            self.label_puntos_nombre.config(text=f"puntos: {self.puntos_usuario}")
        
        elif opciones_usuario == "papel" and opciones_IA == "piedra":
            self.puntos_usuario += 1
            messagebox.showinfo(message=f"La IA ha elegido {opciones_IA}")
            messagebox.showinfo(message=f"Has elegido {opciones_usuario}. \nTienes +1 punto")
            self.label_nombre_turno.config(text=opciones_usuario)
            self.label_IA_turno.config(text=opciones_IA)
            self.label_puntos_nombre.config(text=f"puntos: {self.puntos_usuario}")
        
        elif opciones_usuario == "tijeras" and opciones_IA == "papel":
            self.puntos_usuario += 1
            messagebox.showinfo(message=f"La IA ha elegido {opciones_IA}")
            messagebox.showinfo(message=f"Has elegido {opciones_usuario}. \nTienes +1 punto")
            self.label_nombre_turno.config(text=opciones_usuario)
            self.label_IA_turno.config(text=opciones_IA)
            self.label_puntos_nombre.config(text=f"puntos: {self.puntos_usuario}")
        
        elif opciones_usuario == opciones_IA:
            messagebox.showinfo(message=f"La IA ha elegido {opciones_IA}")
            messagebox.showinfo(message=f"Has elegido {opciones_usuario}. \nEs un empate")
            self.label_nombre_turno.config(text=opciones_usuario)
            self.label_IA_turno.config(text=opciones_IA)
        
        else:
            self.puntos_IA += 1
            messagebox.showinfo(message=f"Has elegido {opciones_usuario}")
            messagebox.showinfo(message=f"La IA ha elegido {opciones_IA} \nLa IA tiene +1 punto")
            self.label_nombre_turno.config(text=opciones_usuario)
            self.label_IA_turno.config(text=opciones_IA)
            self.label_puntos_IA.config(text=f"puntos: {self.puntos_IA}")
        
        if self.intentos == 0:
            messagebox.showinfo(message="Ya no tienes más intentos" + f"\n{self.nombre}: {self.puntos_usuario} vs IA: {self.puntos_IA}")
            
            if self.puntos_usuario > self.puntos_IA:
                messagebox.showinfo(message=f"{self.nombre} has ganado", options=self.destroy())
            elif self.puntos_usuario < self.puntos_IA:
                messagebox.showinfo(message="Ha ganado la IA", options=self.destroy())
            else:
                messagebox.showinfo(message="Ha habido un empate", options=self.destroy())
        
    def destroy(self):
        self.__class__.en_uso = False
        self.root_principal = Inicio.RootPrincipal()
        return super().destroy()
    