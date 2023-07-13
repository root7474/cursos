// See https://aka.ms/new-console-template for more information
using System;

namespace Strcuture_Programing_Example {
    public class Program
    {
        public static void Main(string[] args)
        {
            String? nombre;
            int operation;
            Double firstData;
            Double secondData;
            bool isExit = false;

            // Pedimos que el usuario ingrese su nombre
            Console.Write("Bienvenido a tu calculadora!\n" +
                        "Digita tu nombre: ");
            nombre = Console.ReadLine();

            while (isExit == false)
            {
                // Pedimos que el usuario nos proporcione una opción
                Console.WriteLine($"\nQué opción deseas elegir {nombre}?:\n" +
                                "\n1.) Suma." +
                                "\n2.) Resta." +
                                "\n0.) Salir.");
                operation = GetIntegerDataFromUser("Proporciona la operación que deseas ejecutar: ");

                switch(operation) 
                {
                    case 1:
                        // Suma
                        Console.WriteLine($"\nHas elegido la opción \"{operation}.) Suma.\"\n");

                        // Pedimos al usuario que digite dos números para hacer una opercaión de suma
                        firstData = GetDoubleDataFromUser("Proporciona el primer operando, debe ser un número: ");
                        secondData = GetDoubleDataFromUser("Proporciona el segundo operando, debe ser un número: ");
                        Console.WriteLine($"El resultado de {firstData} + {secondData} es: {firstData + secondData}"); // Mostramos el resultado en consola
                        
                        Console.Write("\nPreciona cualquier tecla para continuar "); // Le pedimos al usuario que presione cualquier tecla para continuar
                        Console.ReadKey();
                        break;
                    
                    case 2:
                        // Resta
                        Console.WriteLine($"\nHas elegido la opción \"{operation}.) Resta.\"\n");

                        // Esta vez le pedimos al usuario otros dos números para la operación de resta
                        firstData = GetDoubleDataFromUser("Proporciona el primer operando, debe ser entero: ");
                        secondData = GetDoubleDataFromUser("Proporciona el segundo operando, debe ser entero: ");
                        Console.WriteLine($"El resultado de {firstData} - {secondData} es: {firstData - secondData}"); // Mostramos el resultado en consola
                        
                        Console.Write("\nPreciona cualquier tecla para continuar "); // Le pedimos al usuario que presione cualquier tecla para continuar
                        Console.ReadKey();
                        break;
                    
                    case 0:
                        // Salir
                        // Esto se ejecutará después de ingresar la opción "0"
                        Console.WriteLine($"\nHas elegido la opción \"{operation}.) Salir.\"" +
                                        "\nHasta pronto...");
                        Console.Write("\nPreciona cualquier tecla para salir "); // Le pedimos al usuario que presione cualquier tecla para continuar
                        Console.ReadKey();
                        
                        isExit = true; // Rompemos el ciclo enviándole un valor de "false" a la variable "isExit"
                        break;

                    default:
                        Console.WriteLine("\nLa opción seleecionada no existe"); // Esto se ejecutará si la opción ingresada por el usuario es incorrecta
                        Console.Write("\nPreciona cualquier tecla para continuar "); // Le pedimos al usuario que presione cualquier tecla para continuar
                        Console.ReadKey();
                        break;
                }

                Console.Clear(); // Borramos lo que hay en consola
                // if (operation == 0) break; // Si la opción ingresada es "0", se cerrará el programa
            }
        }

        // La siguiente función validará que solo se puedan ingresar números enteros
        private static int GetIntegerDataFromUser(string message)
        {
            string? userData;
            int data = 0;
            bool isDataValid = false;

            while (isDataValid == false)
            {
                Console.Write(message);
                userData = Console.ReadLine(); // El usuario deberá ingresar un número

                // Verificamos si el número ingresado por el usuario es un número entero
                if (!int.TryParse(userData, out data))
                {
                    Console.WriteLine("\nEl dato que proporcionaste no es valido. Vuelve a intentarlo\n"); // Si el dato ingresado no es un entero, mostraremos este mensaje
                } else
                {
                    isDataValid = true; // Si el dato ingresado es un entero, continuaremos con el programa
                }
            }

            return data; // Retornamos el valor de data
        }

        // La siguiente función validará que solo se puedan ingresar números decimales
        // Realizamos los mismos pasos que la función anterior pero esta vez con números decimales
        private static Double GetDoubleDataFromUser(String message)
        {
            string? userData;
            Double data = 0;
            bool isDataValid = false;

            while (isDataValid == false)
            {
                Console.Write(message);
                userData = Console.ReadLine();

                if (!Double.TryParse(userData, out data))
                {
                    Console.WriteLine("\nEl dato que proporcionaste no es valido. Vuelve a intentarlo\n");
                } else
                {
                    isDataValid = true;
                }
            }

            return data;
        }
    }
}
