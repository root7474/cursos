def main():
    nombre = "David Andrés"
    apellido = "Rodríguez"
    
    # Concatenar mediante el signo '+' 
    # nombre_completo = "Mr. " + nombre + ' ' + apellido + '.'
    
    # Concatenar mediante "%s"
    # nombre_completo = "Mr. %s %s %s" %(nombre, apellido, "Bolaños")
    
    # Concatenar mediante el método format()
    """ nombre_completo = "Mr. {nombre} {apellido_1} {apellido_2}.".format(
        nombre=nombre, 
        apellido_1=apellido, 
        apellido_2="Bolaños"
    ) """
    
    # Interpolación de strings mediante fstrings
    nombre_completo = f"Mr. {nombre} {apellido} {'Bolaños'}."
    
    print(nombre_completo)
    
if __name__ == "__main__":
    main()
