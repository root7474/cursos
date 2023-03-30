lista_colores = ["Rojo", "Amarillo", "Verde", "Azul"]
mi_color = "Blanco"

for color in lista_colores:
    print(color)
    
    if color == mi_color:
        print(f"Color '{mi_color}' encontrado")
        break
else:
    print(f"No he encontrado el color '{mi_color}'")
    
rango_largo = range(1, 100)
print(rango_largo)

for numero in rango_largo:
    print(numero)
    
    if numero == 990:
        print(f"Número {numero} encontrado")
        break
else:
    print("Número no encontrado")
