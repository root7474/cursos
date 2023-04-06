def calculadora(cantidad, opcion = 1):
    def suma(cantidad):
        suma = None
        
        for i in range(cantidad):
            num = eval(input(f"Digita la cantidad {i + 1}: "))
            
            if suma == None:
                suma = num
            else:
                suma = suma + num
        print(f"\nLa suma es: {suma}")
        
    def resta(cantidad):
        resta = None
        
        for i in range(cantidad):
            num = eval(input(f"Digita la cantidad {i + 1}: "))
            
            if resta == None:
                resta = num
            else:
                resta = resta - num
        print(f"\nLa resta es: {resta}")
        
    def multiplicacion(cantidad):
        multiplicacion = None
        
        for i in range(cantidad):
            num = eval(input(f"Digita la cantidad {i + 1}: "))
            
            if multiplicacion == None:
                multiplicacion = num
            else:
                multiplicacion = multiplicacion * num
        print(f"\nLa multiplicación es: {multiplicacion}")
        
    def division(cantidad):
        try:
            division = None
            
            for i in range(cantidad):
                num = eval(input(f"Digita la cantidad {i + 1}: "))
                
                if division == None:
                    division = num
                else:
                    division = division / num
            print(f"\nLa división es: {division}")
        except ZeroDivisionError:
            print("\nError!!!... División por cero.")
        
    def porcentaje(cantidad = 100):
        porcentaje = cantidad
        num = eval(input("Digita un número: "))
        porcentaje = num / porcentaje
        
        print(f"\nEl porcentaje de {num} es: {porcentaje}")
        
    if opcion == 1:
        suma(cantidad)
    elif opcion == 2:
        resta(cantidad)
    elif opcion == 3:
        multiplicacion(cantidad)
    elif opcion == 4:
        division(cantidad)
    elif opcion == 5:
        porcentaje(cantidad)
    
def menu_usuario(nombre):
    while(True):
        try:
            opcion = eval(input(f"\n{nombre} Digita una opción:\n"
                            "\n1.) Suma."
                            "\n2.) Resta."
                            "\n3.) Multiplicación."
                            "\n4.) División"
                            "\n5.) Porcentaje"
                            "\n0.) Salir"
                            "\n\nOpción: "))
            
            match opcion:
                case 1:
                    cantidad = eval(input("Digita una cantidad: "))
                    print()
                case 2:
                    cantidad = eval(input("Digita una cantidad: "))
                    print()
                case 3:
                    cantidad = eval(input("Digita una cantidad: "))
                    print()
                case 4:
                    cantidad = eval(input("Digita una cantidad: "))
                    print()
                case 5:
                    cantidad = 100
                case 0:
                    print("Hasta pronto")
                    break
                
            if opcion < 0 or opcion > 5:
                print("\nError!!!... Opción incorrecta")
                continue
                
            calculadora(cantidad, opcion)
        except(SyntaxError, NameError):
            print("\nError!!!... Por favor ingresa un número")
            
def main():
    try:
        nombre = input("Bienvenido...\nDigita tu nombre: ")
        menu_usuario(nombre)
    except EOFError:
        print()
        exit()
        
if __name__ == "__main__":
    main()
