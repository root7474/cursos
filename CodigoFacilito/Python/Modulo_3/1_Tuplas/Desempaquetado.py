def main():
    # * -> lista
    # _ -> Omitir valores
    
    numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    uno, _, tres, cuatro, *_, nueve, diez = numeros
    
    print(f"Posición {numeros[0]}: {uno}\n"
          f"Posición {numeros[2]}: {tres}\n"
          f"Posición {numeros[3]}: {cuatro}\n"
          f"Posición {numeros[8]}: {nueve}\n"
          f"Posición {numeros[9]}: {diez}")
    
if __name__ == "__main__":
    main()
