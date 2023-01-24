// Ejercicio 6.1
// Autor: David Rodríguez

int numeroFilas;
int numeroColumnas;

Console.WriteLine();

Console.Write("Número de filas: ");
numeroFilas = int.Parse(Console.ReadLine()!);

Console.Write("Número de columnas: ");
numeroColumnas = int.Parse(Console.ReadLine()!);
Console.WriteLine();

for (var i = 1; i <= numeroFilas; i++)
{
    for (var b = 1; b <= numeroColumnas; b++)
    {
        Console.Write("------------");
    }
    
    Console.WriteLine();

    for (var a = 1; a <= numeroColumnas; a++)
    {
        string mensaje1 = $"Elemento {i},{a}";
        string mensaje2 = mensaje1.Replace("Elemento", "Objeto");
        Console.Write($"|{mensaje2}|");
    }

    Console.WriteLine();
    
    for (var b = 1; b <= numeroColumnas; b++)
    {
        Console.Write("------------");
    }
    
    Console.WriteLine();
}


Console.WriteLine();
