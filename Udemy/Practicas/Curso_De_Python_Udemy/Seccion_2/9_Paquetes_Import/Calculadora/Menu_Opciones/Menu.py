# Importamos los módulos de suma, resta, multiplicación, división y porcentahe con sus respectivos alias
import Operaciones.Suma as suma
import Operaciones.Resta as resta
import Operaciones.Multiplicacion as multiplicacion
import Operaciones.Division as division
import Operaciones.Porcentaje as porcentaje

# Creamos la función "menu()" que contendrá nuestro menú de opciones
def menu(nombre):
    salir = False # Declaramos una variable "salir" y la inicializamos en False
    
    # Mientras que "salir" sea igual a False, el programa se seguirá ejecutando
    # Hasta que "salir" sea igual a True
    while salir == False:
        # Si no se ingresan letras, caracteres especiales o números decimales
        # Se ejecutará lo siguiente
        try:
            opcion = int(input(f"\n{nombre}, digita una opción:\n"
                                "\n1.) Suma."
                                "\n2.) Resta."
                                "\n3.) Multiplicación."
                                "\n4.) División."
                                "\n5.) Calcular el porcentaje de un número"
                                "\n0.) Salir."
                                "\n\nOpción: ")) # Presentamos un menú de opciones y convertimos a eneteros lo que ingrese el usuario por consola
            
            if opcion == 1:
                # Suma
                cantidad = int(input(f"\nHaz elegido la opción \"{opcion}.) Suma.\"\n"
                                    "\nDigita una cantidad: ")) # Si "opcion" es igual a 1, pedimos que se ingrese una cantidad
                print(suma.suma(cantidad)) # Enviamos dicha cantidad a la función "suma" del módulo "Suma.py"
            elif opcion == 2:
                # Resta
                # Hacemos los mismos pasos para las operaciones de resta, multiplicación y división
                cantidad = int(input(f"\nHaz elegido la opción \"{opcion}.) Resta.\"\n"
                                    "\nDigita una cantidad: "))
                print(resta.resta(cantidad))
            elif opcion == 3:
                # Multiplicación
                cantidad = int(input(f"\nHaz elegido la opción \"{opcion}.) Multiplicación.\"\n"
                                    "\nDigita una cantidad: "))
                print(multiplicacion.multiplicacion(cantidad))
            elif opcion == 4:
                # División
                cantidad = int(input(f"\nHaz elegido la opción \"{opcion}.) División.\"\n"
                                    "\nDigita una cantidad: "))
                print(division.division(cantidad))
            elif opcion == 5:
                # Porcentaje
                NUMERO_PORCENTAJE = 100 # Para el caso de porcentaje, declaramos una constante y guardamos el número 100 dentro de ella
                print(f"\nHaz elegido la opción \"{opcion}.) Calcular el porcentaje de un número.\"\n")
                print(porcentaje.porcentaje(NUMERO_PORCENTAJE)) # Enviamos el número 100 a la función "porcentaje" del módulo "Porcentaje.py"
            elif opcion == 0:
                # Salir
                # Si la opción ingresada es 0, la variable "salir" será igual a True y el programa detendrá su ejecución
                print(f"\nHaz elegido la opción \"{opcion}.) Salir.\""
                    "\nHasta pronto...")
                salir = True
            else:
                print("Opción incorrecta!!!") # Esto se ejecutará si la opción ingresada es incorrecta
        except(ValueError):
            # Se ejecutará lo siguiente Hasta ingresar números enteros del 0 - 5
            print("Error!!!... No debes ingresar letras, símbolos especiales o números decimales")
