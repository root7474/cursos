def main():
    """ areas = ("Informática", "Administración", "Contaduría", "Jurídica", "Talento Humano")
    
    #for i in range(len(areas[0:5:-1])):
    #    print(areas[i])
    
    print(areas[0])
    print(areas[-1])
    
    # Subtuplas
    print(areas[:4]) """
    
    # Generar tuplas a partir de listas con la función tuple()
    areas = ["Informática", "Administración", "Contaduría", "Jurídica", "Talento Humano"]
    
    print(f"Lista convertida en tupla: {tuple(areas)}\n"
          f"Tipo: {type(tuple(areas))}")
    
    # Generar listas a partir de tuplas con la función list()
    areas_2 = ("Informática", "Administración", "Contaduría", "Jurídica", "Talento Humano")
    
    print(f"Tupla convertida en lista: {list(areas_2)}\n"
          f"Tipo: {type(list(areas_2))}")
    
    
if __name__ == "__main__":
    main()
