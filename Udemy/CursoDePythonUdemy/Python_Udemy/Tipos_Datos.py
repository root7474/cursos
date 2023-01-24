from tkinter import Variable


print("\nBienvenidos a mi primer programa...\n")

print("Tipo entero: \n", type(23))
print("Tipo decimal: \n", type(12.32))
print("Tipo cadena: \n", type("Saludo"))
print("Tipo booleano: \n", type(False), "\n")

# Comentarios
print("Hola, " + "amigos!!!")
print("Saludo " * 4 + "\n")

""" variable = "Cadena en variable"
variable = "Sumo esto a " + variaable + "\n"
print(variable) """

variable = "Sumo esto a Cadena en variable"
print(variable[5])
print(variable[-1])
print(variable[2:5])
print(len(variable), "\n")
print("Hola".upper())
print(variable.lower())
print(variable.capitalize() + "\n")

cadena = "   Esto es una cadena con   muchos espacios   "
print(cadena.strip() + "\n")

# Reemplazar valor
cadena = "Hola esto es un texto sin reemplazar"
print(cadena)
print(cadena.replace("sin reemplazar", "reemplazado") + "\n")
