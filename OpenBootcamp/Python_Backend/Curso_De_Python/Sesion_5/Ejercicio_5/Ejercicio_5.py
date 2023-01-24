def año_bisiesto(bisiesto):
    if ((bisiesto % 4 == 0) and ((bisiesto % 100 != 0) or (bisiesto % 400 == 0))):
        print(f"El año {bisiesto} es bisiesto")
    else:
        print(f"El año {bisiesto} no es bisiesto")

def menu_ingresar_año(nombre):
    
    while(True):
        opcion = eval(input(f"\n{nombre} ingresa una opción: \n"
                            "\n1.) Calcular año bisiesto."
                            "\n0.) Salir."
                            "\n\nOpcion: "))

        match opcion:
            case 1:
                print(f"\nHaz seleccionado la opción \"{opcion}.) Calcular año bisiesto.\"")
                bisiesto = eval(input("\nIngresa un año para saber si es bisiesto: "))
                año_bisiesto(bisiesto)
            case 0:
                print(f"\nHaz seleccionado la opción \"{opcion}.) Salir.\" \n" + 
                      "\nHasta pronto :) \n")
            case other:
                print(f"\nError!!... Opción {opcion} incorrecta :(")
            
        if opcion == 0: break
    
def main():
    nombre = input("\nBienvenido..." +
                   "\nIngresa tu nombre: ")
    
    menu_ingresar_año(nombre)
    
main()
