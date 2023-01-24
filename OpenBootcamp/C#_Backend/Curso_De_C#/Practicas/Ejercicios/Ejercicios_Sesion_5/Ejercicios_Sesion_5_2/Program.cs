// Ejercicio 5.2
// Autor: David Rodríguez

// Variables a usar
string? nombre;
int opcion;

Console.Write("\nBienvenido..." +
              "\nDigita tu nombre: ");

nombre = Console.ReadLine();

// Menú de opciones
Console.Write("\n" + nombre + " elige un lenguaje de programación: \n" +
              "\n1.) Python" +
              "\n2.) Java" +
              "\n3.) C#" +
              "\n4.) JavaScript" +
              "\n5.) PHP" +
              "\n0.) Salir" +
              "\n\nOpción: ");

opcion = int.Parse(Console.ReadLine()!);

while (true)
{
    // Mensaje de bienvenida a cada curso
    switch (opcion)
    {
        case 1:
            Console.WriteLine("\n" + nombre + " Bienvenido al curso de Python");
            break;
        case 2:
            Console.WriteLine("\n" + nombre + " Bienvenido al curso de Java");
            break;
        case 3:
            Console.WriteLine("\nHola, mundo!!! \n" + nombre + " Bienvenido al curso de C#");
            break;
        case 4:
            Console.WriteLine("\n" + nombre + " Bienvenido al curso de JavaScript");
            break;
        case 5:
            Console.WriteLine("\n" + nombre + " Bienvenido al curso de PHP");
            break;
        case 0:
            Console.WriteLine("\n" + nombre + " Haz dado a la opción \"0.) Salir\"" +
                              "\n\nHasta pronto :) \n");
            break;
        default:
            Console.WriteLine("Error!!!... Opción Incorrecta :(");
            break;
    } if (opcion == 0) break;
    

    // Menú de opciones
    Console.Write("\n" + nombre + " elige otro lenguaje de programación: \n" +
                  "\n1.) Python" +
                  "\n2.) Java" +
                  "\n3.) C#" +
                  "\n4.) JavaScript" +
                  "\n5.) PHP" +
                  "\n0.) Salir" +
                  "\n\nOpción: ");
    
    opcion = int.Parse(Console.ReadLine()!);
}
