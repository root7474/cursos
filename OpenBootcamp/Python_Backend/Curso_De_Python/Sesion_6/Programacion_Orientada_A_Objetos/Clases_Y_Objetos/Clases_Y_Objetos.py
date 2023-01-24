from tkinter.messagebox import NO


class Juguete:
    __encendidio = True
    
    def __init__(self, x):
        print("Estoy en el constructor de la clase Juguete", x )
    
    def enciende(self):
        print("Apagó el aparato: ")
        self.__encendidio = True
    
    def apaga(self):
        print("Apagó el aparato: ")
        self.__encendidio = False
        
    def isEncendido(self):
        return self.__encendidio

# Herencia
class Dino(Juguete):
    color = None
    nombre = None
    
    def __init__(self, nombre):
        # Juguete.__init__(self, nombre)
        super().__init__(nombre)
        print("Estoy en el constructor de la clase Dino")
        
    def verEscamas(self):
        pass
    
def main():
    d = Dino("David")
    
main()
    