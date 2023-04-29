// See https://aka.ms/new-console-template for more information
using System;
using System.Collections.Generic;

namespace Notas_Estudiantes
{
    public class Program
    {
        public static void Main(string[] args)
        {
            int cantidad;

            Console.Write("Digita una cantidad: ");
            cantidad = int.Parse(Console.ReadLine()!);
            notas(cantidad);
        }

        private static void notas(int cantidad) {
            Double notaEstudiantes;
            String nombreEstudiante;
            SortedList<String, Double> listaOrdenada = new SortedList<String, Double>();

            for (int i = 0; i < cantidad; i++) {
                Console.Write($"Ingresa el nombre del estudiante {i + 1}: ");
                nombreEstudiante = Console.ReadLine()!;

                Console.Write($"Ingresa la nota de {nombreEstudiante}: ");
                notaEstudiantes = Double.Parse(Console.ReadLine()!);
                listaOrdenada.Add(nombreEstudiante, notaEstudiantes);
            }

            foreach (KeyValuePair<String, Double> item in listaOrdenada) Console.WriteLine($"Nombre: {item.Key} Nota: {item.Value}");
        }
    }
}
