// Programa que calcúla el área de un triángulo
// Autor: David Rodríguez
using System; // Importamos la librería System

namespace Area_Triangulo
{
    public class Program
    {
        public static void Main(string[] args)
        {
            // Declaramos las variables de tipo string y de tipo Double para la altura y la base del triángulo
            string? baseTrianguloString;
            string? alturaTrianguloString;

            double baseTrianguloDouble;
            double alturaTrianguloDouble;
            double areaTriangulo; // Utilizaremos esta variable para calcular el área del triangulo

            // Imprimimos por consola un mensaje junto con el dibujo de un triángulo
            Console.WriteLine("Te daré el área de un triángulo");
            Console.WriteLine(@"    /\    ");
            Console.WriteLine(@"   /  \   ");
            Console.WriteLine(@"  /    \  ");
            Console.WriteLine(@" /      \ ");
            Console.WriteLine(@"/        \");
            Console.WriteLine("----------");

            // Pedimos al usuario que ingrese la base del triángulo
            Console.Write("Digita la base del triángulo: ");
            baseTrianguloString = Console.ReadLine();

            // Convertimos la base ingresada de tipo string a tipo double
            if (double.TryParse(baseTrianguloString, out baseTrianguloDouble)) {
                Console.Write("Ahora digita la altura del triángulo: "); // Ahora pedimos al usuario que ingrese la altura del triángulo
                alturaTrianguloString = Console.ReadLine();

                // Convertimos la altura ingresada de tipo string a tipo double
                if (double.TryParse(alturaTrianguloString, out alturaTrianguloDouble)) {
                    areaTriangulo = (baseTrianguloDouble * alturaTrianguloDouble) / 2; // Hacemos el cálculo del área del triángulo con los datos ingresados
                    Console.WriteLine($"El área del triángulo es: {areaTriangulo}"); // Imprimimos por consola un mensaje junto con el área del triángulo
                } else {
                    Console.WriteLine("Error!!!... Datos incorrectos."); // Si la altura ingresada no es de tipo numérico, imprimimos un mensaje de error
                }
            } else {
                Console.WriteLine("Error!!!... Datos incorrectos."); // Si la base ingresada no es de tipo numérico, imprimimos un mensaje de error
            }

            Console.ReadKey();
        }
    }
}
