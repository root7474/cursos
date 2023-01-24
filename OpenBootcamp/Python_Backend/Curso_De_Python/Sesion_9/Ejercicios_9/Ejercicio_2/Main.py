from functools import reduce

def miFuncion(x):
    if x % 2 != 0:
        return True
    
    return False

def suma(a, b):
    return a + b

def main():
    numeros = []
    cantidad = eval(input("\nDigita una cantidad: "))
    print()
    
    for i in range(cantidad):
        numeros_input = eval(input(f"Digita el número {i + 1}: "))
        numeros.append(numeros_input)
    
    resultado_1 = filter(miFuncion, numeros)
    resultado_2 = reduce(suma, filter(miFuncion, numeros))
    
    print(f"\nNúmeros impares: {sorted(list(resultado_1))}")
    print(f"Resultado de la suma: {resultado_2}\n")
    
if __name__ == "__main__":
    main()
