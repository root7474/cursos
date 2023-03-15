def esPar(numero):
    if numero % 2 == 0:
        # print(f"{numero} es par")
        return True
    else:
        # print(f"{numero} es impar")
        return False

def main():
    numero = int(input("Dime un número y te indicaré si es par o impar: "))
    resultado = esPar(numero)
    
    if resultado:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")

if __name__ == "__main__":
    main()
