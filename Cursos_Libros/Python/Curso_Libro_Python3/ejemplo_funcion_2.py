def calculo_dos_datos_2(num1, num2):
    res = ((num1 - num2) ** 2) - 1
    return(res)

def main():
    for i in range(0, 3):
        numero_1 = eval(input("Introduce el primer número: "))
        numero_2 = eval(input("Introduce el segundo número: "))
        resultado = calculo_dos_datos_2(numero_1, numero_2)
        
        print("El primer número introducido ha sido: " + str(numero_1))
        print("El segundo número introducido ha sido: " + str(numero_2))
        print("La diferencia entre ellos elevada al cuadrado y luego sumado 1 es: " + str(resultado))

main()
