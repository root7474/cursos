def main():
    lista_numeros = [1, 2, 3, 4, 4.8, 5, 5.7, 7]
    tupla_numeros = (10, 20, 30, 40, 40.8, 50, 50.7, 70)
    lista_numeros_2 = [100, 200, 300, 400, 400.8, 500, 500.7, 700]
    tupla_numeros_2 = (1000, 2000, 3000, 4000, 4000.8, 5000, 5000.7, 7000)
    
    print(tuple(zip(lista_numeros, tupla_numeros, lista_numeros_2, tupla_numeros_2)))

if __name__ == "__main__":
    main()
