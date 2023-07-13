// See https://aka.ms/new-console-template for more information
using System;

namespace Arrays
{
    public class Program
    {
        public static void Main(string[] args)
        {
            // Declaración arreglos 1
            Console.ForegroundColor = ConsoleColor.Red;
            int[] array1 = new int[3];
            array1[0] = 100;
            array1[1] = 200;
            Console.WriteLine($"array[0] = {array1[0]} y array[1] = {array1[1]}");
            Console.ReadKey();

            // Declaración de arreglos 2
            Console.ForegroundColor = ConsoleColor.Green;
            int[] array2 = {1, 3, 5, 7};
            String[] array3 = {"Lun", "Mar", "Mie", "Jue", "Vie"};
            Console.WriteLine($"array2[2] = {array2[2]}, array[4] = {array2[3]} y array3[1] = {array3[1]}");
            Console.ReadKey();

            // Declaración de arreglos 3
            Console.ForegroundColor = ConsoleColor.Yellow;
            double[] array4;
            array4 = new double[] {1.1, 2.2, 3.3, 4.4};
            Console.WriteLine($"array4[1] = {array4[1]} y array4[3] = {array4[3]}");
            Console.ReadKey();

            Console.ForegroundColor = ConsoleColor.Blue;

            foreach (int item in array1)
            {
                Console.WriteLine(item);
            }

            Console.ReadKey();

            int[][] arrayOfArrays = new int[2][];
            arrayOfArrays[0] = new int[] {1};
            arrayOfArrays[1] = new int[] {2, 3, 4};

            foreach (int[] item in arrayOfArrays)
            {
                foreach (int subitem in item)
                {
                    Console.WriteLine(subitem);
                }
            }

            Console.ReadKey();

            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine($"Array 1 tiene: {array1.Length} elementos");
            Console.WriteLine($"Array 2 tiene: {array2.Length} elementos");
            Console.WriteLine($"Array 3 tiene: {array3.Length} elementos");
            Console.WriteLine($"Array 4 tiene: {array4.Length} elementos");
            Console.WriteLine($"Array of arrays tiene: {arrayOfArrays.Length} elementos");
            
            Console.ReadKey();
            
            Console.ForegroundColor = ConsoleColor.White;
            Console.WriteLine($"Array 1 tiene: {array1.Rank} dimensiones");
            Console.WriteLine($"Array 2 tiene: {array2.Rank} dimensiones");
            Console.WriteLine($"Array 3 tiene: {array3.Rank} dimensiones");
            Console.WriteLine($"Array 4 tiene: {array4.Rank} dimensiones");
            Console.WriteLine($"Array of arrays tiene: {arrayOfArrays.Rank} dimensiones");
            
            Console.ReadKey();

            // Arreglos de dos dimensiones
            int[,] studentScores = new int[2, 2];
            studentScores[0, 0] = 10;
            studentScores[0, 1] = 9;
            studentScores[1, 0] = 8;
            studentScores[1, 1] = 10;
            
            Console.ForegroundColor = ConsoleColor.Gray;
            Console.WriteLine($"El estudiante 1 del grupo 1 tiene una nota de: {studentScores[0, 0]}");
            Console.WriteLine($"El estudiante 1 del grupo 2 tiene una nota de: {studentScores[1, 0]}");
            Console.WriteLine($"studentScore tiene: {studentScores.Rank} dimensiones");
            Console.ReadKey();
        }
    }
}
