from Modules.Juguete import Juguete

def main():
    ju = Juguete()
    nombre = input("Digita el nombre del juguete: ")
    precio = eval(input("Ahora digita su precio: "))
    
    ju.setNombre(nombre)
    ju.setPrecio(precio)
    
    print()
    
    f = open("Salida.txt", "w")
    f.write(f"Nombre: {ju.getNombre()}\nPrecio: {ju.getPrecio()}")
    
    f = open("Salida.txt", "r")
    print(f.read())
    
    f.close()
    
    # print(f"Nombre: {ju.getNombre()}\nPrecio: {ju.getPrecio()}")
    
if __name__ == "__main__":
    main()
