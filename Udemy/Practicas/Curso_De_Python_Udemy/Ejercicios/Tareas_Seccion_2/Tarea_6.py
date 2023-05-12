# Tarea 6: Condicional, mayor de edad
# Autor: David Rodríguez

def main():
    # Pedimos al usuario que ingrese su nombre y edad
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    
    # Evaluamos si el usuario es mayor de edad o no
    if edad >= 18:
        print(f"{nombre} eres mayor de edad")
    else:
        print(f"{nombre} no eres mayor de edad")

if __name__ == "__main__":
    main()
