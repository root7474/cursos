import tkinter
from tkinter import ttk
import random
from tkinter import filedialog
from tkinter import colorchooser

window = tkinter.Tk()
    
def mi_funcion():
    print("Clicado")
    
def saludar(event):
    print("Han hecho click en saludar")

def saludar_double_click(event):
    print("Han hecho doble click en saludar")
    
def salir(event):
    print("Adios")
    window.quit()

def main():
    # Posicionamiento mediante pack()
    """ label_1 = tkinter.Label(window, text="Label 1", bg="yellow", fg="blue")
    label_1.pack(ipadx=45, ipady=15, fill='x')
    
    label_2 = tkinter.Label(window, text="Label 2", bg="red", fg="white")
    label_2.pack(ipadx=45, ipady=15, fill='x')
    
    label_3 = tkinter.Label(window, text="Label 3", bg="purple", fg="white")
    label_3.pack(ipadx=45, ipady=15, fill='x')
    
    label_4 = tkinter.Label(window, text="Label 4", bg="blue", fg="white")
    label_4.pack(ipadx=15, ipady=15, side="left")
    
    label_5 = tkinter.Label(window, text="Label 5", bg="yellow", fg="black")
    label_5.pack(ipadx=15, ipady=15, side="left")
    
    label_6 = tkinter.Label(window, text="Label 6", bg="green", fg="white")
    label_6.pack(ipadx=15, ipady=15, side="right") """
    
    # Posicionamiento mediante grid()
    """ window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)
    
    # Etiqueta usurio
    username_label = ttk.Label(window, text="Username:")
    username_label.grid(row=0, column=0, sticky=tkinter.W, padx=5, pady=5)
    
    # Campo usuario
    username_entry = ttk.Entry(window)
    username_entry.grid(row=0, column=1, sticky=tkinter.E, padx=5, pady=5)
    
    # Etiqueta password
    password_label = ttk.Label(window, text="Password:")
    password_label.grid(row=1, column=0, sticky=tkinter.W, padx=5, pady=5)
    
    # Campo password
    password_entry = ttk.Entry(window, show='*')
    password_entry.grid(row=1, column=1, sticky=tkinter.E, padx=5, pady=5)
    
    # Boton
    login_button = ttk.Button(window, text="Login")
    login_button.grid(row=3, column=1, sticky=tkinter.E, padx=5, pady=5) """
    
    # Posicionamiento mediante place()
    """ label_1 = tkinter.Label(window, text="Posicionamiento absoluto", bg="blue", fg="white")
    label_1.place(x=10, y=50)
    
    label_2 = tkinter.Label(window, text="Otro mas", bg="red", fg="yellow")
    label_2.place(x=25, y=30) """
    
    """ colors = ["blue", "red", "yellow", "purple", "green", "black"]
    
    for i in range(0,10):
        color_1 = random.randint(0, len(colors)-1)
        color_2 = random.randint(0, len(colors)-1)
        
        label = tkinter.Label(window, text="Etiqueta!", bg=colors[color_1], fg=colors[color_2])
        label.place(x=random.randint(0, 100), y=random.randint(0, 100)) """
        
    # Widgets
    """ window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)
    
    frame = ttk.Frame(window, width=800, height=600, relief="sunken")
    label = ttk.Label(frame, text="Hola")
    
    label.grid(row=0, column=0, sticky=tkinter.W, padx=5, pady=5)
    frame.grid(row=0, column=0, sticky=tkinter.W) """
    
    # ListBox
    """ window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)
    
    lista = ["Windows", "MacOS", "Linux", "MS-DOS", "AmigaOS", "BeOS", "OS/2"]
    lista_items = tkinter.StringVar(value=lista)
    list_box = tkinter.Listbox(window, height=len(lista), listvariable=lista_items)
    list_box.grid(row=0, column=0, sticky=tkinter.W) """
    
    # RadioButton
    """ window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)
    
    seleccionado = tkinter.StringVar()
    
    r1 = ttk.Radiobutton(window, text="Sí", value='1', variable=seleccionado)
    r2 = ttk.Radiobutton(window, text="No", value='2', variable=seleccionado)
    r3 = ttk.Radiobutton(window, text="Quizá", value='3', variable=seleccionado)
    
    r1.grid(row=1, column=0, padx=5, pady=5)
    r2.grid(row=2, column=0, padx=5, pady=5)
    r3.grid(row=3, column=0, padx=5, pady=5)
    
    seleccionado_2 = tkinter.StringVar()
    
    rs1 = ttk.Radiobutton(window, text="Sí 2", value='12', variable=seleccionado_2)
    rs1.grid(row=0, column=1, padx=5, pady=5) """
    
    # CheckBox
    """ window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)
    
    seleccionado = tkinter.StringVar()
    checkbox = ttk.Checkbutton(window, text="Acepto las condiciones", 
                               variable=seleccionado, command=mi_funcion)
    checkbox.grid(row=0, column=0) """
    
    # Programación Orientada a Eventos
    """ boton = tkinter.Button(window, text="Haz click")
    
    boton.pack()
    boton.bind("<Button-1>", saludar)
    boton.bind("<Double-1>", saludar_double_click)
    
    boton_salir = tkinter.Button(window, text="Salir")
    
    boton_salir.pack()
    boton_salir.bind("<Button-1>", salir) """
    
    # Ejemplos
    # filename = filedialog.askopenfilename()
    colorchooser.askcolor(initialcolor="#ff0000")
    
    window.mainloop()

if __name__ == "__main__":
    main()
