// See https://aka.ms/new-console-template for more information
namespace Instruccion_ForEach
{
    class Program
    {
        public static void Main(string[] args)
        {
            int contador = 0;
            string[] nombres = {"David", "Paty", "Felipe"};
            Console.WriteLine();

            /* for (var i = 0; i < nombres.Length; i++)
            {
                Console.WriteLine("Nombre " + (i + 1) + ": " + nombres[i]);
            }

            Console.WriteLine(); */

            foreach (var nombre in nombres)
            {
                contador ++;
                Console.WriteLine("Nombre " + contador + ": " + nombre);
            }

            Console.WriteLine();
        }
    }
}
