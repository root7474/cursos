// See https://aka.ms/new-console-template for more information
namespace OperadoresRelacionales
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int Num1 = 10, Num2 = 12;
            bool Operaciones = Num1 != Num2;

            Console.WriteLine(Num1 + " es igual que " + Num2 + 
                              "?: " + Operaciones);

            Console.ReadKey();
        }
    }
}
