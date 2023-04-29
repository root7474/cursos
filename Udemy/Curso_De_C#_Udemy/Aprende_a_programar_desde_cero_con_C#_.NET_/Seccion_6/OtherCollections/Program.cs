// See https://aka.ms/new-console-template for more information
using System;
using System.Collections.Generic;

namespace OtherCollections
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            HashSet<string> hashSet = new HashSet<string>();
            
            hashSet.Add("a");
            hashSet.Add("b");
            hashSet.Add("c");
            hashSet.Add("a");

            foreach (var item in hashSet) Console.WriteLine(item);
            Console.ReadKey();

            // Sorted organiza una lista de maner ascendente
            Console.ForegroundColor = ConsoleColor.Green;
            SortedSet<String> sortedSet = new SortedSet<string>();

            sortedSet.Add("d");
            sortedSet.Add("c");
            sortedSet.Add("a");
            sortedSet.Add("b");
            
            foreach (var item in sortedSet) Console.WriteLine(item);
            Console.ReadKey();

            // Dictionary es una lista de llaves / valor
            Console.ForegroundColor = ConsoleColor.Yellow;
            Dictionary<string, double> fruitCost = new Dictionary<string, double>();

            fruitCost.Add("Mango", 60);
            fruitCost.Add("Pera", 30.50);
            fruitCost.Add("Manzana", 25.75);
            
            Console.WriteLine($"El mango cuesta {fruitCost["Mango"]}");
            Console.ReadKey();

            foreach (KeyValuePair<string, double> item in fruitCost) Console.WriteLine(item);
            Console.ReadKey();

            // SortedList es un Dictionary pero ordenado
            Console.ForegroundColor = ConsoleColor.Blue;
            SortedList<string, double> fruitCostSorted = new SortedList<string, double>();

            fruitCostSorted.Add("Mango", 60);
            fruitCostSorted.Add("Pera", 30.50);
            fruitCostSorted.Add("Manzana", 25.75);
            
            foreach (var item in fruitCostSorted) Console.WriteLine(item);
            Console.ReadKey();
        }
    }
}
