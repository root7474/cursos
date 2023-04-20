# Programa de calculadora en consola de Python
# Autor: David Rodríguez
# Importamos el menú de opciones que hemos creado y le damos un alias
import Menu_Opciones.Menu as opciones

def main():
    # Iniciamos con un try
    # Si no se ha precionado "CTRL + D" o "CTRL + C" el programa seguirá con su ejecución
    try:
        nombre = input("Bienvenido... \nDigita tu nombre: ") # Pedimos que el usuario ingrese su nombre
        opciones.menu(nombre) # Enviamos lo que halla en "nombre" a la función "menu" del módulo "Menu.py"
    except(EOFError, KeyboardInterrupt):
        print("\nHasta pronto...") # Se lanzará este mensaje si se oprime "CTRL + D" o "CTRL + C"
if __name__ == "__main__":
    main()
