def calculo_mutiple(a = 3, b = 2):
    mi_sum = a + b
    resta = a - b
    mul = a * b
    
    return(mi_sum, resta, mul, a / b, a ** b)

def imprimir(suma, resta, multiplicacion, division, potencia):
    print(f"La suma es:           {suma}")
    print(f"La resta es:          {resta}")
    print(f"La multiplicacion es: {multiplicacion}")
    print(f"La división es:       {division}")
    print(f"La potencia es:       {potencia}")
    print("\n")

def main():
    suma, resta, multiplicacion, division, potencia = calculo_mutiple()
    imprimir(suma, resta, multiplicacion, division, potencia)

    suma, resta, multiplicacion, division, potencia = calculo_mutiple(2)
    imprimir(suma, resta, multiplicacion, division, potencia)

    suma, resta, multiplicacion, division, potencia = calculo_mutiple(2, 1)
    imprimir(suma, resta, multiplicacion, division, potencia)

    suma, resta, multiplicacion, division, potencia = calculo_mutiple(b = 10, a = 12)
    imprimir(suma, resta, multiplicacion, division, potencia)

    suma, resta, multiplicacion, division, potencia = calculo_mutiple(b = 10)
    imprimir(suma, resta, multiplicacion, division, potencia)

main()
