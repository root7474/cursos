class auto:
    def __init__(self):
        self.marca = None
        self.velocidad = None
        self.kilometraje = None

def main():
    coche = auto()

    coche.marca = input("\nBienvenido... \n" +
                  "\nDigita la marca del auto: ")
    
    coche.velocidad = eval(input("Digita su velocidad: "))
    coche.kilometraje = eval(input("Digita su kilometraje: "))
    
    if coche.kilometraje == 0:
        print(f"El auto es de marca {coche.marca} de velocidad {coche.velocidad} km/h" +
              f" de kilometraje {coche.kilometraje} km." + 
              "\n\nEl auto es nuevo!!!.\n")
        
    elif coche.kilometraje > 0:
        print(f"El auto es de marca {coche.marca} de velocidad {coche.velocidad} km/h" +
              f" de kilometraje {coche.kilometraje} km" +
              "\n\nEl auto es usado.\n")
        
    else:
        print("\nError!!!... no existe un kilometraje negativo\n")

main()
