""" def calculo_multiple(a = 7, b = 8):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    potencia = a ** b

    return(suma, resta, multiplicacion, division, potencia)

def imprimir(suma, resta, multiplicacion, division, potencia):
    print(f"\nEl resultado de la suma es: {suma}")
    print(f"El resultado de la resta es: {resta}")
    print(f"El resultado de la multiplicacion es: {multiplicacion}")
    print(f"El resultado de la division es: {division}")
    print(f"El resultado de la potencia es: {potencia}\n")
    
def main():
    suma, resta, multiplicacion, division, potencia = calculo_multiple()
    imprimir(suma, resta, multiplicacion, division, potencia)
    
    suma, resta, multiplicacion, division, potencia = calculo_multiple(3)
    imprimir(suma, resta, multiplicacion, division, potencia)
    
    suma, resta, multiplicacion, division, potencia = calculo_multiple(4, 5)
    imprimir(suma, resta, multiplicacion, division, potencia)
    
    num1 = eval(input("Número 1: "))
    num2 = eval(input("Número 2: "))
    
    suma, resta, multiplicacion, division, potencia = calculo_multiple(b = num1, a = num2)
    imprimir(suma, resta, multiplicacion, division, potencia)
    
    suma, resta, multiplicacion, division, potencia = calculo_multiple(b = 4)
    imprimir(suma, resta, multiplicacion, division, potencia)
    
main() """

def mi_funcion(a, b, *args, **kwargs):
    print(f"\n{a} \n{b} \n{args} \n{kwargs}\n")
    
mi_funcion(1, 2, 3, 4, 5, 10, j = 77, m = 21)
