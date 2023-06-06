# Tarea 10: Función es primo
# Autor: David Rodríguez

# Creamos una función para calcular si un número es primo o no
# Le pasamos como parámetro el número que ingrese el usuario
def es_primo(numero):
    contador = 2 # Declaramos una variable "contador" y la inicializamos en 2
    
    # Los siguientes son casos especiales
    if numero == 0 or numero == 1 or numero == 4: return False
    
    # Mientras que "contador" sea menor a la división entre el número ingresado y 2
    # Haremos lo siguiente
    while contador < numero / 2:
        contador += 1 # Incrementamos "contador" en 1
        if numero % contador == 0: return False # Devolvemos false si el resto de la división entre "contador" es cero
    
    return True # Devolvemos True si no se cumple ninguna de las condiciones de arriba

def main():
    # Pedimos que se ingrese los datos del usuario y un nuúmero para calcular si es primo o no
    nombre = input("Bienvenido... Digita tu nombre: ")
    numero = eval(input(f"{nombre} digita un número: "))
    resultado = es_primo(numero) # Enviamos el número ingresado por el usuario a la función "es_primo()"
    
    if resultado == True:
        # Si "resultado" es igual a True
        print(f"El número {numero} es primo") # Imprimimos por consola que el número ingresado es primo
    else:
        # Dado el caso de que resultado no sea True
        print(f"El número {numero} no es primo") # Imprimimos por consola que el número ingresado no es primo

if __name__ == "__main__":
    main()
