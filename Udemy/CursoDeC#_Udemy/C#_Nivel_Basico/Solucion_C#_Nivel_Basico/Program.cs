// See https://aka.ms/new-console-template for more information
namespace DatosPrimitivos
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            /* int edad;
            string nombre;
            double sueldo;
            bool casado;

            Console.Write("Cuál es tu nombre: ");
            nombre = Console.ReadLine()!;
            
            Console.Write("Ingresa tu edad: ");
            edad = int.Parse(Console.ReadLine()!);

            Console.Write("Ingresa tu sueldo: ");
            sueldo = double.Parse(Console.ReadLine()!);

            Console.Write("casado?: ");
            casado = bool.Parse(Console.ReadLine()!);

            Console.WriteLine("\nTu nombre es " + nombre +
                              " y tu edad es " + edad + " años");

            Console.WriteLine("Tu sueldo es " + sueldo + " COP " +
                              "y la consulta de Casado es: " + casado); */

            string Nombre = "David";
            int Edad = 26;
            const double Sueldo = 2500000;

            dynamic Contenido = false;

            Console.WriteLine("Mi nombre es " + Nombre + ", mi edad es " + Edad +
                              " y teniendo el sueldo de " + Sueldo + ".");

            Console.WriteLine("Contenido: " + Contenido + ".");
            Console.ReadKey();
        }
    }
}
