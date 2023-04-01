// See https://aka.ms/new-console-template for more information
namespace Instruccion_For
{
    public class Program
    {
        public static void Main(string[] args)
        {
            int Nentero = 0;

            Console.Write("\nIngrese un número para la tabla de multiplicar: ");
            Nentero = int.Parse(Console.ReadLine()!);
            Console.WriteLine();

            for (int i = 1; i <= 10; i++)
            {
                Console.WriteLine(Nentero + " X " + i + " = " + (Nentero * i));
            }

            Console.WriteLine();
            Console.ReadKey();
        }
    }
}
