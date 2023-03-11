def main():
    """ cursos = ("Python", "Flask", "Django", "Rails", "MongoDB")
    
    print(cursos[0])
    print(cursos[-1])
    
    # Subtuplas
    print(cursos[:3]) """
    
    # Generar tuplas a partir de listas con la función tuple()
    cursos = ["Python", "Flask", "Django"]
    
    print(tuple(cursos))
    print(type(tuple(cursos)))
    
    # Generar listas a partir de tuplas con la función list()
    niveles = ("Básico", "Intermedio", "Avanzado")
    
    print(list(niveles))
    print(type(list(niveles)))
    
if __name__ == "__main__":
    main()
    