def calculo_multiple(num1 = 777, num2 = 70, num3 = 7, num4 = 14):
    suma = num1 + num2 + num3 + num4
    resta = (num1 - num2) - (num3 - num4)
    multiplicacion = suma * resta
    division = multiplicacion / 2
    potencia = division ** 2
    
    return (suma, resta, multiplicacion, division, potencia)

def imprimir_resultado(suma, resta, multiplicacion, division, potencia):
    print(f"La suma es: {suma}")
    print(f"La resta es: {resta}")
    print(f"La multiplicación es: {multiplicacion}")
    print(f"La división es: {division}")
    print(f"La potencia es: {potencia}" + "\n")
    
def main():
    suma, resta, multiplicacion, division, potencia = calculo_multiple()
    imprimir_resultado(suma, resta, multiplicacion, division, potencia)
    
    suma, resta, multiplicacion, division, potencia = calculo_multiple(2)
    imprimir_resultado(suma, resta, multiplicacion, division, potencia)
    
    suma, resta, multiplicacion, division, potencia = calculo_multiple(2, 1, 3, 4)
    imprimir_resultado(suma, resta, multiplicacion, division, potencia)
    
    suma, resta, multiplicacion, division, potencia = calculo_multiple(num1 = 77, num4 = 30, num2 = 22, num3 = 20)
    imprimir_resultado(suma, resta, multiplicacion, division, potencia)
    
    suma, resta, multiplicacion, division, potencia = calculo_multiple(num4 = 10)
    imprimir_resultado(suma, resta, multiplicacion, division, potencia)
    
main()
    