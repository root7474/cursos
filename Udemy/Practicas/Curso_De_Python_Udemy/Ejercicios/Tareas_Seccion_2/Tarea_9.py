# Tarea 9: Función, área triangulo
# Autor: David Rodríguez

# Declaramos una función para calcular el área del triángulo
# Le pasamos como parámetros la base y la altura
def area_triangulo(base, altura):
    return (base * altura) / 2 # Retornamos el resultado

def main():
    # Pedimos al usuario que ingrese su nombre y la base y la altura del trángulo
    nombre = input("Bienvenido... Digita tu nombre: ")
    base = eval(input(f"\n{nombre} digita la base del triángulo: "))
    altura = eval(input("Ahora digita su altura: "))
    
    # Enviamos la base y la altura a la función "area_triangulo()" y guardamos el resultado
    resultado = area_triangulo(base, altura)
    
    print(f"\nEl área del triángulo es: {resultado}") # Imprimimos el resultado en consola
    
if __name__ == "__main__":
    main()
    