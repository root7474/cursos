class FichaEmpleado:
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.antigüedad = None
        self.__cualificacion = None
        
    def sueldo(self):
        return 1000000 + self.antigüedad * 25 + self.__cualificacion * 100
    
    def setCualificacion(self, cualif:int):
        if cualif == 1 or cualif == 2 or cualif == 3 or cualif == 4 or cualif == 5:
            self.__cualificacion = cualif
    
    def getCualificacion(self):
        return self.__cualificacion

def main():
    ficha = FichaEmpleado()
    
    ficha.nombre = input("\nBienvenido... \n\nDigita tu nombre: ")
    ficha.edad = eval(input("Ahora digita tu edad: "))
    ficha.antigüedad = eval(input(f"\n{ficha.nombre} cuanto tiempo llevas en la empresa?: "))
    
    cualificacion = eval(input("Cuál es tu cualificació: "))
    ficha.setCualificacion(cualificacion)
    
    print(f"\n{ficha.nombre} tu sueldo con antigüedad de {ficha.antigüedad} con cualificación de {ficha.getCualificacion()} es de: ${ficha.sueldo()}\n")

main()
