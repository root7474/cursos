# Tarea 6: Bucles, numeros pares mostrados en orden inverso
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
                lista_pares = [] # Aquí guardarémos una lista de números ingresados por el usuario
                lista_seleccion_pares = [] # Aquí guardarémos como resultado una selección de números pares
                cantidad = eval(input(f"{nombre} ingresa una cantidad de números: ")) # Pedimos que el usuario digite uns cantidad de números a ingresar
                
                # Recorremos dicha cantidad
                for i in range(cantidad):
                    numero = eval(input(f"Digita el número {i + 1}: ")) # En cada iteración pedimos que se ingrese un número
                    if numero % 2 == 0: lista_pares.append(numero) # Evaluamos si un número es par y lo agregamos a la lista de números pares
                lista_pares.sort() # Si el usuario ingresa números de manera aleatoria, ordenamos la lista con la función "sort()"
                print(f"\nLista números pares: {lista_pares}") # Imprimimos todos los elementos de la lista de números pares
                
                # Pedimos que el usuario ingrese un número de inicio y de fin
                numero_inicio = eval(input(f"\n{nombre} digita un número de inicio: "))
                numero_fin = eval(input(f"{nombre} digita un número de fin: "))
                
                
                # Si los números que ha ingresado el usuario están dentro de la lista, entonces se ejecutará lo siguiente
                if numero_inicio in lista_pares and numero_fin in lista_pares:
                    if numero_inicio < numero_fin: # Dado el caso de que el número de inicio sea menor que el número de fin
                        for i in range(lista_pares.index(numero_inicio), lista_pares.index(numero_fin) + 1):
                            lista_seleccion_pares.append(lista_pares[i]) # Recorremos un rango desde el índice de número de inicio hasta el indice de número de fin de la lista
                        opcion = int(input("Deseas que tu lista tenga un orden inverso? (1. si, 2. no): "))
                        
                        match opcion:
                            case 1:
                                lista_seleccion_pares.reverse() # Dado el caso de que la opción sea 1, hacemos que nuestra lista tenga un orden inverso
                                print(f"\nLista números pares modificada: {lista_seleccion_pares}")
                            case 2:
                                print(f"\nLista números pares modificada: {lista_seleccion_pares}") # si la opción es 2, solo imprimimos la lista
                        
                    else: # Dado el caso de que el número de inicio sea mayor que el número de fin
                        for i in range(lista_pares.index(numero_inicio), lista_pares.index(numero_fin) - 1, -1):
                            lista_seleccion_pares.append(lista_pares[i]) # Recorremos un rango desde el índice de número de inicio hasta el indice de número de fin de la lista con paso de -1
                        print(f"\nLista números pares modificada: {lista_seleccion_pares}") # Imprimimos la nueva lista
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
