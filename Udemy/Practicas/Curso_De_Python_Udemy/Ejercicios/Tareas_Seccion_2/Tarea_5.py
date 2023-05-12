# Tarea 5: Calculo, indice de masa corporal
# Autor: David Rodríguez

def main():
    # Pedimos al usuario que ingrese su nombre, su estatura y su peso
    nombre = input("Ingresa tu nombre: ")
    estatura = eval(input("Ingresa tu estatura: "))
    peso = eval(input("Ingresa tu peso: "))
    imc = peso / pow(estatura, 2) # Calculamos el IMC del usuario
    
    # Mostramos los datos por pantalla más el IMC redondeado a 2 decimales
    print(f"\nNombre: {nombre}"
          f"\nEstatura: {estatura}"
          f"\nPeso: {peso}"
          f"\nIndice de Masa Corporal (IMC): {round(imc, 2)}")

if __name__ == "__main__":
    main()
