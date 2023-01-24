// See https://aka.ms/new-console-template for more information
namespace Metodo_Ejemplo3
{
    class Program
    {
        public static void Main(string[] args)
        {
            string? Nombre;
            double Pago_x_Dia;
            int Dias;
            double Total;

            Console.Write("\nIngresa tu nombre: ");
            Nombre = Console.ReadLine();

            Console.Write("cuánto te pagan por día?: ");
            Pago_x_Dia = double.Parse(Console.ReadLine()!);

            Console.Write("Cuantos días trabajaste?: ");
            Dias = int.Parse(Console.ReadLine()!);

            Total = CalcularTotal(Pago_x_Dia, Dias);
            Console.WriteLine("\n" + Nombre + " tus ganancias obtenidas durante tu tiempo de trabajo son: $" + Total + "\n");
        
            Console.ReadKey();
        }

        // Método para obtener el total de ganancias
        static double CalcularTotal(double pago, int dia) {
            double Total = pago * dia;
            return Total;
        }
    }
}
