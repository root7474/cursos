class FichaEmpleado:
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.antigüedad = None
        self.__cualificacion = None
        
    def __sueldo(self):
        return 1000 + self.antigüedad * 25 + self.__cualificacion * 100
    
    def setCualificacion(self, cualificacion):
        if cualificacion == 1 or cualificacion == 2 or cualificacion == 3 or cualificacion == 4 or cualificacion == 5:
            self.__cualificacion = cualificacion
            
    def getCualificacion(self):
        return self.__cualificacion
    
    def getSueldo(self):
        return self.__sueldo()

class FichaTecnico(FichaEmpleado):
    def __init__(self):
        super().__init__()
        self.__estrellas = "*"
        
    def incEstrellas(self):
        self.__estrellas += "*"
    
    def disEstrellas(self):
        if self.__estrellas == "**":
            self.__estrellas = "*"
        if self.__estrellas == "***":
            self.__estrellas = "**"
        if self.__estrellas == "****":
            self.__estrellas = "***"
        if self.__estrellas == "*****":
            self.__estrellas = "****"
            
    def getEstrellas(self):
        return self.__estrellas
    
class FichaComercial(FichaEmpleado):
    def __init__(self):
        super().__init__()
        self.__cliente_principal = "TecnoWorld2000"
        self.__num_clientes = None
    
    def setCliente(self, cliente:str):
        self.__cliente_principal = cliente
        
    def getCliente(self):
        return self.__cliente_principal
    
    def setNumClientes(self, num_clientes:int):
        self.__num_clientes = num_clientes
        
    def getNumClientes(self):
        return self.__num_clientes
    
def main():
    c = FichaTecnico()
    d = FichaComercial()
    
    c.nombre = input("\nDigita tu nombre: ")
    c.edad = eval(input("Digita tu edad: "))
    c.antigüedad = eval(input(f"\n{c.nombre} cuál es tu antigüedad dentro de la empresa?: "))
    c.setCualificacion(eval(input(f"{c.nombre} cuál es tu cualificación dentro de la empresa?: ")))
    
    print(f"\n{c.nombre} tu sueldo es de: {c.getSueldo()}"
          f"\nTu número inicial de estrellas es de: {c.getEstrellas()}")
    
    c.incEstrellas()
    c.incEstrellas()
    print(f"{c.nombre} después de dos incrementos tu número inicial de estrellas es de: {c.getEstrellas()}")
    
    d.nombre = input("\nDigita tu nombre: ")
    d.edad = eval(input("Digita tu edad: "))
    d.antigüedad = eval(input(f"\n{d.nombre} cuál es tu antigüedad dentro de la empresa?: "))
    d.setCualificacion(eval(input(f"{d.nombre} cuál es tu cualificación dentro de la empresa?: ")))
    
    print(f"\n{d.nombre} tu sueldo es de: {d.getSueldo()}"
          f"\nTu cliente principal es: {d.getCliente()}")
    
    print(f"\nEmpleado/a: {d.nombre}")
    
    cliente_principal = input("\nIntroduce el cliente principal: ")
    d.setCliente(cliente_principal)
    print(f"{d.nombre} tu cliente principal actual es: {d.getCliente()}")
    
    numero_clientes = eval(input("\nIntroduce el número de clientes: "))
    d.setNumClientes(numero_clientes)
    print(f"{d.nombre} tu número de clientes es de: {d.getNumClientes()}\n")
    
if __name__ == "__main__":
    main()
