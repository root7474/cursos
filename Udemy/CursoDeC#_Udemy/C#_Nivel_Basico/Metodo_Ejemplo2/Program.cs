using System.Globalization;
using System.Runtime.InteropServices;
// See https://aka.ms/new-console-template for more information
namespace Metodo_Ejemplo2
{
    class Program
    {
        public static void Main(string[] args)
        {
            // Sumar(1);
            Console.Write("\nQué deseas hacer?: " +
                          "\n1.) Tabla de sumas." +
                          "\n2.) Tabla de multiplicar." + "\n" +
                          "\nOpción: ");
                          
            string? Opcion = Console.ReadLine();

            switch (Opcion)
            {
                case "1":
                    Console.Write("\n\nTabla de sumas." + 
                                  "\nIngresa un número: ");
                    int NumeroSuma = int.Parse(Console.ReadLine()!);
                    Sumar(NumeroSuma);
                    break;

                case "2":
                    Console.Write("\n\nTabla de multiplicar." + 
                                  "\nIngresa un número: ");
                    int NumeroMulti = int.Parse(Console.ReadLine()!);
                    Multiplicar(NumeroMulti);
                    break;
                
                case "":
                    Console.WriteLine("No digitaste ningúna opción!!!... ");
                    break;

                default:
                    Console.WriteLine("Operación no valida!!!... ");
                    break;
            }
            

            Console.ReadKey();
        }

        // Suma
        static void Sumar(int Numero) {
            Console.WriteLine();

            for (int i = 1; i <= 10; i++)
            {
                Console.WriteLine(Numero + " + " + i + " = " + (Numero + i));
            }

            Console.WriteLine();
        }

        static void Multiplicar(int Numero) {
            Console.WriteLine();

            for (int i = 1; i <= 10; i++)
            { 
                Console.WriteLine(Numero + " X " + i + " = " + (Numero * i));
            }

            Console.WriteLine();
        }
    }
}
