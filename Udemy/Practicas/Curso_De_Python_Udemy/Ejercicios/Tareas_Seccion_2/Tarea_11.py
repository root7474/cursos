# Tarea: Funcion bisiesto
# Autor: David Rodríguez

def main():
    # Pedimos al usuario que ingrese su nombre y cualquier año para saber si es bisiesto
    nombre = input("Bienvenido... ingressa tu nombre")
    anyo = int(input(f"{nombre} ingresa un año: "))
    anyo_bisiesto = (lambda anyo: anyo % 4)(anyo) # Calculamos si el año es bisiesto con una función lambda
    
    if anyo_bisiesto == 0:
        # Si el año es bisiesto
        print(f"El año {anyo} es bisiesto") # Imprimimos que dicho año es bisiesto
    else:
        # Dado el caso de que no sea bisiesto
        print(f"El año {anyo} no es bisiesto") # Imprimimos que dicho año no es bisiesto
    
if __name__ == "__main__":
    main()
