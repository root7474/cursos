# Tarea 3: Mas sobre Variables
# Autor: David Rodríguez

def main():
    # Pedimos datos de usurio como el nombre y la edad
    nombre = input("Digita tu nombre: ")
    edad = eval(input("Digita tu edad: ")) # Convertimos la edad que ingrese el usuario a un tipo de dato numérico
    
    # Imprimimos los datos que ha ingresado el usuario y sus tipos por consola
    print(f"Nombre: {nombre}"
          f"\nEdad: {edad}"
          f"\n\nTipo de dato de nombre: {type(nombre)}"
          f"\nTipo de dato de edad: {type(edad)}")

if __name__ == "__main__":
    main()
    
