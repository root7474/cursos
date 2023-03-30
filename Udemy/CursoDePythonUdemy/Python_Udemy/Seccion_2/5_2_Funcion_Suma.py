def suma(num_1, num_2):
    resultado = num_1 + num_2
    return resultado

def main():
    num_1 = int(input("Dime el primer número: "))
    num_2 = int(input("Dime el segundo número: "))
    
    # Llamada a la función
    resultado = suma(num_1, num_2)
    
    # Mostramos el resultado
    print(f"{num_1} + {num_2} = {resultado}")
    
if __name__ == "__main__":
    main()
