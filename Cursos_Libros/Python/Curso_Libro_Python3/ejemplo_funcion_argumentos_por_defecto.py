def calculo_multiple(a = 3, b = 2):
    mi_sum = a + b
    res = a - b
    mul = a * b
    return(mi_sum, res, mul, a / b, a ** b)

def imprimir(suma, resta, multiplicacion, division, potencia):
    print("La suma es: " + str(suma))
    print("La resta es: " + str(resta))
    print("La multiplicacion es: " + str(multiplicacion))
    print("La division es: " + str(division))
    print("La potencia es: " + str(potencia))
    print("\n")
    
def main():
    suma, resta, multiplicacion, division, potencia = calculo_multiple()
    imprimir(suma, resta, multiplicacion, division, potencia)
    
    suma, resta, multiplicacion, division, potencia = calculo_multiple(2)
    imprimir(suma, resta, multiplicacion, division, potencia)
    
    suma, resta, multiplicacion, division, potencia = calculo_multiple(2, 1)
    imprimir(suma, resta, multiplicacion, division, potencia)
    
    suma, resta, multiplicacion, division, potencia = calculo_multiple(b = 10, a = 12)
    imprimir(suma, resta, multiplicacion, division, potencia)
    
    suma, resta, multiplicacion, division, potencia = calculo_multiple(b = 10)
    imprimir(suma, resta, multiplicacion, division, potencia)
    
main()

""" def mi_funcion(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

mi_funcion(1, 2, 3, 4, 5, 10, j = 23, m = 21) """
