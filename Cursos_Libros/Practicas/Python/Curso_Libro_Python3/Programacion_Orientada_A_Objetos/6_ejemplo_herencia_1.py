class FichaEmpleado:
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.antigüedad = None
        self.__cualificacion = None
    
    def __sueldo(self):
        return 1000 + self.antigüedad * 25 + self.__cualificacion * 100
    
    def setCualificacion(self, cualificacion:int):
        if cualificacion == 1 or cualificacion == 2 or cualificacion == 3 or cualificacion == 4 or cualificacion == 5:
            self.__cualificacion = cualificacion
    
    def getCualificacion(self):
        return self.__cualificacion
    
    def getSueldo(self):
        return self.__sueldo()
    
class FichaFabricacion(FichaEmpleado):
    def __init__(self, art_mes:float):
        super().__init__()
        self.__art_mes = art_mes
        
    def incArticulos(self, suma:float):
        self.__art_mes += suma

    def getArticulos(self):
        return self.__art_mes
    
def main():
    b = FichaFabricacion(eval(input("\nDigita la media mensual de artículos manufacturados: ")))
    
    b.nombre = input("\nDigita tu nombre: ")
    b.edad = eval(input("Digita tu edad: "))
    b.antigüedad = eval(input(f"\n{b.nombre} cuantos años llevas en la empresa?: "))
    b.setCualificacion(eval(input(f"{b.nombre} cuál es tu cualificación dentro de la empresa?: ")))
    
    print(f"{b.nombre} tu sueldo es de: {b.getSueldo()}")
    
    b.incArticulos(eval(input("\nDigita la nueva media mensual de artículos manufacturados: ")))
    print(f"{b.nombre} tu media mensual de artículos manufacturados es de: {b.getArticulos()}\n")
    
if __name__ == "__main__":
    main()
