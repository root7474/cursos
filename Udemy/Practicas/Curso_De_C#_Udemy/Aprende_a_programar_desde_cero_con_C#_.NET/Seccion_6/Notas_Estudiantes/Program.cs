// Programa para listar calificaciones de estudiantes consola
// Autor: David Rodríguez
using System;
using System.Collections.Generic; // Importamos a la librería "System.Collections.Generic" para poder generar nuestra lista

namespace Notas_Estudiantes
{
    public class Program
    {
        // Creamos una lista de tipo "SortedList" para generar una lista ascendente
        static SortedList<String, Double> listaOrdenada = new SortedList<String, Double>();

        public static void Main(string[] args)
        {
            String nombre; // Creamos una variable "nombre" de tipo string
            Console.Write("Bienvenido... \nDigita tu nombre: ");
            nombre = Console.ReadLine(); // Pedimos que el usuario ingrese su nombre por consola y lo guardamos dentro de nombre
            MenuOpciones(nombre); // Enviamos el nombre del usuario a la función "MenuOpciones"
        }

        // Creamos una función llamada "MenuOpciones()" con el parámetro nombre
        private static void MenuOpciones(String nombre)
        {
            // Declaramos las variables a usar para nuestro menú de opciones
            int opcion;
            int cantidad;
            bool salir = false; // Inicializamos a la variable "salir" en false

            // Mientras que "salir" sea igual a false, el programa ejecutará lo siguiente
            while (salir == false)
            {
                // Pedimos al usuario que ingrese una opción por consola
                opcion = GetIntegerDataFromUser($"\n{nombre} qué deseas hacer?:\n" +
                                                "\n1.) Ingresar calificaciones de estudiantes." +
                                                "\n2.) Revisar calificaciones de estudiantes." +
                                                "\n0.) Salir." +
                                                "\n\nOpción: ");
                
                // Evaluamos los casos de la opción que halla ingresado el usuario
                switch (opcion) {
                    case 1:
                        // Si la opcíon ingresada es igual a 1, pediremos que se ingrese una cantidad de estudiantes
                        cantidad = GetIntegerDataFromUser("Ingresa una cantidad de estudiante a calificar: ");
                        Console.WriteLine(); // Generamos un salto de línea
                        IngresarNotasEstudiantes(cantidad); // Enviamos dicha cantidad a la función "IngresarNotasEstudiantes()"
                        break; // Rompemos el switch
                    case 2:
                        Console.WriteLine(); // Generamos un salto de línea
                        ListarNotasEstudiantes(); // Si la opcíon ingresada es igual a 2, invocamos a la función "ListarNotasEstudiantes()"
                        break;
                    case 0:
                        // Si la opcíon ingresada es igual a 0, pasamos un valor de true a la variable "salir" para romper el ciclo
                        Console.WriteLine("Hasta pronto...");
                        salir = true;
                        break;
                    default:
                        Console.WriteLine("Error!!!... Opción incorrecta"); // Si la opción ingresada es incorrecta, generamos un mensaje de error
                        break;
                }
            }
        }

        // Creamos una función llamada "IngresarNotasEstudiantes()" con el parámetro cantidad
        private static void IngresarNotasEstudiantes(int cantidad)
        {
            // Creamos unas variables llamadas "calificacionEstudiantes" de tipo decimal y "nombreEstudiantes" de tipo string
            Double calificacionEstudiantes;
            String nombreEstudiantes;

            // Recorremos la cantidad ingresada por el usuario
            for (int i = 0; i < cantidad; i++)
            {
                // En cada iteración pedimos que se ingrese un nombre y una calificación para cada estudiante
                Console.Write($"Ingresa el nombre del estudiante {i + 1}: ");
                nombreEstudiantes = Console.ReadLine();
                calificacionEstudiantes = GetDoubleDataFromUser($"Ingresa la calificación de {nombreEstudiantes}: ");

                listaOrdenada.Add(nombreEstudiantes, calificacionEstudiantes); // Agregamos a nuestra lista el nombre y la calficación ingresados en cada iteración
            }
        }

        // Creamos otra función llamada "ListarNotasEstudiantes()" para listar los nombres y las calificaciones de los estudiantes 
        private static void ListarNotasEstudiantes()
        {
            foreach (KeyValuePair<String, Double> item in listaOrdenada) Console.WriteLine($"Nombre: {item.Key} | Nota: {item.Value}");
        }

        // La siguiente función validará que solo se puedan ingresar números enteros
        private static int GetIntegerDataFromUser(String message)
        {
            String userData;
            int data = 0;
            bool isDataValid = false;

            while (isDataValid == false)
            {
                Console.Write(message);
                userData = Console.ReadLine(); // El usuario deberá ingresar un número

                // Verificamos si el número ingresado por el usuario es un número entero
                if (!int.TryParse(userData, out data))
                {
                    Console.WriteLine("\nEl dato que proporcionaste no es valido. Vuelve a intentarlo"); // Si el dato ingresado no es un entero, mostraremos este mensaje
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
            String userData;
            Double data = 0;
            bool isDataValid = false;

            while (isDataValid == false)
            {
                Console.Write(message);
                userData = Console.ReadLine();

                if (!Double.TryParse(userData, out data))
                {
                    Console.WriteLine("\nEl dato que proporcionaste no es valido. Vuelve a intentarlo");
                } else
                {
                    isDataValid = true;
                }
            }

            return data;
        }
    }
}
