// See https://aka.ms/new-console-template for more information
namespace MyNamespace
{
    public class Program
    {
        public static void Main(string[] args)
        {
            string[,] Persona = new string[3, 2];
            
            Persona[0, 0] = "David Andrés";
            Persona[0, 1] = "Rodríguez Bolaños";
            
            Persona[1, 0] = "Gloria Patricia";
            Persona[1, 1] = "Bolaños Cujar";

            Persona[2, 0] = "Luís Felipe";
            Persona[2, 1] = "Rodríguez Bolaños";
            
            Console.WriteLine();

            for (int Filas = 0; Filas < 3; Filas++)
            {
                Console.Write("Nombre [" + (Filas + 1) + "] = ");

                for (int Columnas = 0; Columnas < 2; Columnas++)
                {
                    Console.Write(Persona[Filas, Columnas] + " ");
                }

                Console.WriteLine();
            }

            // Console.WriteLine("Elvalor de la primera posisión de la matríz es: " + Persona[0, 0]);
            Console.WriteLine();
            Console.ReadKey();
        }
    }
}
