class FichaEmpleado:
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.antiguedad = None
        self.__cualificacion = None
        
    def sueldo(self):
        return(1000 + self.antiguedad * 25 + self.__cualificacion * 100)
    
    def setCualificacion(self, cualif:int):
        if cualif == 1 or cualif == 2 or cualif == 3 or cualif == 4 or cualif == 5:
            self.__cualificacion = cualif
    
    def getCualificacion(self):
        return(self.__cualificacion)

def main():
    a = FichaEmpleado()
    a.nombre = "David"
    a.edad = 26
    a.antiguedad = 2
    
    a.setCualificacion(3)
    a.setCualificacion(-7)
    a.setCualificacion(1.2)

    print(f"El sueldo de {a.nombre} con {a.antiguedad} años en la empresa y con cualificación de grado {a.getCualificacion()} es de {a.sueldo()} euros.")

main()
