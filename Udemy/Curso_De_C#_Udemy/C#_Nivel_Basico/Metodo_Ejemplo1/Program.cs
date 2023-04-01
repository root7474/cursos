// See https://aka.ms/new-console-template for more information
namespace Metodo_Ejemplo1
{
    class Program
    {
        public static void Main(string[] args)
        {
            IngresoDatos();
            Console.ReadKey();
        }

        // Mi Método
        static void IngresoDatos() {
            Console.Write("\nIngresa tu nombre: ");
            string? Nombre = Console.ReadLine();

            Console.WriteLine("Tu nombre es: " + Nombre + "\n");
        }
    }
}
