# Generadores
# Dexlaramos una función para calcular números impares
def impares():
    for numero in range(1, 50, 2):
        yield numero

def main():
    # Imprimimos un rango de números del 1 al 50 con un ciclo for
    """ for numero in range(1, 50):
        print(numero) """
    
    # Imprimimos el generador con un ciclo for
    """ for numero in impares():
        print(numero) """
    
    # Invocamos a la función "impares()"
    generador = impares()
    
    # Imprimimos a la variable "generador" con la función "next()"
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print("Terminando \"next()\" uno a uno\n")
    
    # Declaramos un for para continuar con el generador
    for numero in generador:
        print(numero)
    
if __name__ == "__main__":
    main()
    