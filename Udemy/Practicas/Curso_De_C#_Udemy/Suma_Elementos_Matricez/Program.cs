// See https://aka.ms/new-console-template for more information
namespace Suma_Elementos_Matricez
{
    class Program
    {
        public static void Main(string[] args)
        {
            Matricez sum_matricez = new Matricez();
            
            sum_matricez.SumaMatricez();
            sum_matricez.MostrarResultado();
            sum_matricez.ElementosMatricez();
        }
    }

    class Matricez
    {
        string? Nombre;
        int[,]? Matriz_1;
        int[,]? Matriz_2;
        int[,]? Matriz_3;
        int Filas;
        int Columnas;
        int Numero;

        public void SumaMatricez()
        {
            // Ingresamos un nombre
            Console.Write("\nDigita tu nombre: ");
            Nombre = Console.ReadLine();

            Console.WriteLine("\nBienvenido " + Nombre);

            // Ingresamos una cantidad de filas y columnas
            Console.Write("\nDigita una cantidad de filas: ");
            Filas = int.Parse(Console.ReadLine()!);

            Console.Write("Digita una cantidad de columnas: ");
            Columnas = int.Parse(Console.ReadLine()!);
            
            // Ahora creamos los objetos para cada una de las matricez y guardamos 
            // la cantidad de filas y columnas dentro de ellos
            Matriz_1 = new int[Filas, Columnas];
            Matriz_2 = new int[Filas, Columnas];
            Matriz_3 = new int[Filas, Columnas];

            // Ingresamos por consola los elementos de la matriz 1
            Console.WriteLine("\nDigita los elementos de la matriz 1: \n");

            for (var i = 0; i < Filas; i++)
            {
                for (var a = 0; a < Columnas; a++)
                {
                    Console.Write("Posición [" + (i + 1) + ", " + (a + 1) + "]: ");
                    Numero = int.Parse(Console.ReadLine()!);
                    Matriz_1[i, a] = Numero;
                }
            }

            // Ingresamos por consola los elementos de la matriz 2
            Console.WriteLine("\n\nDigita los elementos de la matriz 2: \n");

            for (var i = 0; i < Filas; i++)
            {
                for (var a = 0; a < Columnas; a++)
                {
                    Console.Write("Posición [" + (i + 1) + ", " + (a + 1) + "]: ");
                    Numero = int.Parse(Console.ReadLine()!);
                    Matriz_2[i, a] = Numero;
                }
            }

            // Sumamos cada una de las posiciones de ambas matricez y el resultado de cada posición 
            // lo alamacenamos dentro de cada posicion de la matriz 3
            for (var i = 0; i < Filas; i++)
            {
                for (var a = 0; a < Columnas; a++)
                {
                    Matriz_3[i, a] = Matriz_1[i, a] + Matriz_2[i, a];
                }
            }
        }

        public void MostrarResultado() {
            // Mostramos los elementos de la matriz 3
            Console.WriteLine("\nResultado matriz 3: \n");

            for (var i = 0; i < Filas; i++)
            {
                for (var a = 0; a < Columnas; a++)
                {
                    Console.WriteLine("Posición [" + (i + 1) + ", " + (a + 1) + "]: " +
                                      Matriz_3![i, a]);
                }
            }

        }

        public void ElementosMatricez() {
            // Mostramos los elementos de la matriz 1 por filas
            Console.WriteLine("\nElementos de la matriz 1 por filas: \n");

            for (var b = 0; b < Filas; b++)
            {
                Console.Write("Fila " + (b + 1) + ": [");

                for (var c = 0; c < Columnas; c++)
                {    
                    Console.Write(Matriz_1![b, c]);
                    Console.Write(" ");
                }

                Console.WriteLine("]");
            }

            // Mostramos los elementos de la matriz 2 por filas
            Console.WriteLine("\nElementos de la matriz 2 por filas: \n");

            for (var b = 0; b < Filas; b++)
            {
                Console.Write("Fila " + (b + 1) + ": [");

                for (var c = 0; c < Columnas; c++)
                {    
                    Console.Write(Matriz_2![b, c]);
                    Console.Write(" ");
                }

                Console.WriteLine("]");
            }

            // Mostramos los elementos de la matriz 3 por filas
            Console.WriteLine("\nElementos de la matriz 3 por filas: \n");

            for (var b = 0; b < Filas; b++)
            {
                Console.Write("Fila " + (b + 1) + ": [");

                for (var c = 0; c < Columnas; c++)
                {    
                    Console.Write(Matriz_3![b, c]);
                    Console.Write(" ");
                }

                Console.WriteLine("]");
            }

            Console.WriteLine();
        }
    }
}
