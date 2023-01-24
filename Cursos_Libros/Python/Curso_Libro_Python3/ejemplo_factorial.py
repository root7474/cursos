def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def main():
    n = eval(input("Introduce un entero positivo para calcular su factorial: "))
    print("El factorial de " + str(n) + " es: " + str(factorial(n)))

main()
