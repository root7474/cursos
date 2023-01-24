// See https://aka.ms/new-console-template for more information
namespace Instruccion_ForEach
{
    class Program
    {
        public static void Main(string[] args)
        {
            string[] fruits = {"Banana", "Fig", "Cherry", "Watermelon"};

            foreach (var fruit in fruits)
            {
                Console.WriteLine(fruit);
            }
        }
    }
}
