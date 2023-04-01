// See https://aka.ms/new-console-template for more information
namespace Vectores
{
    class Program
    {
        public static void Main(string[] args)
        {
            string[] Nombres = {"David", "Andrés", "Luís", "Felipe", 
                                "Gloria", "Patricia", "Jesús"};
            Console.WriteLine();

            /* Console.WriteLine("Nombre: " + Nombres[0]);
            Console.WriteLine("Cantidad de elementos del vector: " + Nombres.Length); */

            for (int i = 0; i < Nombres.Length; i++)
            {
                Console.WriteLine("Nombre " + (i + 1) + ": " + Nombres[i]);
            }

            Console.WriteLine();
            Console.ReadKey();
        }
    }
}
