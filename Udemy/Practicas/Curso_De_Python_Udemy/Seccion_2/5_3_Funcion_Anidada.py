# Programa: Calculadora desde consola
# Autor: David Rodríguez

# Creamos una función que contendrá las operaciones aritméticas de nuestra claculadora
# La función contiene dos parámetros que son cantidad y opció que por defecto tiene el número 1
def calculadora(cantidad, opcion = 1):
    def suma(cantidad): # Función suma() que recibirá como parámetro una acantidad de números
        suma = None # Definimos una variable suma como nula
        
        # Iteramos la cantidad de números digitada por el usuario 
        for i in range(cantidad):
            num = eval(input(f"Digita la cantidad {i + 1}: ")) # En cada iteración se le pedirá al usuario digitar un número
            
            if suma == None:
                suma = num # Si la variable suma es nula entonces le asignamos lo que halla en la variable num
            else:
                suma = suma + num # Si existe un valor dentro de la variable suma, entonces sumamos el valor de suma con el valor de num
        print(f"\nLa suma es: {suma}") # Imprimimos el resultado de la suma
        
    def resta(cantidad): # Para la función resta(), hacemos los mismos pasos que con la función suma()
        resta = None # Esta vez definimos una variable resta como nula
        
        # Volvemos a iterar una cantidad de números digitada por el usuario
        for i in range(cantidad):
            num = eval(input(f"Digita la cantidad {i + 1}: "))
            
            if resta == None:
                resta = num # Como en la variable suma, la variable resta también recibe lo que halla en num si es que es nula
            else:
                resta = resta - num # Sino, restamos el valor de resta con el valor de num
        print(f"\nLa resta es: {resta}") # Imprimimos el resultado de la resta
    
    # Se repiten los mismos pasos para las funciones multiplicacion() y division()    
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
        
    # La función porcentaje calculará el porcentaje de un número ingresado por el usuario
    def porcentaje(cantidad): # Más adelante el parámetro cantidad tendrá un valor de 100 por defecto
        num = eval(input("Digita un número: ")) # Pedímos un número al usuario
        porcentaje = num / cantidad # Hacemos una división para calcular el porcentaje del número ingresado
        print(f"\nEl porcentaje de {num} es: {porcentaje}") # Imprimimos el porcentaje del número ingresado
    
    # Enviamos la cantidad de números ingresada a la operación escogida por el usuario
    if opcion == 1:
        suma(cantidad) # Para el caso de la suma
    if opcion == 2:
        resta(cantidad) # Para el caso de la resta
    if opcion == 3:
        multiplicacion(cantidad) # Para el caso de la multiplicación
    if opcion == 4:
        division(cantidad) # Para el caso de la división
    if opcion == 5:
        porcentaje(cantidad) # Para el caso del porcentaje de un número

# Definimos una función menu_usuario con el parámetro nombre
def menu_usuario(nombre):
    while(True): # Iteramos todas las opciones hasta que el usuario decida finalizar el programa con ctrl + D, ctrl + C o oprimiendo la opción "0"
        try: # Generamos un try para el caso de que el programa no genere errores por parte del usuario
            # Imprimimos un menú de opciones
            opcion = eval(input(f"\n{nombre} Digita una opción:\n"
                            "\n1.) Suma."
                            "\n2.) Resta."
                            "\n3.) Multiplicación."
                            "\n4.) División"
                            "\n5.) Porcentaje"
                            "\n0.) Salir"
                            "\n\nOpción: "))
            
            if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4:
                cantidad = eval(input("Digita una cantidad: ")) # El usuario deberá digitar una cantidad en el caso en que escoja una opción del 1 - 4
                print() # Generamos un salto de línea
            elif opcion == 5:
                cantidad = 100 # Si el usuario gita la opción 5, la variable cantidad tendrá un valor de 100 por defecto
            elif opcion == 0:
                print("Hasta pronto") # Si la opción digitada es "0", se romperá el ciclo y finalizará el programa
                break
            else:
                print("\nError!!!... Opción incorrecta") # Si laopción digitada es incorrecta, el programa lanzará un error y continuará con su ejecución
                continue
                
            calculadora(cantidad, opcion) # Llamamos a la función calculadora() y le pasamos la cantidad de números y la opción digitada por el usuario
        except(SyntaxError, NameError): # Genrámos una excepción para el caso de que el usuario digite un valor vacio o cualquier caracter que no sea un número
            print("\nError!!!... Por favor ingresa solo números") # Imprimimos un mensaje de error pidiéndole al usario que digite solo números
            
def main():
    # Dentro de la función principal, generamos un try para el caso de que el usario no presione ctrl + D o ctrl + C
    try:
        nombre = input("Bienvenido...\nDigita tu nombre: ") # Damosun mensaje de bienevenida y pedimos el nombre del usuario
        menu_usuario(nombre) # Llamamos a la funcón menu_usuario() y le enviamos el nombre del usuario
    except(EOFError, KeyboardInterrupt):
        print("\nHasta pronto") # Generamos un mensaje de despedida para el caso de que el usuario decida interrumpir la ejecución del programa
        exit() # Con exit(), finalizamos la ejecución del programa
        
if __name__ == "__main__":
    main()
