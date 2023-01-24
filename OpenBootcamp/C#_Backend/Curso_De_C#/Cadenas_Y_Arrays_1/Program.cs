// See https://aka.ms/new-console-template for more information
/* string str1;
string? str2 = null;
string str3 = System.String.Empty;
string str4 = "";
string str5 = " ";

// Tipo y Salida
Console.WriteLine($"str5: {str5}\n" + str5.GetType());

// Array de chars y string
char[] letters = {'#', 'C', '$'};
Console.WriteLine(letters[0]);
string str6 = "#C$";
Console.WriteLine(str6[0]); */

// Literales
// Caracteres de escape -> \n \u00c6 \r \t
/* string columns = "Column 1\tColumn 2\tColumn 3";
string hr = "-------------------------------------------------------------------------";
string contenido = "Contenido 1\nContenido 1\nContenido 1\tContenido 2 Contenido 2 Contenido 2\tContenido 3 Contenido 3 Contenido 3";

Console.WriteLine(columns + $"\n{hr}");
Console.WriteLine(contenido);

// Filas
string rows = "Contenido 1 Contenido 1 Contenido 1\r\nContenido 2 Contenido 2 Contenido 2\r\nContenido 3 Contenido 3 Contenido 3\r\nRow 3";
Console.WriteLine(rows);

//Algunos caracteres de escape -> \' \" \\ \v etc

string multilinea1 = "Hola, " + 
                    "esto es un mensaje " + 
                    "en varias líneas";

Console.WriteLine(multilinea1);

string multilinea2 = @"Hola, 
                      esto es un mensaje 
                      en varias líneas 
                      sin concatenar";

Console.WriteLine(multilinea2);

string comillas = @"El se autoproclama ""programador"".";

Console.WriteLine(comillas); */

// Interpiolación
/* var persona = (nombre: "David", nacimiento: 1996, lenguaje: "Python, Java, C#, JavaScript y PHP");
Console.WriteLine($"{persona.nombre} es un hombre de {2022 - persona.nacimiento} años y le gusta programar en {persona.lenguaje}."); */

// Subcadenas
/* string miString1 = "Este es mi mensaje";

// Substring, Replace, IndexOf, Trim
string miString2 = miString1.Substring(0, 10);
Console.WriteLine(miString2);

string miString3 = miString1.Replace("mensaje", "podcast");
Console.WriteLine(miString3);

// Limpiar espacios
string miString4 = miString1.Trim();
Console.WriteLine(miString4);

// Encontrar caracter
int index = miString1.IndexOf('m');
Console.WriteLine(index); */

// Strings nulos y vacios
/* string str = "Hello";
string? nullStr = null;
string emptyStr = string.Empty;

string tempStr = str + nullStr;
Console.WriteLine(tempStr);

bool b = (emptyStr == nullStr);
Console.WriteLine(b);

string newStr = emptyStr + nullStr;
Console.WriteLine(newStr);
Console.WriteLine(emptyStr.Length);
// Console.WriteLine(nullStr.Length);
Console.WriteLine(newStr.Length);

// Añadimos valores
nullStr = "a";
Console.WriteLine(nullStr.Length);

emptyStr = "";
emptyStr += nullStr;
Console.WriteLine(emptyStr); // a

// StringBuilder
StringBuilder strBuilder = new StringBuilder("Hola mundo!!!");
Console.WriteLine(strBuilder[0]); // H
Console.WriteLine(strBuilder); // Hola mundo!!! */

// Transformar una cadena a número si es posible
/* decimal i = 0;
string s = "1.2";
bool result = decimal.TryParse(s, out i);
Console.WriteLine($"{result}, i: {i}"); */

// Arrays
/* int[] arr = new int[2]; // (1, 2)

string[] names = new string[2]; // Indices 0, 1
names[0] = "Jhon Doe";
names[1] = "Jhon Wick";

foreach (string elemento in names)
{
    Console.WriteLine(elemento);
}

for (var i = 0; i < names.Length; i++)
{
    Console.WriteLine(names[i]);
}

int[] numbers = {4, 3, 8, 0, 5};
Array.Sort(numbers); // Ordenamos el array de ints

foreach (int elemento in numbers)
{
    Console.Write($"{elemento} ");
} */

// Arrays multi dimensionales
int[,] miArray2D = new int[2, 2]; // 1 2
                                  // 3 4

miArray2D[0, 0] = 1;
miArray2D[0, 1] = 2;
miArray2D[1, 0] = 3;
miArray2D[1, 1] = 4;

for (var i = 0; i < 2; i++)
{
    for (var j = 0; j < 2; j++)
    {
        Console.Write($"{miArray2D[i, j]} ");
    }

    Console.WriteLine();
}

Console.WriteLine(miArray2D.Length); // 4
