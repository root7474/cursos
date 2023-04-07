def main():
    # Funciones startswith() y endswith()
    texto = "Esto es un texto para el el ejemplo que vamos a realizar"
    print(f"La cadena empieza con \"Esto\"?: {texto.startswith('Esto')}")
    print(f"La cadena termina con \"realizar\"?: {texto.lower().endswith('Realizar'.lower())}")
    
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
    print(f"Texto con espacios: {texto}")
    print(f"Texto sin espacios: {texto.strip()}")
    
    # Función replace()
    print(texto.replace("-", " hola "))
    
if __name__ == "__main__":
    main()
    