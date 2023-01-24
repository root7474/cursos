""" for numero in range(1, 50):
    print(numero) """
    
# Generadores
def impares():
    for numero in range(1, 50, 2):
        yield numero

generador = impares()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print("Terminando next uno a uno y pasamos al bucle for")

for numero in generador:
    print(numero)
print(generador)


# print(impares())
