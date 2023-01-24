# Suma
def Suma(cant):
    suma = None
    print()

    for i in range(cant):
        num = eval(input(f"Digita el número {i + 1}: "))
        if suma == None:
            suma = num
        else:
            suma = suma + num
        
    print(f"\nEl resultado de la suma es: {suma}")
    return(suma)

# Resta
def Resta(cant):
    resta = None
    print()

    for i in range(cant):
        num = eval(input(f"Digita el número {i + 1}: "))
        if resta == None:
            resta = num
        else:
            resta = resta - num

    print(f"\nEl resultado de la resta es: {resta}")
    return(resta)

# Multiplicacion
def Multiplicacion(cant):
    multiplicacion = None
    print()

    for i in range(cant):
        num = eval(input(f"Digita el número {i + 1}: "))
        if multiplicacion == None:
            multiplicacion = num
        else:
            multiplicacion = multiplicacion * num

    print(f"\nEl resultado de la multiplicacion es: {multiplicacion}")
    return(multiplicacion)

# Division
def Division(cant):
    division = None
    print()

    for i in range(cant):
        num = eval(input(f"Digita el número {i + 1}: "))
        if division == None:
            division = num
        else:
            division = division / num

    print(f"\nEl resultado de la division es: {division}")
    return(division)

# Modulo de una división
def Modulo(cant):
    modulo = None
    print()

    for i in range(cant):
        num = eval(input(f"Digita el número {i + 1}: "))
        if modulo == None:
            modulo = num
        else:
            modulo = modulo % num

    print(f"\nEl resultado de la modulo de la división es: {modulo}")
    return(modulo)

def menu(nombre):
    opcion = eval(input(f"\nQué deseas hacer {nombre}?: \n"
                         "\n1.) Sumar."
                         "\n2.) Restar."
                         "\n3.) Multiplicar"
                         "\n4.) Dividir"
                         "\n5.) Modulo de un división."
                         "\n0.) Salir \n"
                         "\nOpción: "))
    return(opcion)

def main():
    nombre = input("\nBienvenido..." +
                   "\nDigita tu nombre: ")
    opcion = menu(nombre)

    while(True):
        # Suma
        if (opcion == 1):
            print("\nHaz elegido la opción \"1.) Sumar.\"")
            cantidad = eval(input("\nDigita una cantidad de números a sumar: "))
            Suma(cantidad)

        # Resta
        elif (opcion == 2):
            print("\nHaz elegido la opción \"2.) Restar.\"")
            cantidad = eval(input("\nDigita una cantidad de números a restar: "))
            Resta(cantidad)

        # Multiplicación
        elif (opcion == 3):
            print("\nHaz elegido la opción \"3.) Multiplicar.\"")
            cantidad = eval(input("\nDigita una cantidad de números a multiplicar: "))
            Multiplicacion(cantidad)

        # División
        elif (opcion == 4):
            print("\nHaz elegido la opción \"3.) Dividir.\"")
            cantidad = eval(input("\nDigita una cantidad de números a dividir: "))
            Division(cantidad)

        # Módulo
        elif (opcion == 5):
            print("\nHaz elegido la opción \"3.) Modulo de una división.\"" +
                  "\nSolo debes digitar 2 números: ")
            cantidad = 2
            Modulo(cantidad)

        # Salir
        elif (opcion == 0):
            print("\nHaz elegido la opcion \"0.) Salir\"... \n" +
                  "\nHasta pronto!!!... \n")
            break

        # Error
        else:
            print("\nError!!!... Opción incorrecta!!!")

        opcion = menu(nombre)

main()
