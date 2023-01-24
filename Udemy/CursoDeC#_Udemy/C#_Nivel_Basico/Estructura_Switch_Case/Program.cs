// See https://aka.ms/new-console-template for more information
namespace SwitchCase
{
    class Program
    {
        public static void Main(string[] args)
        {
            int Dia;
            
            Console.Write("Ingrese el día en número: ");
            Dia = int.Parse(Console.ReadLine()!);

            switch (Dia)
            {
                case 1:
                    Console.WriteLine("Es lunes.");
                    break;

                case 2:
                Console.WriteLine("Es martes.");
                    break;

                case 3:
                    Console.WriteLine("Es miércoles");
                    break;

                case 4:
                    Console.WriteLine("Es jueves");
                    break;

                case 5:
                    Console.WriteLine("Es viernes");
                    break;

                case 6:
                    Console.WriteLine("Es sábado");
                    break;

                case 7:
                    Console.WriteLine("Es domingo");
                    break;

                default:
                    Console.WriteLine("El día ingresado no es valido");
                    break;
            }

            Console.ReadKey();
        }
    }
}
