def main():
    mensaje = "Hola mundo!"
    
    # ljust -> Justificar a la izquierda
    # rjust -> Justificar a la derecha
    # center -> Centrar
    
    """ mensaje = mensaje.ljust(20)
    print(mensaje, '.') """
    
    """ mensaje = mensaje.rjust(20)
    print(mensaje) """
    
    mensaje = mensaje.center(20)
    print(mensaje)
    
if __name__ == "__main__":
    main()
    