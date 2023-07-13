// See https://aka.ms/new-console-template for more information
using System;

namespace Metodos_2
{
    public class Program
    {
        public static void Main(string[] args)
        {
            float f = 3.1415f;
            EscribirNumeroReal(f);
            SumaDeNumerosReales(3.5, 3.1);
        }

        public static void EscribirNumeroReal(float n) {
            Console.WriteLine(n.ToString("#.####"));
        }

        public static void SumaDeNumerosReales(float a, float b)
        {
            float resultado = a + b;
            Console.WriteLine(resultado.ToString("#.#"));
        }

        public static void SumaDeNumerosReales(double a, double b)
        {
            double resultado = a + b;
            Console.WriteLine(resultado.ToString("#.#"));
        }
    }
}
