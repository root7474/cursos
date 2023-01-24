def numeros(num1, num2, num3):
    print("El primer número es: " + str(num1) +
          "\nEl segundo número es: " + str(num2) +
          "\nEl tercer número es: " + str(num3) + "\n")

def main():
    numeros(1, 2, 3)
    numeros(num3 = 10, num2 = 15, num1 = 2)
    numeros(100, num3 = 200, num2 = 1)
    numeros(7, 8, num3 = 9)
    
    print("Introduce tres números: ")
    a = eval(input("Número 1: "))
    b = eval(input("Número 2: "))
    c = eval(input("Número 3: "))
    
    numeros(a, num3 = b, num2 = c)
    
main()
