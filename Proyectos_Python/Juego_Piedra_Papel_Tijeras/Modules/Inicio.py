import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import Modules.Juego as Juego

class RootPrincipal(tk.Tk):
    def __init__(self, *args, callback = None, intentos_callback = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.callback = callback
        self.intentos_callback = intentos_callback
        self.geometry("380x123")
        self.resizable(0, 0)
        self.title("Ventana principal")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.frm = ttk.Frame(self)
        self.frm.grid(sticky='nesw')
        self.label_titulo = ttk.Label(self.frm, text="Bienvenido")
        self.label_titulo.grid(column=0, row=0, columnspan=3, pady=5)
        self.label_nombre = ttk.Label(self.frm, text="Digita tu nombre:", width=15)
        self.label_nombre.grid(column=0, row=1, sticky='e', padx=15, pady=3)
        self.caja_nombre = ttk.Entry(self.frm, width=25)
        self.caja_nombre.grid(column=1, row=1, sticky='w', padx=10, pady=3)
        self.label_intentos = ttk.Label(self.frm, text="Número intentos:", width=15)
        self.label_intentos.grid(column=0, row=2, pady=5)
        self.caja_intentos = ttk.Entry(self.frm, width=25)
        self.caja_intentos.grid(column=1, row=2, sticky='w', padx=10, pady=3)
        self.boton_abrir = ttk.Button(self.frm, width=24, text="Comenzar juego", command=self.abrir_root_sec)
        self.boton_abrir.grid(column=1, row=3, sticky='', padx=10, pady=3)
        self.boton_cerrar = ttk.Button(self.frm, width=14, text="Cerrar juego", command=self.destroy)
        self.boton_cerrar.grid(column=0, row=3, sticky='e', padx=15, pady=3)
        # self.mainloop()
        
    def destroy(self) -> None:
        return super().quit()
        
    def abrir_root_sec(self):
        if not Juego.RootSec.en_uso:
            self.callback = self.caja_nombre.get()
            self.intentos_callback = self.caja_intentos.get()
            self.root_sec = Juego.RootSec()
            self.root_sec.nombre_ingresado(self.callback)
            self.root_sec.numero_intentos(self.intentos_callback)
            return super().state(newstate="withdraw")
        else:
            return super().state(newstate="normal")
        