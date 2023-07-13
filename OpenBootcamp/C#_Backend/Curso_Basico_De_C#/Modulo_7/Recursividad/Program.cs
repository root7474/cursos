// See https://aka.ms/new-console-template for more information
using System;

namespace Recursividad
{
    public class Program
    {
        public static void Main(string[] args)
        {
            for (int i = 0; i <= 10; i++) Console.WriteLine($"{i}: {CalcularFactorial(i)}");
        }

        // Recursividad
        /* 
         *  Factorial -> !
         *  1! = 1
         *  2! = 2 x 1 = 2
         *  3! = 3 x 2 x 1 = 6
         */

        public static long CalcularFactorial(int n)
        {
            if (n.Equals(0)) return 1; // Cuando n = 0, devolvemos 1 y terminamos la recursividad
            if (n.Equals(1)) return 1; // Cuando n = 1, devolvemos 1 y terminamos la recursividad
            return n * CalcularFactorial(n - 1);
        }
    }
}
