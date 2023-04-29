// See https://aka.ms/new-console-template for more information
using System;
using System.Collections;

namespace StacksAndQueues
{
    public class Program
    {
        public static void Main(string[] args)
        {
            // Pilas
            String word;
            int counter;
            Stack greetingSatck;

            // Usando PUSH y POP
            Console.ForegroundColor = ConsoleColor.Green;
            greetingSatck = new Stack();
            greetingSatck.Push("Hola");
            greetingSatck.Push("buenos");
            greetingSatck.Push("días");

            counter = greetingSatck.Count;
            Console.WriteLine($"Hay {counter} elementos en la pila");

            for (int i = 0; i < counter; i++)
            {
                word = (string)greetingSatck.Pop()!;
                Console.WriteLine($"Pop: {word}");
            }

            Console.WriteLine($"Hay {counter} elementos en la pila");
            Console.ReadKey();
            
            // Usando PEEK
            Console.ForegroundColor = ConsoleColor.Yellow;
            greetingSatck.Push("Hola");
            greetingSatck.Push("buenos");
            greetingSatck.Push("días");

            counter = greetingSatck.Count;
            Console.WriteLine($"Hay {counter} elementos en la pila");

            for (int i = 0; i < counter; i++)
            {
                word = (string)greetingSatck.Peek()!;
                Console.WriteLine($"Siguiente palabra en la pila: {word}");

                word = (string)greetingSatck.Pop()!;
                Console.WriteLine($"Pop: {word}");
            }

            Console.ReadKey();

            // Usando CONTAINS y CLEAR
            Console.ForegroundColor = ConsoleColor.White;
            greetingSatck.Push("Hola");
            greetingSatck.Push("buenos");
            greetingSatck.Push("días");

            if (greetingSatck.Contains("días")) greetingSatck.Clear();
            Console.WriteLine($"La pila greetingSatck contiene {greetingSatck.Count} elementos depués de ejecutar el método CLEAR");
            Console.ReadKey();

            // COLAS
            Console.ForegroundColor = ConsoleColor.Cyan;
            Queue greetingQueue = new Queue();
            greetingQueue.Enqueue("Hola");
            greetingQueue.Enqueue("buenos");
            greetingQueue.Enqueue("días");

            counter = greetingQueue.Count;
            Console.WriteLine($"Hay {greetingQueue.Count} elementos en la cola");

            for (int i = 0; i < counter; i++)
            {
                word = (string)greetingQueue.Peek()!;
                Console.WriteLine($"El siguiente elemento de la cola es: {word}");

                word = (string)greetingQueue.Dequeue()!;
                Console.WriteLine($"DEQUEUE: {word}");
            }

            Console.WriteLine($"Hay {greetingQueue.Count} elementos en la cola");
            Console.ReadKey();

            // Usando CONTAINS y CLEAR
            Console.ForegroundColor = ConsoleColor.Gray;
            greetingQueue.Enqueue("Hola");
            greetingQueue.Enqueue("buenos");
            greetingQueue.Enqueue("días");

            if (greetingQueue.Contains("días")) greetingQueue.Clear();
            Console.WriteLine($"La pila greetingQueue contiene {greetingQueue.Count} elementos depués de ejecutar el método CLEAR");
            Console.ReadKey();
        }
    }
}
