// See https://aka.ms/new-console-template for more information
namespace CondicionIf
{
    public class Program
    {
        public static void Main(string[] args)
        {
            string Nombre;
            double Sueldo;

            Console.Write("Ingresa tu nombre: ");
            Nombre = Console.ReadLine()!;

            Console.Write("Ingresa tu sueldo: ");
            Sueldo = double.Parse(Console.ReadLine()!);

            // El sueldo minimo en Colombia si es que es menor a 1200000
            // Si tu sueldo es mayor a 1200000 y menor o igual a 1200000, tu sueldo es rentable
            // Si el sueldo ingresado es mayor a 2000000, tu sueldo es generoso 
            if (Sueldo <= 1200000)
            {
                Console.WriteLine(Nombre + ", el sueldo que tienes es menor o igual al mínimo vital.");
            } else if (Sueldo > 1200000 && Sueldo <= 2000000)
            {
                Console.WriteLine(Nombre + ", tu sueldo rentable.");
            } else if (Sueldo > 2000000)
            {
                Console.WriteLine(Nombre + ", tu sueldo es generoso.");
            }

            Console.ReadKey();
        }
    }
}
