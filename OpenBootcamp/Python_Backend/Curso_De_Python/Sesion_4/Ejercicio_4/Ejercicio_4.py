# Numeros del 1 al 100 en orden inverso
# Autor: David Rodríguez

# Ciclo While
numero = 100
print("\nNumeros del 1 al 100 en orden inverso con ciclo while\n")

while numero <= 100:
    print("Numero = " + str(numero))
    numero -= 1
    
    if numero == 0:
        break

# Ciclo For
numero = 100
print("\nNumeros del 1 al 100 en orden inverso con ciclo for\n")

for i in range(numero, 0, -1):
    print("Numero = " + str(i))

# Ciclo For y Reversed
numero = 100

print("\nNumeros del 1 al 100 en orden inverso con ciclo for y reversed\n")

for i in reversed(range(1, numero + 1)):
    print(f"Numero = {i}")

print()
