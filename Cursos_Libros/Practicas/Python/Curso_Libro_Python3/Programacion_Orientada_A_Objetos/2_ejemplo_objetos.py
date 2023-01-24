class FichaEmpleado:
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.antigÜedad = None
        self.cualificacion = None
        
    def sueldo(self):
        return 1000000 + self.antigÜedad * 25 + self.cualificacion * 100
    
def main():
    ficha = FichaEmpleado()
    ficha.nombre = input("\nBienvenido... \n\nDigita tu nombre: ")
    ficha.edad = eval(input("Ahora digita tu edad: "))
    ficha.antigÜedad = eval(input(f"\n{ficha.nombre}, cuantos años llevas en la empresa?: "))
    ficha.cualificacion = eval(input("Cuál es tu cualificación?: "))

    print(f"\n{ficha.nombre} tu sueldo con antigüedad {ficha.antigÜedad} años en la empresa y con cualificación de grado {ficha.cualificacion} es de : ${ficha.sueldo()}\n")

main()
