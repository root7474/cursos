def suma(num1, num2):
    resultado = num1 + num2
    return resultado

num1 = eval(input("Dime el primer número: "))
num2 = eval(input("Dime el segundo número: "))

# Llamada a la función
resultado = suma(num1, num2)

# Mostramos el resultado
# print("La suma entre " + str(num1) + " + " + str(num2) + " es: " + str(resultado))
print(f"La suma entre {num1} + {num2} es: {resultado}")
