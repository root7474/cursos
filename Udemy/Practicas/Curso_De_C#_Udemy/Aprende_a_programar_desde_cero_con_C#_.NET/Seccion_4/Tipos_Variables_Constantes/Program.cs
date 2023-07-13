// See https://aka.ms/new-console-template for more information
using System;

namespace Tipos_Variables_Constantes
{
    public class Program
    {
        public static void Main(string[] args)
        {
            const double PI = 3.14159265359;
            string? userData;
            double radius;
            double circleArea;

            Console.Write("Proporciona el radio de tu círculo por favor: ");
            userData = Console.ReadLine();

            if (double.TryParse(userData, out radius))
            {
                circleArea = PI * Math.Pow(radius, 2);
                Console.WriteLine($"El área del círculo es: {circleArea}");
            } else
            {
                Console.WriteLine("Los datos proporcionados son incorrectos.");
            }
        }
    }
}
