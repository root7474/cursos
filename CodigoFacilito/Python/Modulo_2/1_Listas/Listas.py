def main():
    # Listas
    lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java", "Rust"]
    lista_cursos_2 = ['C', "C++", "Docker"]
    
    """ print(lista_cursos[0])
    print(lista_cursos[1])
    print(lista_cursos[2])
    print(lista_cursos[3])
    print(lista_cursos[4]) """
    
    # Actualizar elementos de listas
    """ lista_cursos[4] = "Rust"
    print(lista_cursos) """
    
    # Sublistas
    # [start:end]
    # [start:] -> Obtenemos los últimos elementos de la lista
    # [:end] -> Obtenemos los primeros elementos de la lista
    # [start:end:skip]
    
    """ sub_lista = lista_cursos[0:3]
    print(sub_lista) """
    
    # Modificar listas
    """ lista_cursos.append("MongoDB")
    lista_cursos.append("C#")
    lista_cursos.append("JavaScript")
    
    lista_cursos.insert(1, "Rails")
    lista_cursos.insert(0, "PyGame")
    
    lista_cursos.extend(lista_cursos_2)
    
    print(lista_cursos)
    print(lista_cursos_2)
    
    # Eliminar elementos de una lista
    lista_cursos.remove("MongoDB")
    del lista_cursos[0]
    lista_cursos.clear()
    
    print(len(lista_cursos)) """
    
    # Métodos de listas
    lista = [8, 5, 90, 1, 5, 44, 5, 132, 600, 3, 4]
    
    """ lista.sort(reverse=True)
    print(lista) """
    
    """ lista.sort()
    
    print(f"Min: {lista[0]}")
    print(f"Max: {lista[-1]}\n")
    
    # Con funciones min() y max()
    print(f"Min: {min(lista)}\n"
          f"Max: {max(lista)}\n")
    
    # Buscar elementos dentro de una lista
    print(11 not in lista) """
    
    # Método index()
    print(5 in lista)
    print(lista.index(5)) # Solo retorna el primer índice
    
if __name__ == "__main__":
    main()
    