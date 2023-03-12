def main():
    lista_nombres = ["David", "Patricia", "Andrés", "Gloria", "Luís", "Felipe"]
    lista_trabajos = ["Informático", "Administradora", "Electrónico"]
    
    """ print(lista_nombres[0])
    print(lista_nombres[1])
    print(lista_nombres[2])
    print(lista_nombres[3])
    print(lista_nombres[4])
    print(lista_nombres[5]) """

    """ lista_nombres[3] = "Jesús"
    print(lista_nombres) """
    
    """ sub_lista_nombres = lista_nombres[1:3]
    print(sub_lista_nombres) """
    
    """ lista_trabajos.append("Contador")
    lista_trabajos.append("Gerente")
    
    print(lista_trabajos)
    
    lista_trabajos.insert(0, "Jurídico")
    lista_trabajos.insert(1, "Asesor")
    
    lista_nombres.extend(lista_trabajos)
    
    print(lista_nombres)
    print(lista_trabajos)
    
    lista_nombres.remove("Andrés")
    print(lista_nombres)
    
    del lista_nombres[0]
    print(lista_nombres)
    
    lista_nombres.clear()
    print(len(lista_nombres)) """
    
    lista_numeros = [100, 200, 50, 500.4, 90, 70, 500.5, 50, 50]
    
    """ lista_numeros.sort(reverse=True)
    print(lista_numeros) """
    
    """ lista_numeros.sort()
    print(f"Min: {lista_numeros[0]}")
    print(f"Max: {lista_numeros[-1]}")
    
    print(f"Min: {min(lista_numeros)}\n"
          f"Max: {max(lista_numeros)}")
    
    numero = eval(input("Digita un número: "))
    print(f"El número {numero} está en la lista?: ")
    
    if (numero in lista_numeros) == False:
        print("No")
    if (numero in lista_numeros) == True:
        print("Sí") """
        
    print(50 in lista_numeros)
    print(lista_numeros.index(50))

if __name__ == "__main__":
    main()
    