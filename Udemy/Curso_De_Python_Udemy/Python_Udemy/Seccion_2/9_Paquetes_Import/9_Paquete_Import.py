import Paquetes.Funcion
# from Paquetes.Funcion import *

def main():
    print(Paquetes.Funcion.esPar(25))
    print(Paquetes.Funcion.esPar(64))
    # print(f"La suma es: {suma(25, 64)}")
    print(f"La suma es: {Paquetes.Funcion.suma(25, 64)}")

if __name__ == "__main__":
    main()
