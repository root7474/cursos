def main():
    diccinario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    """ valor = diccinario['d']
    
    print(valor) """
    
    """ # Método get()
    valor = diccinario.get("a", "La llave no existe en el diccionario") # Por defecto retorna None
    print(valor) """
    
    # Método setdefault()
    valor = diccinario.setdefault('e', 5)
    print(valor)
    print(diccinario)

if __name__ == "__main__":
    main()
