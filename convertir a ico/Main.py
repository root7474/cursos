from PIL import Image

def main():
    im = Image.open(input("Digita la ruta de la imagen exportar: "))
    im.save(input("Nombre de la imagen nueva: "))

if __name__ == "__main__":
    main()
