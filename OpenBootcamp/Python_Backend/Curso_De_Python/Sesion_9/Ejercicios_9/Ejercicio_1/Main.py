def main():
    elementos = input("Escribe países separados por comas: ")
    lista_paises = elementos.split(", ")
    paises = ", ".join(sorted(list(set(lista_paises))))
    
    print(f"Paises ingresados por orden alfabetico: {paises}")

if __name__ == "__main__":
    main()
