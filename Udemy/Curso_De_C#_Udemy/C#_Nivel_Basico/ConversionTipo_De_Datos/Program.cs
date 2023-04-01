using System;
// See https://aka.ms/new-console-template for more information
namespace ConversionDatos
{
    public class Program
    {
        public static void Main(string[] args)
        {
            String Nombre;
            int Edad;
            bool Casado;
            double Sueldo;

            Console.Write("Ingrese su nombre: ");
            Nombre = Console.ReadLine()!;
            
            Console.Write("Ingrese su edad: ");
            Edad = int.Parse(Console.ReadLine()!);

            Console.Write("Eres casado: ");
            Casado = bool.Parse(Console.ReadLine()!);

            Console.Write("Ingresa tu sueldo: ");
            Sueldo = double.Parse(Console.ReadLine()!);

            Console.ReadKey();
        }
    }
}
