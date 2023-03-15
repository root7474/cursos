# Prgrama de calculadora básica para consola en Python
# Autor: David Rodríguez

# Creamos una función suma() con el parámetro cantidad
def suma(cantidad):
    suma = None
    
    # Iteramos con un for la cantidad de números a sumar y calculamos su resultado
    for i in range(cantidad):
        i += 1
        numero = eval(input(f"Digita el número {i}: ")) # Pedimos un número al usuario
        
        # Dado el caso que suma sea igual a None le agregaremos lo que tenemos en numero
        if suma == None:
            suma = numero
        else:
            suma = suma + numero # Si suma ya no es igual None, haremos la respectiva operación

    print(f"\nEl resultado de la suma es: {suma}\n") # Imprimimos el resultado de la suma

# Creamos una función resta() con el parámetro cantidad
def resta(cantidad):
    resta = None
    
    # Iteramos con un for la cantidad de números a restar y calculamos su resultado
    for i in range(cantidad):
        i += 1
        numero = eval(input(f"Digita el número {i}: ")) # Pedimos un número al usuario
        
        # Dado el caso que resta sea igual a None le agregaremos lo que tenemos en numero
        if resta == None:
            resta = numero
        else:
            resta = resta - numero # Si resta ya no es igual None, haremos la respectiva operación

    print(f"\nEl resultado de la resta es: {resta}\n") # Imprimimos el resultado de la resta

# Creamos una función multiplicacion() con el parámetro cantidad
def multiplicacion(cantidad):
    multiplicacion = None
    
    # Iteramos con un for la cantidad de números a multiplicar y calculamos su resultado
    for i in range(cantidad):
        i += 1
        numero = eval(input(f"Digita el número {i}: ")) # Pedimos un número al usuario
        
        # Dado el caso que multiplicacion sea igual a None le agregaremos lo que tenemos en numero
        if multiplicacion == None:
            multiplicacion = numero
        else:
            multiplicacion = multiplicacion * numero # Si multiplicacion ya no es igual None, haremos la respectiva operación

    print(f"\nEl resultado de la multiplicación es: {multiplicacion}\n") # Imprimimos el resultado de la multiplicación

# Creamos una función division() con el parámetro cantidad
def division(cantidad):
    division = None
    
    # Iteramos con un for la cantidad de números a multiplicar y calculamos su resultado
    for i in range(cantidad):
        i += 1
        numero = eval(input(f"Digita el número {i}: ")) # Pedimos un número al usuario
        
        # Dado el caso que division sea igual a None le agregaremos lo que tenemos en numero
        if division == None:
            division = numero
        else:
            division = division / numero # Si division ya no es igual None, haremos la respectiva operación

    print(f"\nEl resultado de la división es: {division}\n") # Imprimimos el resultado de la división

# Creamos una función resto() con el parámetro cantidad
# El usuario solo ṕodrá calcular la cantidad definida por el sistema
# Es decir solo podrá calcular 2 números
def resto(cantidad):
    resto = None
    print("Solo puedes calcular dos números\n")
    
    # Iteramos con un for la cantidad de números a multiplicar y calculamos su resultado
    for i in range(cantidad):
        i += 1
        numero = eval(input(f"Digita el número {i}: ")) # Pedimos un número al usuario
        
        # Dado el caso que resto sea igual a None le agregaremos lo que tenemos en numero
        if resto == None:
            resto = numero
        else:
            resto = resto % numero # Si resto ya no es igual None, haremos la respectiva operación

    print(f"\nEl resultado del resto de la división es: {resto}\n") # Imprimimos el resultado

# Creamos una función para el menú de opciones
def opciones():
    nombre = input("Bienvenido..."
                   "\nDigita tu nombre: ") # Pedimos el nombre del usuario
    
    # Iteramos el menú de opciones hasta que el usuario rompa el ciclo
    while(True):
        opciones = eval(input(f"{nombre} escoge una opción:\n"
                            "\n1.) Suma."
                            "\n2.) Resta."
                            "\n3.) Multiplicación."
                            "\n4.) División."
                            "\n5.) Resto de una división."
                            "\n0.) Salir"
                            "\n\nOpción: "))
        
        # Dado el caso de que el usuario escoja la opción 1
        if opciones == 1:
            print("\nHaz elegido la opción: \"1.) Suma.\"")
            cantidad = eval(input("Digita una cantidad de números a sumar: ")) # Le pedimos al usuario que digite una cantidad
            print()

            suma(cantidad) # Enviamos esa cantidad a nuestra función de suma()
            
        # Dado el caso de que el usuario escoja la opción 2
        elif opciones == 2:
            print("\nHaz elegido la opción: \"1.) Resta.\"")
            cantidad = eval(input("Digita una cantidad de números a restar: ")) # Le pedimos al usuario que digite una cantidad
            print()

            resta(cantidad) # Enviamos esa cantidad a nuestra función de resta()

        # Dado el caso de que el usuario escoja la opción 3
        elif opciones == 3:
            print("\nHaz elegido la opción: \"1.) Multiplicación.\"")
            cantidad = eval(input("Digita una cantidad de números a multiplicar: ")) # Le pedimos al usuario que digite una cantidad
            print()

            multiplicacion(cantidad) # Enviamos esa cantidad a nuestra función de multiplicacion()

        # Dado el caso de que el usuario escoja la opción 4
        elif opciones == 4:
            print("\nHaz elegido la opción: \"1.) División.\"")
            cantidad = eval(input("Digita una cantidad de números a dividir: ")) # Le pedimos al usuario que digite una cantidad
            print()

            division(cantidad) # Enviamos esa cantidad a nuestra función de division()

        # Dado el caso de que el usuario escoja la opción 5
        elif opciones == 5:
            print("\nHaz elegido la opción: \"1.) Resto de una división.\"")
            cantidad = 2 # Para este caso, el número 2 será la cantidad definida por el sistema
            resto(cantidad) # Enviamos esa cantidad a nuestra función de resto()

        # Dado el caso de que el usuario escoja la opción 0
        elif opciones == 0:
            print("\nHaz elegido la opción: \"0.) Salir.\""
                  "\n\nHasta pronto!!!...")
            break # EL programa romperá el ciclo y dará fin a su ejecución
        
        # Dado el caso de que el usuario digite una opción incorrecta
        else:
            print("\nError!!!... Opción incorrecta.\n")

# Función principal de ejecució del programa
def main():
    opciones() # Llamamos a la función de opciones()
    
if __name__ == "__main__":
    main()
