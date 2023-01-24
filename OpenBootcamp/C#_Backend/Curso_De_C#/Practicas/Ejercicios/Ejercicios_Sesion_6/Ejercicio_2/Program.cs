// See https://aka.ms/new-console-template for more information

// Strings nulos y vacios
/* using System.Text;

string str = "Hello";
string? nullStr = null;
string emptyStr = string.Empty;

string tempStr = str + nullStr;
Console.WriteLine(tempStr);

bool b = (nullStr == emptyStr);
Console.WriteLine(b);

string newStr = emptyStr + nullStr;
Console.WriteLine(newStr);
Console.WriteLine(emptyStr.Length);
// Console.WriteLine(nullStr.Length);
Console.WriteLine(newStr.Length);

nullStr = "a";
Console.WriteLine(nullStr.Length);

emptyStr = "";
emptyStr += nullStr;
Console.WriteLine(emptyStr); // a

// StringBuilder
StringBuilder strBuilder = new StringBuilder("Hello World in C#!!!");
Console.WriteLine(strBuilder[0]); // H
Console.WriteLine(strBuilder); // Hello World in C#!!! */

// Transformar una cadena a número si es posible
/* decimal i = 0;
string s = "1.2";
bool result = decimal.TryParse(s, out i);
Console.WriteLine($"{result}, i: {i}"); */

// Arrays

// Declaramos las filas y las columnas
int filas;
int columnas;

// Declaramos una variable número que almacenar los datos de cada
// Posición del array
int numero;

// Agregamos la longitud en filas y columnas
Console.Write("\nAgrega la longitud de las filas: ");
filas = int.Parse(Console.ReadLine()!);

Console.Write("Agrega la longitud de las columnas: ");
columnas = int.Parse(Console.ReadLine()!);

Console.WriteLine();

// Declaramos un array multidimensional
int[,] matriz = new int[filas, columnas];

// Agregamos datos por cada posición del array
for (var i = 0; i < filas; i++)
{
    for (var a = 0; a < columnas; a++)
    {
        Console.Write($"Posición {i + 1}, {a + 1}: ");
        numero = int.Parse(Console.ReadLine()!);
        matriz[i, a] = numero;
    }
}

Console.WriteLine();

// Mostramos los elementos del array por filas
for (var i = 0; i < filas; i++)
{
    Console.Write($"Fila {i + 1}: [");

    for (var a = 0; a < columnas; a++)
    {
        Console.Write($"{matriz[i, a]} ");
    }

    Console.WriteLine("]");
}

Console.WriteLine();
