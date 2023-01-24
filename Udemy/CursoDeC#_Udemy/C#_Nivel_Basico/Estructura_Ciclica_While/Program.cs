// See https://aka.ms/new-console-template for more information
namespace Estructura_Ciclica_While
{
    public class Program
    {
        public static void Main(string[] args)
        {
            int Correlativo = 0;
            Console.WriteLine("La tabla #5");

            while (Correlativo <= 12)
            {
                Console.WriteLine(" 5 x " + Correlativo + " = " + (5 * Correlativo));
                Correlativo++;
            }

            Console.ReadKey();
        }
    }
}
