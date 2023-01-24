// Autor David Rodríguez
// Ejercicio 1
/* string? nombre;
string? apellido;
int edad;
string? pais;
string? numeroTelefonico;
string? sabeProgramar;

Console.Write("\nDigita tu nombre: ");
nombre = Console.ReadLine();

Console.Write("Digita tu apellido: ");
apellido = Console.ReadLine();

Console.Write("Digita tu edad: ");
edad = int.Parse(Console.ReadLine()!);

Console.Write("De qué país eres?: ");
pais = Console.ReadLine();

Console.Write("Digita tu número telefónico: ");
numeroTelefonico = Console.ReadLine();

Console.Write("Sabes programar?: ");
sabeProgramar = Console.ReadLine()!;

Console.WriteLine("\nNombre: " + nombre +
                  "\nApellido: " + apellido +
                  "\nEdad: " + edad +
                  "\nPaís: " + pais +
                  "\nNúmero telefónico: " + numeroTelefonico +
                  "\nSabe programar?: " + sabeProgramar);

// Ejercicio 2
// Coche
int puertas;
int ruedas;
string? marca;
string? ITV_Vigente;

Console.Write("\nCoche: \n" +
              "\nNúmero de puertas: ");
puertas = int.Parse(Console.ReadLine()!);

Console.Write("Número de ruedas: ");
ruedas = int.Parse(Console.ReadLine()!);

Console.Write("Marca: ");
marca = Console.ReadLine();

Console.Write("ITV Vigente (1) Si, (0) No: ");
ITV_Vigente = Console.ReadLine();

Console.WriteLine("\nNumero de puertas: " + puertas +
                  "\nNúmero de ruedas: " + ruedas +
                  "\nMarca: " + marca +
                  "\nITV Vigente: " + ITV_Vigente);

// Mesa
float peso;
float largo;
string? material;
string? color;

Console.Write("\nMesa: \n" +
              "\nPeso: ");
peso = float.Parse(Console.ReadLine()!);

Console.Write("Largo: ");
largo = float.Parse(Console.ReadLine()!);

Console.Write("Material: ");
material = Console.ReadLine();

Console.Write("Color: ");
color = Console.ReadLine();

Console.WriteLine("\nPeso: " + peso +
                  "\nLargo: " + largo +
                  "\nMaterial: " + material +
                  "\nColor: " + color); */

// Ejercicio 3
int numero;
char letra;

Console.Write("\nDigita un número: ");
numero = int.Parse(Console.ReadLine()!);

Console.Write("Digita una letra: ");
letra = char.Parse(Console.ReadLine()!);

Console.WriteLine(numero + " es mayor o igual que 18?: " + (numero >= 18));
Console.WriteLine("'" + letra + "' es igual que 'a'?: " + (letra == 'a'));
Console.WriteLine(numero + " es mayor o igual a 18 y '" + letra + "' es igual que 'a'?: " + (numero >= 18 && letra == 'a'));
Console.WriteLine(numero + " es mayor o menor que 18?: " + (numero > 18 || numero < 18));
