class FichaEmpleado:
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.antiguedad = None
        self.__cualificacion = None

    def __sueldo(self):
        return(1000 + self.antiguedad * 25 + self.__cualificacion * 100)

    def setCualificacion(self, cualif:int):
        if cualif == 1 or cualif == 2 or cualif == 3 or cualif == 4 or cualif == 5:
            self.__cualificacion = cualif

    def getCualificacion(self):
        return(self.__cualificacion)

    def getSueldo(self):
        return(self.__sueldo())

class FichaFabricacion(FichaEmpleado):
    def __init__(self, art_mes:float):
        super().__init__()
        self.__articulos_mes = art_mes
    
    def incArticulos(self, suma:float):
        self.__articulos_mes += suma
        
    def getArticulos(self):
        return(self.__articulos_mes)
    
def main():
    b = FichaFabricacion(27.5)
    b.nombre = "David"
    b.edad = 27
    b.antiguedad = 4
    b.setCualificacion(4)
    print(f"El sueldo de {b.nombre} es: {b.getSueldo()}")
    
    b.incArticulos(34.5)
    print(f"La media mensual de artículos manufacturados por {b.nombre} es {b.getArticulos()}")
    
if __name__ == '__main__':
    main()
