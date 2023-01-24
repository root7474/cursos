import tkinter

class Interfaz:
    def __init__(self, ventana):
        self.num_1 = None
        self.num_2 = None
        self.operacion = None
        
        self.ventana = ventana
        self.ventana.title("Calc 1.0")
        self.icono = tkinter.PhotoImage(file="/home/root7474/Documents/Cursos/OpenBootcamp/Python_Backend/Curso_De_Python/Practicas/Calc1.0/images/Calculator.png")
        self.ventana.iconphoto(False, self.icono)
        self.ventana.resizable(0, 0)
        self.ventana.geometry("411x363")
        
        self.pantalla = tkinter.Entry(self.ventana, width=31, bg="black", fg="White", 
                                      borderwidth=0, font=("arial", 18, "bold"))
        
        self.pantalla.grid(row=0, padx=1, pady=2, columnspan=4)
        
        self.boton_1 = tkinter.Button(self.ventana, text='1', width=9, height=3, 
                                      bg="white", fg="red", borderwidth=0, 
                                      cursor="hand2", command=lambda: self.envia_boton(1)).grid(row=1, column=0, padx=1.5, pady=1)
        
        self.boton_2 = tkinter.Button(self.ventana, text='2', width=9, height=3,
                                      bg="white", fg="red", borderwidth=0, 
                                      cursor="hand2", command=lambda: self.envia_boton(2)).grid(row=1, column=1, padx=1.5, pady=1)
        
        self.boton_3 = tkinter.Button(self.ventana, text='3', width=9, height=3,
                                      bg="white", fg="red", borderwidth=0, 
                                      cursor="hand2", command=lambda: self.envia_boton(3)).grid(row=1, column=2, padx=1.5, pady=1)
        
        self.boton_4 = tkinter.Button(self.ventana, text='4', width=9, height=3,
                                      bg="white", fg="red", borderwidth=0, 
                                      cursor="hand2", command=lambda: self.envia_boton(4)).grid(row=2, column=0, padx=1.5, pady=1)
        
        self.boton_5 = tkinter.Button(self.ventana, text='5', width=9, height=3,
                                      bg="white", fg="red", borderwidth=0, 
                                      cursor="hand2", command=lambda: self.envia_boton(5)).grid(row=2, column=1, padx=1.5, pady=1)
        
        self.boton_6 = tkinter.Button(self.ventana, text='6', width=9, height=3,
                                      bg="white", fg="red", borderwidth=0, 
                                      cursor="hand2", command=lambda: self.envia_boton(6)).grid(row=2, column=2, padx=1.5, pady=1)
        
        self.boton_7 = tkinter.Button(self.ventana, text='7', width=9, height=3,
                                      bg="white", fg="red", borderwidth=0, 
                                      cursor="hand2", command=lambda: self.envia_boton(7)).grid(row=3, column=0, padx=1.5, pady=1)
        
        self.boton_8 = tkinter.Button(self.ventana, text='8', width=9, height=3,
                                      bg="white", fg="red", borderwidth=0, 
                                      cursor="hand2", command=lambda: self.envia_boton(8)).grid(row=3, column=1, padx=1.5, pady=1)
        
        self.boton_9 = tkinter.Button(self.ventana, text='9', width=9, height=3,
                                      bg="white", fg="red", borderwidth=0, 
                                      cursor="hand2", command=lambda: self.envia_boton(9)).grid(row=3, column=2, padx=1.5, pady=1)
        
        self.boton_0 = tkinter.Button(self.ventana, text='0', width=9, height=3,
                                      bg="white", fg="red", borderwidth=0, 
                                      cursor="hand2", command=lambda: self.envia_boton(0)).grid(row=4, column=1, padx=1.5, pady=1)
        
        self.boton_igual = tkinter.Button(self.ventana, text='=', width=9, height=3,
                                      bg="red", fg="white", borderwidth=0, 
                                      cursor="hand2", command=self.igual).grid(row=4, column=0, padx=1.5, pady=1)
        
        self.boton_punto = tkinter.Button(self.ventana, text='.', width=9, height=3,
                                          bg="spring green", fg="black", borderwidth=0,
                                          cursor="hand2", command=lambda: self.envia_boton('.')).grid(row=4, column=2, padx=1, pady=1)
        
        self.boton_suma = tkinter.Button(self.ventana, text='+', width=9, height=3,
                                          bg="deep sky blue", fg="black", borderwidth=0,
                                          cursor="hand2", command=self.suma).grid(row=1, column=3, padx=1.5, pady=1)
        
        self.boton_menos = tkinter.Button(self.ventana, text='-', width=9, height=3,
                                          bg="deep sky blue", fg="black", borderwidth=0,
                                          cursor="hand2", command=self.resta).grid(row=2, column=3, padx=1.5, pady=1)
        
        self.boton_multiplicacion = tkinter.Button(self.ventana, text='X', width=9, height=3,
                                          bg="deep sky blue", fg="black", borderwidth=0,
                                          cursor="hand2", command=self.multiplicacion).grid(row=3, column=3, padx=1.5, pady=1)
        
        self.boton_division = tkinter.Button(self.ventana, text='/', width=9, height=3,
                                          bg="deep sky blue", fg="black", borderwidth=0,
                                          cursor="hand2", command=self.division).grid(row=4, column=3, padx=1.5, pady=1)

        self.boton_porcentaje = tkinter.Button(self.ventana, text='%', width=9, height=3,
                                               bg="deep sky blue", fg="black", borderwidth=0,
                                               cursor="hand2", command=self.procentaje).grid(row=5, column=3, padx=1, pady=1)
        
        self.boton_despejar = tkinter.Button(self.ventana, text='C', width=35, height=3,
                                             bg="deep sky blue", fg="black", borderwidth=0,
                                             cursor="hand2", command=self.despejar).grid(row=5, column=0, columnspan=3, padx=3, pady=1)

    def envia_boton(self, valor):
        anterior = self.pantalla.get()
        self.pantalla.delete(0, tkinter.END)
        self.pantalla.insert(0, str(anterior) + str(valor))
        
    def suma(self):
        self.num_1 = self.pantalla.get()
        self.num_1 = float(self.num_1)
        
        self.pantalla.delete(0, tkinter.END)
        self.operacion = '+'
        
    def resta(self):
        self.num_1 = self.pantalla.get()
        self.num_1 = float(self.num_1)
        
        self.pantalla.delete(0, tkinter.END)
        self.operacion = '-'
        
    def multiplicacion(self):
        self.num_1 = self.pantalla.get()
        self.num_1 = float(self.num_1)
        
        self.pantalla.delete(0, tkinter.END)
        self.operacion = 'X'
        
    def division(self):
        self.num_1 = self.pantalla.get()
        self.num_1 = float(self.num_1)
        
        self.pantalla.delete(0, tkinter.END)
        self.operacion = '/'
        
    def procentaje(self):
        self.num_1 = self.pantalla.get()
        self.num_1 = float(self.num_1)
        
        self.pantalla.delete(0, tkinter.END)
        self.pantalla.insert(0, round(self.num_1 / 100, 4))
        
    def igual(self):
        self.num_2 = self.pantalla.get()
        self.pantalla.delete(0, tkinter.END)
        
        if self.operacion == '+':
            self.pantalla.insert(0, round(self.num_1 + float(self.num_2), 4))
        if self.operacion == '-':
            self.pantalla.insert(0, round(self.num_1 - float(self.num_2), 4))
        if self.operacion == 'X':
            self.pantalla.insert(0, round(self.num_1 * float(self.num_2), 4))
        if self.operacion == '/':
            try:
                self.pantalla.insert(0, round(self.num_1 / float(self.num_2), 4))
            except ZeroDivisionError:
                self.pantalla.insert(0, "Error!!!... División por cero ;(")
            
    def despejar(self):
        self.pantalla.delete(0, tkinter.END)
