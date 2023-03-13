def main():
    # Método split()
    """ lenguajes = "Python Ruby Java Rust C++ C"
    listado_lenguajes = lenguajes.split() # Divide caracteres por espacios
    
    print(listado_lenguajes) """
    
    #Método join()
    lenguajes = ["Python", "Ruby", "Java", "Rust"]
    string_lenguajes = ' '.join(lenguajes)
    string_lenguajes_2 = string_lenguajes.split()
    
    print(string_lenguajes)
    print(type(string_lenguajes))
    
    print(string_lenguajes_2)
    print(type(string_lenguajes_2))
    
if __name__ == "__main__":
    main()
