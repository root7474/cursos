import tkinter as tk
from tkinter import _Cursor, _Relief, _ScreenUnits, _TakeFocusValue, Menu, Misc, ttk
from typing import Any
from typing_extensions import Literal
import Modules.Inicio as Inicio

class Intentos(tk.Toplevel):
    def __init__(self, *args, callback = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.callback = callback
        self.geometry("380x123")
        self.resizable(0, 0)
        self.title("Ventana principal")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.frm = ttk.Frame(self)
        self.frm.grid(sticky='nesw')
        self.label_intentos = ttk.Label(self.frm, text="")
        self.label_intentos.grid(column=0, row=0, pady=5)
        self.caja_intentos = ttk.Entry(self.frm, width=25)
        self.caja_intentos.grid(column=2, row=1, sticky='w', padx=10, pady=3)
        self.boton_intentos = ttk.Button(self.frm, width=24, text="Comenzar juego", command=self.abrir_root_sec)
        self.boton_intentos.grid(column=2, row=2, sticky='', padx=10, pady=3)
        
