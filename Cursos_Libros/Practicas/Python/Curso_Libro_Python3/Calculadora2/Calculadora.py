nombre = input("Bienvenido...\n" +
               "Digíta tu nombre: ")

def Sumar():
    print("\n\nHaz elegído la opción '1.) Sumar.'")
    cantidad = eval(input("Digita la cantidad a sumar: "))
    print()

    suma = None

    for i in range(cantidad):
        numero = eval(input("Digita el número " + str(i + 1) + ": "))

        if suma == None:
            suma = numero
        else:
            suma = suma + numero
    print("\nEl resultado de la suma es: " + str(suma) + "\n")

def Restar():
    print("\n\nHaz elegído la opción '2.) Restar.'")
    cantidad = eval(input("Digita la cantidad a restar: "))
    print()

    resta = None

    for i in range(cantidad):
        numero = eval(input("Digita el número " + str(i + 1) + ": "))

        if resta == None:
            resta = numero
        else:
            resta = resta - numero
    print("\nEl resultado de la resta es: " + str(resta) + "\n")

def Multiplicar():
    print("\n\nHaz elegído la opción '3.) Multiplicar.'")
    cantidad = eval(input("Digita la cantidad a multiplicar: "))
    print()

    multiplicar = None

    for i in range(cantidad):
        numero = eval(input("Digita el número " + str(i + 1) + ": "))

        if multiplicar == None:
            multiplicar = numero
        else:
            multiplicar = multiplicar * numero
    print("\nEl resultado de la multiplicación es: " + str(multiplicar) + "\n")

def Dividir():
    print("\n\nHaz elegído la opción '4.) Dividir.'")
    cantidad = eval(input("Digita la cantidad a dividir: "))
    print()

    division = None

    for i in range(cantidad):
        numero = eval(input("Digita el número " + str(i + 1) + ": "))

        if division == None:
            division = numero
        else:
            division = division / numero
    print("\nEl resultado de la división es: " + str(division) + "\n")

def Resto():
    print("\n\nHaz elegído la opción '5.) Resto de una división.'")
    print("Solo puedes digitar 2 números")
    print()

    resto = None

    for i in range(2):
        numero = eval(input("Digita el número " + str(i + 1) + ": "))

        if resto == None:
            resto = numero
        else:
            resto = resto % numero
    print("\nEl resultado del resto de la división es: " + str(resto) + "\n")

def Salir():
    print("\n\nHaz elegído la opción '0.) Salir.'" +
          "\n\nHasta pronto!!!...")

def main():
    opcion = int(input("\n\nQué deseas hacer " + nombre + "?:" +
                       "\n1.) Sumar." +
                       "\n2.) Restar." +
                       "\n3.) Multiplicar." +
                       "\n4.) Dividir." +
                       "\n5,) Resto de una división" +
                       "\n0.) Salir"
                       "\n\nOpción: "))

    while(True):
        if opcion == 1:
            Sumar()
        elif opcion == 2:
            Restar()
        elif opcion == 3:
            Multiplicar()
        elif opcion == 4:
            Dividir()
        elif opcion == 5:
            Resto()
        elif opcion == 0:
            Salir()
            break
        else:
            print("Error!!!... Opción Equivocada!!!")

        opcion = int(input("\nQué más deseas hacer " + nombre + "?:" +
                           "\n1.) Sumar." +
                           "\n2.) Restar." +
                           "\n3.) Multiplicar." +
                           "\n4.) Dividir." +
                           "\n5,) Resto de una división" +
                           "\n0.) Salir"
                           "\n\nOpción: "))

main()
