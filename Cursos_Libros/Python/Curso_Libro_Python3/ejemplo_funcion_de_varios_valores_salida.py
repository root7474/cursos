def calculo_multipĺe(a, b):
    suma = a + b
    resta = a - b
    mult = a * b
    
    return(suma, resta, mult, a / b, a ** b)

def main():
    print("Introduce los valores sobre los que se harán los cálculos")
    num1 = eval(input("Número 1: "))
    num2 = eval(input("Número 2: "))
    suma, resta, multiplicacion, division, potencia = calculo_multipĺe(num1, num2)
    
    print("La suma es: " + str(suma))
    print("La resta es: " + str(resta))
    print("La multiplicacion es: " + str(multiplicacion))
    print("La division es: " + str(division))
    print("La potencia es: " + str(potencia))
    
main()
    