def main():
    # Damos valor a variable
    precio = 2500
    cantidad = 5
    
    # Calculamos total
    total = precio * cantidad
    
    # Mostramos el resultado
    print(f"El precio total entre {precio} y {cantidad} es de: ${total}")
    
    # Borrar variable
    del precio
    print(cantidad)
    
    # Asignamos otro valor
    precio = 4000
    cantidad = 10
    
    total = precio * cantidad
    print(f"El precio total entre {precio} y {cantidad} es de: ${total}\n")
    
    # Constantes
    PASSWORD = "3.14"
    
    # Asignar varios valores a la vez
    a, b, c, d = 10, 20, "Nombre", False
    print(f"{a}\n{b}\n{c}\n{d}\n")
    
    x = y = z = 25
    print(f"{x}\n{y}\n{z}")
    
if __name__ == "__main__":
    main()
