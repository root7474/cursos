"""
    Ejercicio 1 Sesión 7
    Autor: David Rodríguez
"""

# Desde este script cargamos el programa
# Importamos la clase "Opciones" desde el módulo "Opciones.py"
from Operaciones_Calculadora.Opciones import Opciones

def main():
    opciones = Opciones()
    nombre = input("\nBienvenido... \nDigita tu nombre: ")
    opciones.menu(nombre)

if __name__ == '__main__':
    main()
