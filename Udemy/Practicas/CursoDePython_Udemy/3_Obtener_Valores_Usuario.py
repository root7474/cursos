def main():
    # Pedimos el nombre de usuario y lo imprimimos por pantalla
    nombre = input("Dame tu nombre: ")
    print(f"Nombre: {nombre}\n")
    
    # Pedimos números al usuario y calcculamos su resultado
    num_1 = eval(input("Ingresa el número 1: "))
    num_2 = eval(input("Ingresa el número 2: "))
    resultado = num_1 + num_2
    
    print(f"\nEl resultado de la suma entre {num_1} y {num_2} es: {resultado}")
    
if __name__ == "__main__":
    main()
