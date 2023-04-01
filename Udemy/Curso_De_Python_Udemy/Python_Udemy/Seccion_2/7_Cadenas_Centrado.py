def main():
    texto = "Esto es un texto para el el ejemplo que vamos a realizar"
    print(f"La cadena empieza con: {texto.startswith('Esto')}")
    print(f"La cadena termina con: {texto.lower().endswith('Realizar'.lower())}")
    
    # Alinear texto
    # Función center()
    print(texto.center(80, '-'))
    
    # Función len()
    print(len(texto))
    print(texto.center(len(texto) + 7, '-'))
    
    # Función ljust()
    print(texto.ljust(80, '-'))
    
    # Función rjust()
    print(texto.rjust(80, '-'))
    
    # Función strip()
    texto = "    Esto es una cadena con espacios en blanco y algúnos caracteres raros *./6535-*-/\\j    "
    print(texto)
    print(f"Cadena sin espacios: {texto.strip()}")
    
    # Función replace()
    print(texto.replace('-', " hola "))
    
if __name__ == "__main__":
    main()
