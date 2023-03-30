# Función para calcular números pares
def esPar(numero):
    if numero % 2 == 0:
        # print(f"{numero} es par")
        return True
    else:
        # print(f"{numero} es impar")
        return False
        
def main():
    # Pedimos un número para calcular si es par y lo enviamos a la funció "esPar()"
    numero = eval(input("Número: "))
    # esPar(numero)
    resultado = esPar(numero)
    
    if resultado:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")
    
if __name__ == "__main__":
    main()
