// See https://aka.ms/new-console-template for more information
namespace Declare_And_Define_Arrays
{
    class Program
    {
        public static void Main(string[] args)
        {
            /* int[] notas = {10, 9, 10};
            string[] frutas = {"Manzana", "Banana", "Higo", "Cereza"}; */

            // Valores de acceso
            /* Console.WriteLine("1.) " + frutas[0]); // Manzana
            Console.WriteLine("2.) " + frutas[1]); // Banana
            Console.WriteLine("3.) " + frutas[2]); // Higo
            Console.WriteLine("4.) " + frutas[0]); // Cereza */

            // Modificar valores
            /* frutas[0] = "Sandía";
            frutas[1] = "Limón";

            Console.WriteLine("1.) " + frutas[0]);
            Console.WriteLine("2.) " + frutas[1]); */

            // Cantidad de elementos de un vector
            /* Console.WriteLine("Cantidad de elementos en \"frutas\": " + frutas.Length);
            Console.WriteLine("Cantidad de elemnetos en \"notas\": " + notas.Length); */

            // Recorrer vectores con ciclos
            string[] frutas = {"Manzana", "Banana", "Higo", "Cereza"};

            for (var fruta = 0; fruta < frutas.Length; fruta++)
            {
                Console.WriteLine("Fruta " + (fruta + 1) + ": " + frutas[fruta]);
            }
        }
    }
}
