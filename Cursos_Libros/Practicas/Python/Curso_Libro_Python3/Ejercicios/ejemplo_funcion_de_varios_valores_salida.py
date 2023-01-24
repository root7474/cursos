def calculo_multiple(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    potencia = a ** b

    return(suma, resta, multiplicacion, division, potencia)

def main():
    print("\nIntroduce los valores sobre los que se harán los cálculos\n")

    num1 = eval(input("Número 1: "))
    num2 = eval(input("Número 2: "))
    suma, resta, multiplicacion, division, potencia = calculo_multiple(num1, num2)

    print(f"\nEl resultado de la suma entre {num1} + {num2} es: {suma}")
    print(f"El resultado de la resta entre {num1} - {num2} es: {resta}")
    print(f"El resultado de la multiplicación entre {num1} x {num2} es: {multiplicacion}")
    print(f"El resultado de la división entre {num1} / {num2} es: {division}")
    print(f"El resultado de la potencia de {num1} ^ {num2} es: {potencia}\n")

main()
