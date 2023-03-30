def main():
    # Imprimimos un Mensaje de bienvenida
    print("Bienvenidos a mi primer programa!!!\n")
    
    # Imprimimos los tipos de datos numericos, strings y booleanos
    print(f"Tipo entero: {type(23)}")
    print(f"Tipo decimal: {type(12.32)}")
    print(f"Tipo cadena: {type('Hola Mundo!!!')}")
    print(f"Tipo booleano: {type(True)}\n")
    
    # Imprimimos mensaje "Hola amigos" concatendo cun signo "+"
    print("Hola " + "amigos")
    
    # Imprimos "Saludo" 4 veces con un salto de línea
    print("Saludo " * 4 + '\n')
    
    # Indicamos una variable de tipo cadena y la concatenamos con otro mensaje de tipo cadena
    """ variable = "Cadena en variable"
    variable = "Sumo esto a " + variable + '\n'
    print(variable) """
    
    # Hcemos lo mismo con fstrings
    """ variable = "Cadena en variable"
    variable = f"Sumo esto a {variable} \n"
    print(variable) """
    
    # Posiciones y funciones con strings en Python
    variable = "Sumo esto a Cadena en variable"
    print(variable[5])
    print(variable[-1])
    print(variable[2:5])
    print(f"{len(variable)}\n")
    print("Hola".upper())
    print(variable.lower())
    print(f"{variable.capitalize()}\n")
    
    # Reemplazar valores en strings
    cadena = "Hola, esto es un texto sin reemplazar"
    
    print(cadena) # Imprimimos la variable "cadena" sin reemplazar texto
    print(cadena.replace("sin reemplazar", "reemplazado")) # Imprimos la variable "cadena" reemplazando el texto "sin reemplazar" por el texto "reemplazado"
    
if __name__ == "__main__":
    main()
