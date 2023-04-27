import os
def main():
    carpeta = "/home/root7474/Documents/Cursos/Udemy/Curso_De_Python_Udemy/Python_Udemy/Seccion_2/11_Archivos/micarpeta"
    # print(carpeta)
    
    listado = os.listdir(carpeta)
    print(listado)
    print(type(listado))
    
    # Filtrado
    """ for archivo in listado:
        if archivo.endswith(".txt"):
            print("fichero mp3 encontrado")
            print(f"Nombre de fichero: {archivo}") """
            
    # Otra forma de foltrar
    filtrado = [archivo for archivo in listado if archivo.endswith(".zip")]
    print(type(filtrado))
    print(filtrado)
    
    # Cambio de directorio
    os.chdir(carpeta)
    # os.rename("renombrado7_renombrado1_comprimido - copia (2).zip", "CambiadoNombreComprimido.zip")
    
    # Borrar
    os.chdir(carpeta)
    
    # os.remove("CambiadoNombreComprimido.zip")
    filtrado = [archivo for archivo in listado if archivo.endswith(".zip")]
    print(filtrado)
    
    # Renombrar varios archivos al tiempo
    contador = 1
    listado = os.listdir(carpeta)
    print(f"{listado}"
          "\nFin listado inicial")
    
    """ for archivo in os.listdir():
        nombre,  extension = os.path.splitext(archivo)
        print(f"{nombre}\n{extension}")
        
        nuevo_nombre = f"renombrado{str(contador)}_{nombre}{extension}"
        contador += 1
        os.rename(archivo, nuevo_nombre)
    
    listado = os.listdir(carpeta)
    print("Listado renombrado"
          f"\n\n{listado}") """
    
    # Copiar contenido de un fichero a otro
    """ try:
        fichero = open("Hola.txt", 'r')
        nuevo_fichero = open("Nuevo_Fichero.txt", 'w')
        os.chdir(carpeta)
        
        for linea in fichero:
            nuevo_fichero.write(linea)
        
        fichero.close()
        nuevo_fichero.close()
    except FileNotFoundError:
        print("No se ha encotrado el fichero") """
        
    # Otra forma con with
    try:
        os.chdir(carpeta)
        with open("Hola.txt") as fichero:
            with open("Nuevo_Fichero_3.txt", 'w') as nuevo_nichero:
                for linea in fichero:
                    nuevo_nichero.write(linea)
    except FileNotFoundError:
        print("No se ha encotrado el fichero")
        
if __name__ == "__main__":
    main()
