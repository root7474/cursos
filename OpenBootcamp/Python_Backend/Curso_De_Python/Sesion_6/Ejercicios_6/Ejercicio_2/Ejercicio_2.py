# Ejercicio 6.2
# Autor: David Rodríguez

class alumno:
    def __init__(self):
        self.__nombre = None
        self.__nota = None
        
    def setNombre(self, nombre:str):
        self.__nombre = nombre
    
    def getNombre(self):
        return self.__nombre
    
    def setNota(self, nota:eval):
        self.__nota = nota
        
    def getNota(self):
        return self.__nota

def main():
    al = alumno()
    
    nombre = input("\nBienvenido... \nDigita tu nombre: ")
    nota = eval(input("Digita tu nota: "))
    al.setNombre(nombre)
    
    if nota >= 3 and nota <= 5:
        al.setNota(nota)
        print(f"\n{al.getNombre()} has aprobado con una nota de {al.getNota()} puntos.\n")
    elif nota >= 0 and nota <= 2.9:
        al.setNota(nota)
        print(f"\n{al.getNombre()} no has aprobado y te has quedado con una nota de {al.getNota()} puntos.\n")
    else:
        print("\nError!!... debes digitar una nota de 0 a 5 puntos.\n")
    
main()
