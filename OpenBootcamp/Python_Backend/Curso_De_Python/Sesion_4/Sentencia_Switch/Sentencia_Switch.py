# If Elif Else
valor = 4
        
if valor == 1:
    print("\nValor 1\n")
elif valor == 2:
    print("\nValor 2\n")
elif valor == 3:
    print("\nValor 3\n")
elif valor == 4:
    print("\nValor 4\n")
elif valor == 5:
    print("\nValor 5\n")
else:
    print("\nValor no encontrado\n")

# Switch en Python 3.10
match valor:
    case 1:
        print("\nValor 1\n")
    case 2:
        print("\nValor 2\n")
    case 3:
        print("\nValor 3\n")
    case 4:
        print("\nValor 4\n")
    case 5:
        print("\nValor 5\n")
    case other:
        print("\nValor no encontrado\n")

# Recorrer listas
lista = [1, 2, 3, 'a', 5]

for valorActual in lista:
    print(valorActual)

print()

# Bandera de estado
lista = ["hola", "", "adios"]

for palabra in lista:
    if palabra == "mensaje":
        print("Palabra encontrada\n")
        break
else:
    print("Palabra no encontrada\n")
    
# pass
for palabra in lista:
    pass
