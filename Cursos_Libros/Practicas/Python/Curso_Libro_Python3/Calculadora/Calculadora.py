nombre = input("\nBinevenido...\n" +
               "\nDigita tu nombre: ")
def Suma():
    cantidad = eval(input("\n\nHas elegído la opción 'Suma'" +
                          "\nDigita la cantidad de números: "))

    suma = None
    
    for i in range(cantidad):
        numero = eval(input("Digita el número " + str(i + 1) + ": "))

        if suma == None:
            suma = numero
        else:
            suma = suma + numero
    print("\nEl resultado de la suma es: " + str(suma) + "\n")
    
def resta():
    cantidad = eval(input("\n\nHas elegído la opción 'Resta'" +
                          "\nDigita la cantidad de números: "))
    print()

    resta = None
    
    for i in range(cantidad):
        numero = eval(input("Digita el número " + str(i + 1) + ": "))

        if resta == None:
            resta = numero
        else:
            resta = resta - numero
    print("\nEl resultado de la resta es: " + str(resta) + "\n")
    
def multiplicacion():
    cantidad = eval(input("\n\nHas elegído la opción 'Multiplicar'" +
                          "\nDigita la cantidad de números: "))
    print()

    multiplicacion = None
    
    for i in range(cantidad):
        numero = eval(input("Digita el número " + str(i + 1) + ": "))

        if multiplicacion == None:
            multiplicacion = numero
        else:
            multiplicacion = multiplicacion * numero
    print("\nEl resultado de la multiplicación es: " + str(multiplicacion) + "\n")
    
def division():
    cantidad = eval(input("\n\nHas elegído la opción 'Dividir'" +
                          "\nDigita la cantidad de números: "))
    print()

    division = None
    
    for i in range(cantidad):
        numero = eval(input("Digita el número " + str(i + 1) + ": "))

        if division == None:
            division = numero
        else:
            division = division / numero
    print("\nEl resultado de la división es: " + str(division) + "\n")
    
def resto():
    print("\n\nSolo puedes digitar dos números...\n")
    resto = None
    
    for i in range(2):
        numero = eval(input("Digita el número " + str(i + 1) + ": "))

        if resto == None:
            resto = numero
        else:
            resto = resto % numero
    print("\nEl resultado del resto de la división es: " + str(resto) + "\n")

def main():
    while(True):
        opcion = eval(input("\nQue deseas hacer " + nombre + "?:\n" +
                            "\n1.) Suma" +
                            "\n2.) Resta" +
                            "\n3.) Multplicar" +
                            "\n4.) División" +
                            "\n5.) Resto" +
                            "\n0.) Salir" +
                            "\n\nOpción: "))

        if opcion == 1:
            Suma()
        elif opcion == 2:
            resta()
        elif opcion == 3:
            multiplicacion()
        elif opcion == 4:
            division()
        elif opcion == 5:
            resto()
        elif opcion == 0:
            print("\n\nHasta pronto...\n")
            break
        else:
            print("\nOpcion incorrecta!!!...\n")

main()
