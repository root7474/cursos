def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    n = eval(input("\nIntroduce un entero positivo para calcular su factorial: "))
    print(f"El factorial de {n} es: {factorial(n)}\n")

main()
