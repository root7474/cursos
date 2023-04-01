def main():
    # Función lower()
    cadena = "EjEmplo dE CaDENa de tExtos"
    print(cadena.lower())
    
    # Función upper()
    print(cadena.upper())
    
    # Función capitalize()
    print(cadena.capitalize())
    
    # Función title()
    print(cadena.title())
    
    # Función swapcase()
    print(cadena.swapcase())
    
    # Función isupper()
    cadena = "MAYUSCULAS"
    
    print(cadena)
    print(cadena.isupper())
    
    # Función islower()
    cadena = "minusculas"
    print(cadena.islower())
    
    # Función isnumeric()
    cadena = "1234"
    print(cadena.isnumeric())
    
    # Función isalnum()
    cadena = "a34"
    print(cadena.isalnum())
    
    # Función istitle()
    cadena = "Título 1"
    print(cadena.istitle())
    
    cadena = "esto no es un título"
    print(cadena.istitle())
    
if __name__ == "__main__":
    main()
