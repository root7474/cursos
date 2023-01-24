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

def aumentaAntiguedad(objeto, antiguedad):
    objeto.antiguedad += 1
    antiguedad += 1

def main():
    a = FichaEmpleado()
    a.nombre = "David"
    a.edad = 26
    a.setCualificacion(3)
    antiguedad = eval(input(f"Introduce la antiguedad de {a.nombre}: "))
    a.antiguedad = antiguedad

    print(f"Antes del aumento de antiguedad, el campo antiguedad para {a.nombre} es: {a.antiguedad} y la variable antiguedad es: {antiguedad}")

    aumentaAntiguedad(a, antiguedad)

    print(f"Despues del aumento de antiguedad, el campo antiguedad para {a.nombre} es: {a.antiguedad} y la variable antiguedad es: {antiguedad}")

main()
