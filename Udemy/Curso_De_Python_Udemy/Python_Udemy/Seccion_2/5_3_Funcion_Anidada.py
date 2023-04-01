def calcular(num_1, num_2, operacion = "sumar"):
    def sumar(num_1, num_2):
        return num_1 + num_2

    def restar(num_1, num_2):
        return num_1 - num_2
    
    def multiplicar(num_1, num_2):
        return num_1 * num_2
    
    def dividir(num_1, num_2):
        return num_1 / num_2
    
    if operacion == "sumar":
        print(f"{num_1} + {num_2} = {sumar(num_1, num_2)}")
    elif operacion == "restar":
        print(f"{num_1} - {num_2} = {restar(num_1, num_2)}")
    elif operacion == "multiplicar":
        print(f"{num_1} X {num_2} = {multiplicar(num_1, num_2)}")
    elif operacion == "dividir":
        print(f"{num_1} / {num_2} = {dividir(num_1, num_2)}")
    return "Resultado devuelto\n"

def main():
    print(calcular(3, 4))
    print(calcular(5, 78, "multiplicar"))
    print(calcular(45, 34, "sumar"))
    print(calcular(5, 2, "restar"))
    print(calcular(6, 2, "dividir"))
    
if __name__ == "__main__":
    main()
