// Ejercicios 5.1
// Autor: David Rodríguez

// Variables a utilizar
string? nombre;
int opcion;

// Precios base
int precioCamiseta = 50000;
int precioPantalon = 30000;
int precioChaqueta = 70000;
int precioMedias = 20000;
int precioZapatos = 50000;
int precioConjunto = 220000;

// Cupones
const string cuponDescuentoString1 = "E8AVC78D";
const string cuponDescuentoString2 = "EDF1R3R5";
const string cuponDescuentoString3 = "A172C78D";

string? cuponIngresar;

double cuponDescuentoDouble1 = 30;
double cuponDescuentoDouble2 = 20;
double cuponDescuentoDouble3 = 10;


// Ingreso nombre de usuario
Console.Write("\nBienvenido..." +
              "\ndigita tu nombre: ");

nombre = Console.ReadLine();

// Menú de opciones
Console.Write("\nQué deseas hacer " + nombre + "?: \n" +
              "\n1.) Comprar camiseta: $50000 COP" +
              "\n2.) Comprar pantalón: $30000 COP" +
              "\n3.) Comprar chaqueta: $70000 COP" +
              "\n4.) Comprar medias:   $20000 COP" +
              "\n5.) Comprar zapatos:  $50000 COP" +
              "\n6.) Lleva el conjunto completo con 50% de descuento" +
              "\n0.) Salir" +
              "\n\nOpción: ");

opcion = int.Parse(Console.ReadLine()!);

while (true)
{
    // Camiseta
    if (opcion == 1)
    {
        double descuento;

        Console.Write("\n1.) Comprar camiseta: $50000 COP" +
                      "\nIngresa tu cupón si tienes uno o sino presiona enter: ");
        cuponIngresar = Console.ReadLine();

        switch (cuponIngresar)
        {
            case cuponDescuentoString1:
                Console.WriteLine("\n" + nombre + "Tienes un descuento del 30%");
                descuento = Convert.ToDouble(precioCamiseta) - (Convert.ToDouble(precioCamiseta) * 
                            (cuponDescuentoDouble1 / 100));

                Console.WriteLine("\nEl precio total con descuento de " + 
                                  cuponDescuentoDouble1 + "% es de: $" + descuento + " COP");
                break;

            case cuponDescuentoString2:
                Console.WriteLine("\n" + nombre + " Tienes un descuento del 20%");
                descuento = Convert.ToDouble(precioCamiseta) - (Convert.ToDouble(precioCamiseta) * 
                            (cuponDescuentoDouble2 / 100));

                Console.WriteLine("\nEl precio total con descuento de " + 
                                  cuponDescuentoDouble2 + "% es de: $" + descuento + " COP");
                break;

            case cuponDescuentoString3:
                Console.WriteLine("\n" + nombre + " Tienes un descuento del 30%");
                descuento = Convert.ToDouble(precioCamiseta) - (Convert.ToDouble(precioCamiseta) * 
                            (cuponDescuentoDouble3 / 100));

                Console.WriteLine("\nEl precio total con descuento de " + 
                                  cuponDescuentoDouble3 + "% es de: $" + descuento + " COP");
                break;

            case "":
                Console.WriteLine("\nEl precio total es de: $" + precioCamiseta + " COP");
                break;

            default:
                Console.WriteLine("\nError!!!... Cupón no existente");
                break;
        }
    } 
    
    // Pantalón
    if (opcion == 2)
    {
        double descuento;

        Console.Write("\n2.) Comprar pantalón: $30000 COP" +
                      "\nIngresa tu cupón si tienes uno o sino presiona enter: ");
        cuponIngresar = Console.ReadLine();

        switch (cuponIngresar)
        {
            case cuponDescuentoString1:
                Console.WriteLine("\n" + nombre + "Tienes un descuento del 30%");
                descuento = Convert.ToDouble(precioPantalon) - (Convert.ToDouble(precioPantalon) * 
                            (cuponDescuentoDouble1 / 100));

                Console.WriteLine("\nEl precio total con descuento de " + 
                                  cuponDescuentoDouble1 + "% es de: $" + descuento + " COP");
                break;

            case cuponDescuentoString2:
                Console.WriteLine("\n" + nombre + " Tienes un descuento del 20%");
                descuento = Convert.ToDouble(precioPantalon) - (Convert.ToDouble(precioPantalon) * 
                            (cuponDescuentoDouble2 / 100));

                Console.WriteLine("\nEl precio total con descuento de " + 
                                  cuponDescuentoDouble2 + "% es de: $" + descuento + " COP");
                break;

            case cuponDescuentoString3:
                Console.WriteLine("\n" + nombre + " Tienes un descuento del 30%");
                descuento = Convert.ToDouble(precioPantalon) - (Convert.ToDouble(precioPantalon) * 
                            (cuponDescuentoDouble3 / 100));

                Console.WriteLine("\nEl precio total con descuento de " + 
                                  cuponDescuentoDouble3 + "% es de: $" + descuento + " COP");
                break;

            case "":
                Console.WriteLine("\nEl precio total es de: $" + precioPantalon + " COP");
                break;

            default:
                Console.WriteLine("\nError!!!... Cupón no existente");
                break;
        }
    }

    // Chaqueta
    if (opcion == 3)
    {
        double descuento;

        Console.Write("\n3.) Comprar chaqueta: $70000 COP" +
                      "\nIngresa tu cupón si tienes uno o sino presiona enter: ");
        cuponIngresar = Console.ReadLine();

        switch (cuponIngresar)
        {
            case cuponDescuentoString1:
                Console.WriteLine("\n" + nombre + "Tienes un descuento del 30%");
                descuento = Convert.ToDouble(precioChaqueta) - (Convert.ToDouble(precioChaqueta) * 
                            (cuponDescuentoDouble1 / 100));

                Console.WriteLine("\nEl precio total con descuento de " + 
                                  cuponDescuentoDouble1 + "% es de: $" + descuento + " COP");
                break;

            case cuponDescuentoString2:
                Console.WriteLine("\n" + nombre + " Tienes un descuento del 20%");
                descuento = Convert.ToDouble(precioChaqueta) - (Convert.ToDouble(precioChaqueta) * 
                            (cuponDescuentoDouble2 / 100));

                Console.WriteLine("\nEl precio total con descuento de " + 
                                  cuponDescuentoDouble2 + "% es de: $" + descuento + " COP");
                break;

            case cuponDescuentoString3:
                Console.WriteLine("\n" + nombre + " Tienes un descuento del 30%");
                descuento = Convert.ToDouble(precioChaqueta) - (Convert.ToDouble(precioChaqueta) * 
                            (cuponDescuentoDouble3 / 100));

                Console.WriteLine("\nEl precio total con descuento de " + 
                                  cuponDescuentoDouble3 + "% es de: $" + descuento + " COP");
                break;

            case "":
                Console.WriteLine("\nEl precio total es de: $" + precioChaqueta + " COP");
                break;

            default:
                Console.WriteLine("\nError!!!... Cupón no existente");
                break;
        }
    }

    // Medias
    if (opcion == 4)
    {
        double descuento;

        Console.Write("\n4.) Comprar medias: $20000 COP" +
                      "\nIngresa tu cupón si tienes uno o sino presiona enter: ");
        cuponIngresar = Console.ReadLine();

        switch (cuponIngresar)
        {
            case cuponDescuentoString1:
                Console.WriteLine("\n" + nombre + "Tienes un descuento del 30%");
                descuento = Convert.ToDouble(precioMedias) - (Convert.ToDouble(precioMedias) * 
                            (cuponDescuentoDouble1 / 100));

                Console.WriteLine("\nEl precio total con descuento de " + 
                                  cuponDescuentoDouble1 + "% es de: $" + descuento + " COP");
                break;

            case cuponDescuentoString2:
                Console.WriteLine("\n" + nombre + " Tienes un descuento del 20%");
                descuento = Convert.ToDouble(precioMedias) - (Convert.ToDouble(precioMedias) * 
                            (cuponDescuentoDouble2 / 100));

                Console.WriteLine("\nEl precio total con descuento de " + 
                                  cuponDescuentoDouble2 + "% es de: $" + descuento + " COP");
                break;

            case cuponDescuentoString3:
                Console.WriteLine("\n" + nombre + " Tienes un descuento del 30%");
                descuento = Convert.ToDouble(precioMedias) - (Convert.ToDouble(precioMedias) * 
                            (cuponDescuentoDouble3 / 100));

                Console.WriteLine("\nEl precio total con descuento de " + 
                                  cuponDescuentoDouble3 + "% es de: $" + descuento + " COP");
                break;

            case "":
                Console.WriteLine("\nEl precio total es de: $" + precioMedias + " COP");
                break;

            default:
                Console.WriteLine("\nError!!!... Cupón no existente");
                break;
        }
    }

    // Zapatos
    if (opcion == 5)
    {
        double descuento;

        Console.Write("\n5.) Comprar zapatos: $50000 COP" +
                      "\nIngresa tu cupón si tienes uno o sino presiona enter: ");
        cuponIngresar = Console.ReadLine();

        switch (cuponIngresar)
        {
            case cuponDescuentoString1:
                Console.WriteLine("\n" + nombre + "Tienes un descuento del 30%");
                descuento = Convert.ToDouble(precioZapatos) - (Convert.ToDouble(precioZapatos) * 
                            (cuponDescuentoDouble1 / 100));

                Console.WriteLine("\nEl precio total con descuento de " + 
                                  cuponDescuentoDouble1 + "% es de: $" + descuento + " COP");
                break;

            case cuponDescuentoString2:
                Console.WriteLine("\n" + nombre + " Tienes un descuento del 20%");
                descuento = Convert.ToDouble(precioZapatos) - (Convert.ToDouble(precioZapatos) * 
                            (cuponDescuentoDouble2 / 100));

                Console.WriteLine("\nEl precio total con descuento de " + 
                                  cuponDescuentoDouble2 + "% es de: $" + descuento + " COP");
                break;

            case cuponDescuentoString3:
                Console.WriteLine("\n" + nombre + " Tienes un descuento del 30%");
                descuento = Convert.ToDouble(precioZapatos) - (Convert.ToDouble(precioZapatos) * 
                            (cuponDescuentoDouble3 / 100));

                Console.WriteLine("\nEl precio total con descuento de " + 
                                  cuponDescuentoDouble3 + "% es de: $" + descuento + " COP");
                break;

            case "":
                Console.WriteLine("\nEl precio total es de: $" + precioZapatos + " COP");
                break;

            default:
                Console.WriteLine("\nError!!!... Cupón no existente");
                break;
        }
    }

    // Conjunto completo
    if (opcion == 6)
    {
        double descuento;

        Console.WriteLine("\n5.) Comprar conjunto completo por 30% de descuento");
        descuento = Convert.ToDouble(precioConjunto) - (Convert.ToDouble(precioConjunto) * 
                    (cuponDescuentoDouble1 / 100));

        Console.WriteLine("\nEl precio total con descuento de " + 
                          cuponDescuentoDouble1 + "% es de: $" + descuento + " COP");
    }

    if (opcion == 0)
    {
        Console.WriteLine("\nHasta pronto!!! \n");
        break;
    }

    // Menú de opciones
    Console.Write("\nQué mas deseas hacer " + nombre + "?: \n" +
                  "\n1.) Comprar camiseta: $50000 COP" +
                  "\n2.) Comprar pantalón: $30000 COP" +
                  "\n3.) Comprar chaqueta: $70000 COP" +
                  "\n4.) Comprar medias:   $20000 COP" +
                  "\n5.) Comprar zapatos:  $50000 COP" +
                  "\n6.) Lleva el conjunto completo con 30% de descuento" +
                  "\n0.) Salir" +
                  "\n\nOpción: ");

    opcion = int.Parse(Console.ReadLine()!);
}
