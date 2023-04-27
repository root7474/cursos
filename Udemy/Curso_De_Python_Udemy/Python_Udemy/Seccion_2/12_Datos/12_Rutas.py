import os
import pandas as pd

def main():
    # Directorio actual
    directorio_actual = os.getcwd()
    print(f"Estoy en: {directorio_actual}")
    
    # Directorio datos
    directorio_datos = os.path.join(directorio_actual, "datos")
    print(f"Estoy en: {directorio_datos}")
    print(f"Existe el directorio?: {os.path.exists(directorio_datos)}")
    print(f"Es una carpeta o directorio?: {os.path.isdir(directorio_actual)}")
    
    # Listar archivos de datos
    listado = [os.path.join(directorio_datos, item)
               for item in os.listdir(directorio_datos)]
    
    print(listado)
    print(os.listdir(directorio_datos))

    # Crear carpeta
    try:
        carpeta_nueva = os.mkdir(os.path.join(directorio_actual, "Nueva_Carpeta"))
        print(carpeta_nueva)
    except FileExistsError:
        print("La carpeta ya existe")
    
    # Abrimos fichero fuera de datos
    fichero_exterior = os.path.join(directorio_actual, "datos.csv")
    df_exterior = pd.read_csv(fichero_exterior)
    print("\nMostramos fichero exterior:"
          f"\n\n{df_exterior}")
    
    # Abrimos fichero dentro de datos
    fichero_interior = os.path.join(directorio_datos, "datos.csv")
    df_interior = pd.read_csv(fichero_interior)
    print("\nMostramos fichero interior:"
          f"\n\n{df_interior}")
    
    # Abrimos sin indicar ruta
    fichero = "datos.csv"
    df = pd.read_csv(fichero)
    print("\nFichero sin indicar ruta:"
          f"\n\n{df}")
    
if __name__ == "__main__":
    main()
