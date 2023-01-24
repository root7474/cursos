def numeros(num1, num2, num3, num4):
    print("El primer número introducido es: " + str(num1) +
          "\nEl segundo número introducido es: " + str(num2) +
          "\nEl tercer número introducido es: " + str(num3) +
          "\nEl cuarto número introducido es: " + str(num4) + "\n")
    
    
def main():
    numeros(1, 2, 3, 4)
    numeros(num1 = 777, num2 = 70, num3 = 7, num4 = 0)
    numeros(100, num3 = 200, num4 = 1, num2 = 2)
    numeros(7, 8, 10, num4 = 9)
    
    print("Introduce cuatro números: ")
    a = eval(input("Número 1: "))
    b = eval(input("Número 2: "))
    c = eval(input("Número 3: "))
    d = eval(input("Número 4: "))
    
    numeros(a, num2 = b, num3 = c , num4 = d)
    
main()
    