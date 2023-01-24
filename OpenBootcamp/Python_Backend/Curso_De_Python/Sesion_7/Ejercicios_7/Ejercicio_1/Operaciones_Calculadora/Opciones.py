# Clase que se utiliza para ingreso de datos de usuario, también contiene menú de opciones
# Importamos la clase "Operaciones" desde el módulo "Operaciones.py"
from Operaciones_Calculadora.Operaciones import Operaciones

class Opciones:
    # Inicializamos los atributos a usar
    def __init__(self):
        self.__nombre = None
        self.__opcion = 0
    
    def setNombre(self, nombre:str):
        self.__nombre = nombre
    
    def getNombre(self):
        return self.__nombre
    
    def setOpcion(self, opcion):
        if self.__opcion is not None:
            self.__opcion = opcion
        else:
            print("Variable is none")
    
    def getOpcion(self):
        return self.__opcion
    
    # Función donde el usuario deberá digitar su nombre y elegir una opción
    def menu(self, nombre):
        operaciones = Operaciones()
        self.setNombre(nombre)
        
        while(True):
            opcion = eval(input(f"\n{self.getNombre()}, Elige una opcion\n"
                                "\n1.) Sumar."
                                "\n2.) Restar."
                                "\n3.) Multiplicar."
                                "\n4.) Dividir."
                                "\n0.) Salir."
                                "\n\nOpcion: "))
        
            self.setOpcion(opcion)
            
            # Si el usuario elige la opción 1, el programa entrará a la operación de suma
            if self.getOpcion() == 1:
                print(f"\nHaz elegido la opción \"{self.getOpcion()}.) Sumar.\"")
                cantidad = eval(input("\nDigita una cantidad de números a sumar: "))
                operaciones.setCantidad(cantidad)
                operaciones.Sumar()
            
            # Si el usuario elige la opción 2,  el programa entrará a la operación de resta
            elif self.getOpcion() == 2:
                print(f"\nHaz elegido la opción \"{self.getOpcion()}.) Restar.\"")
                cantidad = eval(input("\nDigita una cantidad de números a restar: "))
                operaciones.setCantidad(cantidad)
                operaciones.Restar()
            
            # Si el usuario elige la opción 3,  el programa entrará a la operación de multiplicación
            elif self.getOpcion() == 3:
                print(f"\nHaz elegido la opción \"{self.getOpcion()}.) Multiplicar.\"")
                cantidad = eval(input("\nDigita una cantidad de números a multiplicar: "))
                operaciones.setCantidad(cantidad)
                operaciones.Multiplicar()
            
            # Si el usuario elige la opción 4,  el programa entrará a la operación de resta
            elif self.getOpcion() == 4:
                print(f"\nHaz elegido la opción \"{self.getOpcion()}.) Dividir.\"")
                cantidad = eval(input("\nDigita una cantidad de números a dividir: "))
                operaciones.setCantidad(cantidad)
                operaciones.Dividir()
            
            # Si el usuario elige la opción 0, el programa terminará su ejecución
            elif self.getOpcion() == 0:
                print(f"\nHaz elegido la opción \"{self.getOpcion()}.) Salir.\"\n"
                    "\nHasta pronto...\n")
                break
            
            else:
                print("Error!!!... Opción no valida.")
