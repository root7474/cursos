# Importamos el módulo math
import math
# from math import sqrt

def main():
    numero = eval(input("Dime un número y te indico su raíz: "))
    print(f"La raíz cuadrada de {numero} es: {math.sqrt(numero)}")
    
if __name__ == "__main__":
    main()
