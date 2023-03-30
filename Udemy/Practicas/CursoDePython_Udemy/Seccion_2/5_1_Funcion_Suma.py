# Dclaramos una función para suma de números
def suma(num_1, num_2):
    resultado = num_1 + num_2
    # print(f"El resultado de la suma entre {num_1} y {num_2} es: {resultado}")
    return resultado
    
def main():
    # Pedimos unos números al usuario
    num_1 = eval(input("Ingresa el número 1: "))
    num_2 = eval(input("Ingresa el número 2: "))
    
    # Enviamos los dos números a la función "suma()" para calcular su resultado
    resultado = suma(num_1, num_2)
    
    # Imprimimos el resultado de la suma de ambos números
    print(f"El resultado de la suma entre {num_1} y {num_2} es: {resultado}")
    
if __name__ == "__main__":
    main()
