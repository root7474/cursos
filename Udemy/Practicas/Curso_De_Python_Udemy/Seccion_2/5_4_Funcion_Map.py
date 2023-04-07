import functools # Importamos el módulo functools

def main():
    # Función map()
    lista = [23, 56, 7, 2, 6, 9, 18, 21, 75, 65] # Definimos una variable lista
    print(list(map(lambda valor: valor * valor, lista))) # Multiplicamos cada item de la lista por el mismo item

    # Función filter()
    print(list(filter(lambda valor: valor % 2 == 0, lista))) # Filtramos los números pares de la lista

    # Función reduce
    print(str(functools.reduce(lambda x, resultado: x + resultado, lista))) # Sumamos toso los items dde la lista

if __name__ == "__main__":
    main()
