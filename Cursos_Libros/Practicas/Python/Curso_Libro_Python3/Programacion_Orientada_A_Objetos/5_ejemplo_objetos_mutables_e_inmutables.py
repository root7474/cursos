class FichaEmpleado:
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.antigüedad = None
        self.__cualificacion = None
        
    def __sueldo(self):
        return 1000000 + self.antigüedad * 25 + self.__cualificacion * 100
    
    def setCualificacion(self, cualificacion:int):
        if cualificacion == 1 or cualificacion == 2 or cualificacion == 3 or cualificacion == 4 or cualificacion == 5:
            self.__cualificacion = cualificacion
    
    def getCualificacion(self):
        return self.__cualificacion
    
    def getSueldo(self):
        return self.__sueldo()
    
def aumentaAntigüedad(objeto, antigüedad):
    objeto.antigüedad += 1
    antigüedad += 1

def main():
    ficha = FichaEmpleado()
    
    ficha.nombre = input("\nBienvenido... \n\nDigita tu nombre: ")
    ficha.edad = eval(input("Ahora digita tu edad: "))
    antigüedad = eval(input(f"\n{ficha.nombre}, cuanto tiempo llevas en la empresa?: "))
    ficha.antigüedad = antigüedad
    
    cualificacion = eval(input("Cuál es tu cualificación?: "))
    ficha.setCualificacion(cualificacion)
    
    print(f"\nAntes del campo antigüedad, el campo antigüedad para {ficha.nombre} es: {ficha.antigüedad} y la variable antiüedad es: {antigüedad}")
    aumentaAntigüedad(ficha, antigüedad)
    
    print(f"Después del campo antigüedad, el campo antigüedad para {ficha.nombre} es: {ficha.antigüedad} y la variable antiüedad es: {antigüedad}\n")

main()
