def main():
    nombres = ("David", "Patricia", "Luís", "Andrés", "Gloria", "Felipe", "Lucio", "Josué", "Jesús")
    nombre_1, nombre_2, nombre_3, _, nombre_5, *_, nombre_10 = nombres
    
    print(f"Nombre: {nombre_1}\n"
          f"Nombre: {nombre_2}\n"
          f"Nombre: {nombre_3}\n"
          f"Nombre: {nombre_5}\n"
          # f"Nombres restantes: {nombres_restantes}\n"
          f"Nombre: {nombre_10}\n")
    
if __name__ == "__main__":
    main()
