def calculo_tres_datos(num1, num2, num3):
    resultado = ((num1 + num2) * num3) / num3
    return(resultado)

def main():
    for i in range(0, 3):
        numero_1 = eval(input("Introduce el primer número: "))
        numero_2 = eval(input("Introduce el segundo número: "))
        numero_3 = eval(input("Introduce el tercer número: "))
        resultado = calculo_tres_datos(numero_1, numero_2, numero_3)
        
        print("El primer número introducido ha sido" + str(numero_1))
        print("El segundo número introducido ha sido: " + str(numero_2))
        print("El tercer número introducido ha sido: " + str(numero_3))
        print("El resultado de la operación entre ((" + str(numero_1) + " + " + str(numero_2) + 
              ") X " + str(numero_3) + ") / " + str(numero_3) + " es: " + str(resultado))

main()
