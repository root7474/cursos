""" for numero in range(1, 50):
    print(numero) """
    
# Generadores
def impares():
    for numero in range(1, 50, 2):
        yield numero

def main():
    """ for numero in impares():
        print(numero) """
    
    generador = impares()
    
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print("Terminando next uno a uno y pasamos a bucle for")
    
    for numero in generador:
        print(numero)
    
if __name__ == "__main__":
    main()
