def esPar(numero):
    if numero % 2 == 0:
        # print("El número es par")
        return True
    else:
        # print("El número es impar")
        return False
        
numero = eval(input("Dime un número y te indicaré si es par o no: "))
resultado = esPar(numero)

if resultado:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")
