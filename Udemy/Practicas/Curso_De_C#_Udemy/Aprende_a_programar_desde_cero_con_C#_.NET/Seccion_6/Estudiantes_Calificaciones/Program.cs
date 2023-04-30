// Programa para listar calificaciones de estudiantes por consola
// Autor: David Rodríguez
using System;
using System.Collections.Generic; // Importamos a la librería "System.Collections.Generic" para poder generar nuestra lista

namespace StudentScores
{
    class Program
    {
        static void Main(string[] args)
        {
            int score; // Declaramos una variable "score" para guardar la calificación de cada estudiante
            String[] studentNames = new String[3]; // Declaramos un arreglo con llamado "studentNames"
            SortedList<String, int> sortedStudentScores = new SortedList<String, int>(); // Declaramos una lista ordenada para guardar la calificación y el nombre de los estudiantes

            // Recorremos el array para inicializarlo con los nombres que ingrese el usuario por consola
            for (var i = 0; i < studentNames.Length; i++)
            {
                Console.Write($"Ingresa el nombre del estudiante {i + 1}: ");
                studentNames[i] = Console.ReadLine()!;
            }

            Console.WriteLine(); // Agregamos un salto de línea

            // Recorremos cada item del array
            foreach (var item in studentNames)
            {
                score = 0; // Inicializamos a "score" en 0

                // Si "score" es igual a 0, haremos lo siguiente
                while (score == 0)
                {
                    // Pedimos al usuario que ingrese una calificación por consola y la guardamos en "score"
                    Console.Write($"Proporciona la calificación de {item}: ");
                    GetInteger(Console.ReadLine()!, out score);
                }

                // Agregamos el nombre del estudiante y su calificación a "sortedStudentScores"
                sortedStudentScores.Add(item, score);
            }

            Console.WriteLine(); // Agregamos otro salto de línea

            // Barremos a la lista "sortedStudentScores" y la pintamos de color verde en pantalla
            Console.ForegroundColor = ConsoleColor.Green;
            foreach (KeyValuePair<String, int> item in sortedStudentScores) Console.WriteLine($"Nombre: {item.Key} | Calificación: {item.Value}");

            Console.ReadKey();
        }

        // Creamos una función llamada "GetInteger" Con los parámetros "data" y "score"
        // Con esta función evaluaremos si la calificación ingresada es un entero o no
        private static void GetInteger(string data, out int score)
        {
            if (!int.TryParse(data, out score))
            {
                Console.WriteLine("El dato debe ser entero"); // Si la calificación ingresada no es un entero, se imprimirá un mensaje de error
            }
        }
    }
}