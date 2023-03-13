def main():
    diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    print(len(diccionario))
    
    # Eliminar elementos con del
    del diccionario['a']
    
    # Eliminar elementos con el método pop()
    valor = diccionario.pop('b')

    # Eliminar todos los elementos del diccionario con el método clear()
    diccionario.clear()
    
    print(valor)
    print(diccionario)
    print(len(diccionario))
    
if __name__ == "__main__":
    main()
    