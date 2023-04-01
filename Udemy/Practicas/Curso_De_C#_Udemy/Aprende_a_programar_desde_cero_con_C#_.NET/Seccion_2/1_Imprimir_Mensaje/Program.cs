// See https://aka.ms/new-console-template for more information
// Práctica 1
// Autor: David Rodríguez
using System;

namespace _1_Imprimir_Mensaje
{
    public class Program
    {
        public static void Main(string[] args)
        {
            string mensaje1 = string.Empty;
            string mensaje2 = string.Empty;

            Console.Write("Digita tu nombre: ");
            mensaje1 = Console.ReadLine()!;
            
            Console.WriteLine("Tu nombre es: " + mensaje2);
            Console.Read();
        }
    }
}