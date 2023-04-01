// See https://aka.ms/new-console-template for more information
namespace OperadoresLogicos
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int a = 10, b = 2, c = 0, d = 205;
            bool Resultado = !((a < b) || (c == d));

            Console.WriteLine("Resultado de !((" + a + " < " + b + ") || " +
                              "(" + c + " == " + d + ")) es: " + Resultado);
            Console.ReadKey();
        }
    }
}
