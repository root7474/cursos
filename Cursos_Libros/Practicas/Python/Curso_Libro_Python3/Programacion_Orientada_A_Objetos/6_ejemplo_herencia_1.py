class FichaEmpleado:
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.antigüedad = None
        self.__cualificacion = None
        
    def __sueldo(self):
        return(1000 + self.antigüedad * 25 + self.__cualificacion * 100)
    
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
        self.__articulos_mes = art_mes
        
    def incArticulos(self, suma:float):
        self.__articulos_mes += suma
    
    def getArticulos(self):
        return self.__articulos_mes

def main():
    fabricacion = FichaFabricacion(eval(input("Digita la media de artículos manufacturados al mes: ")))
    fabricacion.nombre = input("Digita el nombre del empleado: ")
    fabricacion.edad = eval(input("Digita su edad: "))
    fabricacion.antigüedad = eval(input(f"Digita la antigüedad de {fabricacion.nombre} en la empresa: "))
    
    fabricacion.setCualificacion(eval(input(f"Digita su cualificación: ")))
    print(f"El sueldo de {fabricacion.nombre} es de: {fabricacion.getSueldo()}")
    
    fabricacion.incArticulos(eval(input("Incrementa la media de artículos manufacturados al mes: ")))
    print(f"La media de artículos manufacturados por {fabricacion.nombre} es de: {fabricacion.getArticulos()}")

if __name__ == "__main__":
    main()
