using System;

namespace Arrays
{
    public class Program
    {
        public static void Main(string[] args)
        {
            /* int[] arr = new int[2]; // (1, 2)
            string[] names = new string[2]; // Indices 0, 1
            names[0] = "John Doe";
            names[1] = "John Wick";

            foreach (string item in names) 
            {
                Console.WriteLine(item);
            }

            for (int i = 0; i < names.Length; i++) {
                Console.WriteLine(names[i]);
            }

            int[] numbers = {4, 3, 8, 0, 5};
            Array.Sort(numbers); // Ordenamos el array de ints
            Console.WriteLine(numbers);

            foreach (int items in numbers) 
            {
                Console.Write($"| {items} |");
            } */

            // Más tipos de arrays
            int filaMiArray1D = 2;
            int columnasMiArray1D = 2; 
            int[, ] miArray2D = new int [filaMiArray1D, columnasMiArray1D];
            
            miArray2D[0, 0] = 1;
            miArray2D[0, 1] = 2;
            miArray2D[1, 0] = 3;
            miArray2D[1, 1] = 4;
            Console.WriteLine(miArray2D.Length);

            for (int i = 0; i < filaMiArray1D; i++)
            {
                Console.Write($"\nFila {i + 1}: ");

                for (int j = 0; j < columnasMiArray1D; j++)
                {
                    Console.Write($"| {miArray2D[i, j]} |");
                }
            }

            Console.WriteLine();
        }
    }
}
