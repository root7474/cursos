# Tarea 6: Bucles, numeros impares
# Autor: David Rodríguez

def main():
    condicion_while = False # Esta variable que nos servirá como condición para la ejecución del programa
    nombre = input("Ingresa tu nombre: ") # Pedimos un nombre al usuario

    # Lo siguiente se ejecutará si la variable "condicion_while" es igual a False
    while condicion_while == False:
        opcion = eval(input(f"{nombre} deseas continuar (1. si, 2. no)?: ")) # Le pedimos al usuario que ingrese una opción entre 1 y 2
        
        match opcion:
            case 1:
                # Dado el caso de que la opción sea 1
                # Declaramos dos variables de tipo lista
                lista_impares = [] # Aquí guardarémos una lista de números ingresados por el usuario
                lista_seleccion_impares = [] # Aquí guardarémos como resultado una selección de números impares
                cantidad = eval(input(f"{nombre} ingresa una cantidad de números: ")) # Pedimos que el usuario digite uns cantidad de números a ingresar
                
                # Recorremos dicha cantidad
                for i in range(cantidad):
                    numero = eval(input(f"Digita el número {i + 1}: ")) # En cada iteración pedimos que se ingrese un número
                    if numero % 2 != 0: lista_impares.append(numero) # Evaluamos si un número es impar y lo agregamos a la lista de números impares
                lista_impares.sort() # Si el usuario ingresa números de manera aleatoria, ordenamos la lista con la función "sort()"
                print(f"\nLista números impares: {lista_impares}") # Imprimimos todos los elementos de la lista de números impares
                
                # Pedimos que el usuario ingrese un número de inicio y de fin
                numero_inicio = eval(input(f"\n{nombre} digita un número de inicio: "))
                numero_fin = eval(input(f"{nombre} digita un número de fin: "))
                
                # Si los números que ha ingresado el usuario están dentro de la lista, entonces se ejecutará lo siguiente
                if numero_inicio in lista_impares and numero_fin in lista_impares:
                    if numero_inicio < numero_fin: # Dado el caso de que el número de inicio sea menor que el número de fin
                        for i in range(lista_impares.index(numero_inicio), lista_impares.index(numero_fin) + 1):
                            lista_seleccion_impares.append(lista_impares[i]) # Recorremos un rango desde el índice de número de inicio hasta el indice de número de fin de la lista
                        print(f"\nLista números impares modificada: {lista_seleccion_impares}") # Imprimimos la nueva lista
                        
                    else: # Dado el caso de que el número de inicio sea mayor que el número de fin
                        for i in range(lista_impares.index(numero_inicio), lista_impares.index(numero_fin) - 1, -1):
                            lista_seleccion_impares.append(lista_impares[i]) # Recorremos un rango desde el índice de número de inicio hasta el indice de número de fin de la lista con paso de -1
                        print(f"\nLista números impares modificada: {lista_seleccion_impares}") # Imprimimos la nueva lista
                else:
                    print("Error!!!... número descoconocido") # Si los números ingresados no están dentro de la lista, se nos mostrará este error
                    
            case 2:
                # Dado el caso de que la opción sea 2, la condición del bucle tendrá un valor de True
                # Y el programa terminará su ejecución
                print("Hasta luego...")
                condicion_while = True
            case default:
                print("Error!!!... Opción incorrecta") # Si la opción es incorrecta, se nos mostrará este error

if __name__ == "__main__":
    main()
