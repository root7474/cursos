# Damos valor a variable
precio = 225
cantidad = 3

# Calculamos total
total = precio * cantidad

# Mostramos el resultado
print("\nEl precio total entre " + str(precio) + " y " + 
      str(cantidad) + " es: " + str(total))

# Borrar variable
del precio
print(cantidad)

# Asignamos otro valor
precio = 25
cantidad = 21

total = precio * cantidad

print("\nEl precio total entre " + str(precio) + " y " + 
      str(cantidad) + " es: " + str(total) + "\n")

# Constantes
PASSWORD = "3.14"

# Asignar varios valores a la vez
a, b, c, d = 1, 4, "Nombre", True
print(a)
print(b)
print(c)
print(d, "\n")

x = y = z = 68
print(x)
print(y)
print(z, "\n")
