class FichaEmpleado:
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.antiguedad = None
        self.cualificacion = None
        
    def sueldo(self):
        return(1000 + self.antiguedad * 25 + self.cualificacion * 100)

def main():
    a = FichaEmpleado()
    a.nombre = "David"
    a.edad = 26
    a.antiguedad = 2
    a.cualificacion = 1

    b = FichaEmpleado()
    b.nombre = "Felipe"
    b.edad = 21
    b.antiguedad = 9
    b.cualificacion = 4

    print(f"El sueldo de {a.nombre} con {a.antiguedad} años en la empresa y con cualificación de grado {a.cualificacion} es de {a.sueldo()} euros.")
    print(f"El sueldo de {b.nombre} con {b.antiguedad} años en la empresa y con cualificación de grado {b.cualificacion} es de {b.sueldo()} euros.")

main()
