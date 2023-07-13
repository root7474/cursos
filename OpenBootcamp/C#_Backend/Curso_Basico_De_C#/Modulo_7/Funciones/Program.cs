using System;
using System.Linq;
// See https://aka.ms/new-console-template for more information
namespace Funciones
{
    public class Program
    {
        public static void Main(string[] args)
        {
            // Funciones con nombre
            /* int resultado = CalcularCuadrado(2); // 4
            Console.WriteLine($"Resultado: {resultado}");

            CalcularAprobado(0);
            CalcularAprobado(1);
            CalcularAprobado(2);
            CalcularAprobado(3);
            CalcularAprobado(4);
            CalcularAprobado(5);

            int i = 0;
            Console.WriteLine($"i desde main: {i}");
            
            int a = EntendiendoScope(i);
            Console.WriteLine($"a desde main: {a}"); */

            // Funciones anónimas: (input-parameters) => expression
            int[] numbers = {2, 3, 4, 5};
            var squareNumbers = numbers.Select(x => x * x);
            Console.WriteLine(string.Join(" ", squareNumbers));
        }

        // Función con retorno
        public static int CalcularCuadrado(int n)
        {
            return n * n; // int
            // Código
        }

        // Función sin retorno
        public static void CalcularAprobado(int a)
        {
            if (a == 0  || a == 1 || a == 2) 
            {
                Console.WriteLine($"Tu nota es {a}. Has suspendido");
            } else if (a == 3  || a == 4 || a == 5) 
            {
                Console.WriteLine($"Tu nota es {a}. Has aprobado");
            } else 
            {
                Console.WriteLine("Nota incorrecta");
            }
        }

        public static int EntendiendoScope(int a)
        {
            a++;
            return a;
        }
    }
}