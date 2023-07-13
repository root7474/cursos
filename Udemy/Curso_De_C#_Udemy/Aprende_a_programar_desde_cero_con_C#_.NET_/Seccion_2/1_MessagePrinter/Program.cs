// See https://aka.ms/new-console-template for more information
using System;

namespace _1_MessagePrinter
{
    public class Program
    {
        public static void Main(string[] args)
        {
            string message = String.Empty;
            string Message = String.Empty;

            Console.WriteLine("Proporciona un mensaje por favor: ");
            message = Console.ReadLine()!;
            Console.WriteLine("Tu cadena es: " + Message);
            Console.Read();
        }
    }
}
