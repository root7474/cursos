def main():
    # Función lower()
    cadena = "EjEmplo dE CaDENa de tExtos"
    print(cadena.lower())
    
    # Función upper()
    print(cadena.upper())
    
    # Funciín capitalize()
    print(cadena.capitalize())
    
    # Función title()
    print(cadena.title())
    
    #Función swapcase()
    print(cadena.swapcase())
    
    # Función isuper()
    cadena = "MAYÚSCULAS"
    print(cadena)
    print(cadena.isupper())
    
    # Función islower()
    cadena = "minúsculas"
    print(cadena)
    print(cadena.islower())
    
    # Función isnumeric()
    cadena = "1234"
    print(cadena)
    print(cadena.isnumeric())
    
    # Función isalnum()
    cadena = "a34"
    print(cadena)
    print(cadena.isalnum())
    
    #Función istitle()
    cadena = "Título 1"
    print(cadena)
    print(cadena.istitle())
    
    cadena = "esto no es un título"
    print(cadena)
    print(cadena.istitle())
    
if __name__ == "__main__":
    main()
    