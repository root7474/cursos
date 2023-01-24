// See https://aka.ms/new-console-template for more information
namespace Estructura_Ciclica_Do_While
{
    public class Program
    {
        public static void Main(string[] args)
        {
            int Numero = 0;

            do
            {
                Console.WriteLine("El valor de la variable Número es: " + Numero);
                Numero++;
            } while (Numero <= 10);

            Console.ReadKey();
        }
    }
}
