# Guardar datos en archivos
def main():
    # Abrimos el archivo
    escritura = open("archivo.txt", "w")
    escritura.write("Esto se escribe en el archivo" 
                    "\nY esto se escribe en la línea siguiente"
                    "\n\t\t\tY esto en otra línea tabulado")

    escritura.close()
    
    # Lectura de fichero
    lectura = open("archivo.txt", "r")
    
    # Leemos una línea
    lee_linea = lectura.readline()
    print(f"Leemos una línea \n{lee_linea}")
    lectura.close()
    
    # Leemos todo el fichero
    lectura = open("archivo.txt", "r")
    # lee_todo = lectura.readlines() # Podemos usar "readlines()", que devuelve una lista con cada línea
    lee_todo = lectura.read()
    
    print(type(lee_todo))
    print(f"Leemos todo \n{lee_todo}")
    lectura.close()

if __name__ == "__main__":
    main()
