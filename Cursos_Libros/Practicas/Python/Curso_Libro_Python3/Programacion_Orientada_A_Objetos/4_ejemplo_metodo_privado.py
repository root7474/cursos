class FichaEmpleado:
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.antiüedad = None
        self.__cualificacion = None
        
    def __sueldo(self):
        return 1000000 + self.antiüedad * 25 + self.__cualificacion * 100
    
    def setCualificacion(self, cualificacion:int):
        if cualificacion == 1 or cualificacion == 2 or cualificacion == 3 or cualificacion == 4 or cualificacion == 5:
            self.__cualificacion = cualificacion
    
    def getCualificacion(self):
        return self.__cualificacion
    
    def getSueldo(self):
        return self.__sueldo()

def main():
    ficha = FichaEmpleado()
    
    ficha.nombre = input("\nBienvenido... \n\nDigita tu nombre: ")
    ficha.edad = eval(input("Ahora digita tu edad: "))
    ficha.antiüedad = eval(input(f"\n{ficha.nombre}, cuanto tiempo llevas en la empresa?: "))
    
    cualificacion = eval(input("Cuál es tu cualificación?: "))
    ficha.setCualificacion(cualificacion)
    
    print(f"{ficha.nombre} tu sueldo con antigüedad de {ficha.antiüedad} años, con cualificación de grado {ficha.getCualificacion()} es de: ${ficha.getSueldo()}\n")

main()
