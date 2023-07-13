// Suma de dos matricez
// Autor: David Rodríguez
using System; // Importamos la librería "System"

namespace Arrays
{
    public class Matricez
    {
        public static void Main(string[] args)
        {
            int filas; // Declaramos una variable para las filas
            int columnas; // Declaramos una variable para las columnas
            Double[, ] matriz1; // Declaramos un array bidimensional para la primera matriz
            Double[, ] matriz2; // Declaramos un array bidimensional para la segunda matriz
            Double[, ] matrizResultado; // Declaramos un array bidimensional para el resultado de las dos primeras matricez

            // Matriz 1
            // Pedimos que se ingrese el número de filas y columnas para la primera matriz
            Console.Write("Ingresa la cantidad de filas para la primera matriz: ");
            filas = int.Parse(Console.ReadLine()!);
            
            Console.Write("Ingresa la cantidad de columnas para la primera matriz: ");
            columnas = int.Parse(Console.ReadLine()!);
            
            matriz1 = new Double[filas, columnas]; // Agrgamos el número de filas y columnas a la primera matriz

            // Recorremos la cantidad de filas y columnas de la primera matriz
            for (int i = 0; i < filas; i++) {
                for (int j = 0; j < columnas; j++) {
                    Console.Write($"Ingresa el número {i + 1}, {j + 1}: "); // Pedimos que se ingrese un número en cada iteración
                    matriz1[i, j] = Double.Parse(Console.ReadLine()!); // Agregamos dicho número en cada posición
                }
            }

            // Imprimimos todos los elementos de cada posición de la primera matriz
            Console.WriteLine("\nMatriz 1:");

            // Recorremos cada una de las posiciones de la primera matriz y los imprimimos por consola
            for (int i = 0; i < filas; i++) {
                Console.Write($"\nFila {i + 1}: "); 
                for (int j = 0; j < columnas; j++) Console.Write($"| {matriz1[i, j]} |");
            }

            Console.WriteLine(); // Agregamos un salto de línea
            
            // Matriz 2
            // A continuación volvemos a repetir los pasos anteriores con la segunda matriz
            Console.Write("\nIngresa la cantidad de filas para la segunda matriz: ");
            filas = int.Parse(Console.ReadLine()!);
            
            Console.Write("Ingresa la cantidad de columnas para la segunda matriz: ");
            columnas = int.Parse(Console.ReadLine()!);
            
            matriz2 = new Double[filas, columnas];

            for (int i = 0; i < filas; i++) {
                for (int j = 0; j < columnas; j++) {
                    Console.Write($"Ingresa el número {i + 1}, {j + 1}: ");
                    matriz2[i, j] = Double.Parse(Console.ReadLine()!);
                }
            }

            Console.WriteLine("\nMatriz 2:");

            for (int i = 0; i < filas; i++) {
                Console.Write($"\nFila {i + 1}: ");
                for (int j = 0; j < columnas; j++) Console.Write($"| {matriz2[i, j]} |");
            }

            Console.WriteLine();

            // Matriz resultado
            // Hacemos lo siguiente para la suma de las dos primeras mtricez
            matrizResultado = new Double[filas, columnas]; // Agregamos el número de filas y columnas dentro de una matriz resultado
            Console.WriteLine("\nMatriz resultado:");

            // Recorremos la cantidad de filas y columnas
            for (int i = 0; i < filas; i++) {
                Console.Write($"\nFila {i + 1}: ");
                
                for (int j = 0; j < columnas; j++) {
                    // Hacemos la suma de cada elemento de las dos primeras matricez
                    matrizResultado[i, j] = matriz1[i, j] + matriz2[i, j]; // Guardamos dicha suma en cada posición de la matriz resultado
                    Console.Write($"| {matrizResultado[i, j]} |"); // Imprimimos el resultado
                }
            }

            Console.WriteLine(); // Agregamos un salto de línea
        }
    }
}
