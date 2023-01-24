# Abstracción
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass
    
    def diHola(Self):
        print("Hola")
    
class Perro(Animal):
    def sonido(self):
        print("Guau")
        
class Gato(Animal):
    def sonido(self):
        print("Miau")
        
def main():
    p = Perro()
    p.sonido()
    p.diHola()
    
    g = Gato()
    g.sonido()
    g.diHola()
    
main()
