# Clase que se utiliza para realizar los calculos de forma sucesiva

class Operaciones:
    # Inicializamos los atributos a usar
    def __init__(self):
        self.__cantidad = None
    
    def setCantidad(self, cantidad):
        self.__cantidad = cantidad
    
    def getCantidad(self):
        return self.__cantidad
    
    # Función para operación de suma
    def Sumar(self):
        suma = None
        print()
        
        for i in range(self.getCantidad()):
            numero = eval(input(f"Digita el número {i + 1}: "))
            
            if suma == None:
                suma = numero
            else:
                suma = suma + numero
            
        print(f"\nEl resultado de la suma es: {suma}\n")
        
    # Función para operación de resta
    def Restar(self):
        resta = None
        print()
        
        for i in range(self.getCantidad()):
            numero = eval(input(f"Digita el número {i + 1}: "))
            
            if resta == None:
                resta = numero
            else:
                resta = resta - numero
            
        print(f"\nEl resultado de la resta es: {resta}\n")
    
    # Función para operación de multiplicación
    def Multiplicar(self):
        multi = None
        print()
        
        for i in range(self.getCantidad()):
            numero = eval(input(f"Digita el número {i + 1}: "))
            
            if multi == None:
                multi = numero
            else:
                multi = multi * numero
            
        print(f"\nEl resultado de la multiplicación es: {multi}\n")
    
    # Función para operación de división
    def Dividir(self):
        division = None
        print()
        
        for i in range(self.getCantidad()):
            numero = eval(input(f"Digita el número {i + 1}: "))
            
            if division == None:
                division = numero
            else:
                division = division / numero
            
        print(f"\nEl resultado de la división es: {division}\n")
    