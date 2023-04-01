// See https://aka.ms/new-console-template for more information
namespace Suma_Elementos_Vectores
{
    class Program
    {
        public static void Main(string[] args)
        {
            Vectores vectores = new Vectores();
            vectores.SumaVectores();
            vectores.MostrarSumaVectores();
        }
    }

    class Vectores
    {
        int[]? Vector_1;
        int[]? Vector_2;
        int[]? Vector_3;
        int Numero;
        int Cant;
        
        public void SumaVectores() {
            Console.Write("\nDigita una cantidad: ");
            Cant = int.Parse(Console.ReadLine()!);

            Vector_1 = new int[Cant];
            Vector_2 = new int[Cant];
            Vector_3 = new int[Cant];

            // Datos Vector_1
            Console.WriteLine("\nIngresa " + Cant + " Números " +
                              " para el primer vector: \n");

            for (var i = 0; i < Cant; i++)
            {
                Console.Write("Digita el número " + (i + 1) + ": ");
                Numero = int.Parse(Console.ReadLine()!);
                Vector_1[i] = Numero;
            }

            // Datos Vector_2
            Console.WriteLine("\n\nIngresa " + Cant + " Números " +
                              " para el segundo vector: \n");

            for (var i = 0; i < Cant; i++)
            {
                Console.Write("Digita el número " + (i + 1) + ": ");
                Numero = int.Parse(Console.ReadLine()!);
                Vector_2[i] = Numero;
            }

            // Suma entre ambos vectores
            for (var i = 0; i < Cant; i++)
            {
                Vector_3[i] = Vector_1[i] + Vector_2[i];
            }
        }

        public void MostrarSumaVectores() 
        {
            // Mostramos el resultado de la suma
            Console.WriteLine("\nResultado de la suma: \n");

            for (var i = 0; i < Vector_3!.Length; i++)
            {
                Console.WriteLine("Posición " + (i + 1) + ": " + Vector_3[i]);
            }

            Console.WriteLine();
            Console.ReadKey();
        }
    }
}
