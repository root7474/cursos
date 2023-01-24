// See https://aka.ms/new-console-template for more information
using System;

namespace Excepciones
{
    class Program
    {
        public static void Main(string[] args)
        {
            int Edad;
            
            try
            {
                Console.Write("Ingresa tu edad: ");
                Edad = int.Parse(Console.ReadLine()!);
            } catch (Exception ex)
            {
                 // TODO
                 Console.WriteLine("Error: " + ex.Message);
            }

            Console.ReadKey();
        }
    }
}
