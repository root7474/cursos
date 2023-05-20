from PIL import Image

def main():
    im = Image.open(input("Imagen a exportar: "))
    im.save(input("Nombre de la imagen nueva: "))

if __name__ == "__main__":
    main()
