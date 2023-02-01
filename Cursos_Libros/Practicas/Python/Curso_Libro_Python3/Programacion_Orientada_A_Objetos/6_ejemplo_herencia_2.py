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
    
class FichaTecnico(FichaEmpleado):
    def __init__(self):
        super().__init__()
        self.__estrellas = '*'
        
    def incEstrellas(self):
        self.__estrellas += '*'
        
    def disEstrellas(self):
        if self.__estrellas == "**":
            self.__estrellas = '*'
        if self.__estrellas == "***":
            self.__estrellas = "**"
        if self.__estrellas == "****":
            self.__estrellas = "***"
        if self.__estrellas == "*****":
            self.__estrellas = "****"
            
    def getEstrellas(self):
        return self.__estrellas
    
class FichaComercial(FichaEmpleado):
    def __init__(self, cliente:str):
        super().__init__()
        self.__cliente_principal = cliente
        self.__num_clientes = None
        
    def setClientes(self, cli:str):
        self.__cliente_principal = cli
    
    def setNumClientes(self, num:int):
        self.__num_clientes = num
        
    def getClientes(self):
        return self.__cliente_principal
    
    def getNumClientes(self):
        return self.__num_clientes
    
def main():
    tecnico = FichaTecnico()
    tecnico.nombre = input("\nDigita el nombre del empleado: ")
    tecnico.edad = eval(input("Digita su edad: "))
    tecnico.antigüedad = eval(input(f"Digita la antigüedad de {tecnico.nombre} en la empresa: "))
    
    tecnico.setCualificacion(eval(input(f"Digita su cualificación: ")))
    print(f"\nEl sueldo de {tecnico.nombre} es de: {tecnico.getSueldo()}"
          f"\nEl número inicial de estrellas de {tecnico.nombre} es: {tecnico.getEstrellas()}\n")
    
    cant_estrellas_inc = eval(input("Cuántas estrellas deseas incrementar?: "))
    
    for i in range(cant_estrellas_inc):
        i += 1
        tecnico.incEstrellas()
    
    print(f"Después de {i} incrementos, el número actual de estrellas de {tecnico.nombre} es: {tecnico.getEstrellas()}")
    
    tecnico.disEstrellas()
    print(f"Tras un decremento el número actual de estrellas de {tecnico.nombre} es: {tecnico.getEstrellas()}\n")
    
    comercial = FichaComercial(input("Cliente principal: "))
    comercial.nombre = input("Digita el nombre del empleado: ")
    comercial.edad = eval(input("Digita su edad: "))
    comercial.antigüedad = eval(input(f"Digita la antigüedad de {comercial.nombre} en la empresa: "))
    
    comercial.setCualificacion(eval(input(f"Digita su cualificación: ")))
    print(f"\nEl sueldo de {comercial.nombre} es de: {comercial.getSueldo()}."
          f"\nEl cliente principal de {comercial.nombre} es: {comercial.getClientes()}.")
    
    print(f"\nEmpleado/a: {comercial.nombre}\n")
    
    comercial.setClientes(input("Cliente principal: "))
    print(f"El cliente principal es: {comercial.getClientes()}\n")
    
    comercial.setNumClientes(eval(input("Número de clientes: ")))
    print(f"El número de clientes es: {comercial.getNumClientes()}\n")
    
if __name__ == "__main__":
    main()
