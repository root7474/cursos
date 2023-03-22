def main():
    # Agregamos una lista de colores
    lista_colores = ["Rojo", "Amarillo", "Verde", "Azul"]
    mi_color = "Rojo"
    
    # Imprimimos la lis ta de colores con un for ... in
    for color in lista_colores:
        print(color)
        
        # Buscamos cualquier color con un if y si no lo encuentra, de "Color no encontrado"
        if color == mi_color:
            print(f"Color {mi_color} encontrado\n")
            break
        else:
            print(f"Color {mi_color} no encontrado")
            break
    
    # Declaramos un rango de números deseado y lo imprimimos por pantalla
    rango = range(1, 90)
    print(rango)
    
    # Recorremos el rango con un ciclo for ... in
    for numero in rango:
        print(numero)
        
        # Empezamos a buscar un número que esté dentro del rango
        if numero == 91:
            print(f"{numero} encontrado")
            break # Rompemos el ciclo si encontramos dicho número
    
    # Si no se ha encontrado el número
    else:
        print("Número no encontrado")

if __name__ == "__main__":
    main()
