// Programa de calculadora en consola de .NET
// Autor: David Rodríguez
using System;

namespace Calculadora
{
    public class Program
    {
        public static void Main(string[] args)
        {
            String? nombre; // Declaramos una variable "nombre"

            // Damos un mensaje de bienvenida y pedimos que el usuario ingrese su nombre
            Console.Write("Bienvenido... \nDigita tu nombre: ");
            nombre = Console.ReadLine()!; // Guardamos el nombre del usuario dentron de "nombre"
            
            menu(nombre); // Enviamos el nombre a la función "menu()"
        }

        // Creamos una funció "menu()" que recibe el parámetro de "nombre"
        private static void menu(String nombre)
        {
            bool pass = false; // Declaramos una variable booleana "pass" y le ponemos el valor de false
            int opcion; // Declaramos una variable entera llamada "opcion"
            int cantidad; // Declaramos una variable entera llamada "cantidad"

            // Mientras que "pass" sea igual a false, haremos lo siguiente 
            while (pass == false)
            {
                opcion = errorInt($"\n{nombre} digita una opción:\n" +
                                    "\n1.) Suma." +
                                    "\n2.) Resta." +
                                    "\n3.) Multiplicación" +
                                    "\n4.) División." +
                                    "\n5.) Calcular el porcentaje de un número." +
                                    "\n0.) Salir." +
                                    "\n\nOpción: "); // Llamamos a la función "intError" y le pasamos como parámetro las opciones a elegir

                if (opcion == 1)
                {
                    // Si la opción digitada es igual a 1, volvemos a llamar a la función errorInt
                    // Le pasamos como parámetro un mensaje pidiendo que se ingrese una cantidad a sumar
                    cantidad = errorInt("Digita una cantidad a sumar: ");
                    Console.WriteLine(suma(cantidad)); // Enviamos la cantidad digitada a la función "suma()"
                } else if (opcion == 2)
                {
                    // Si la opción digitada es igual a 2, volvemos a llamar a la función errorInt
                    // Le pasamos como parámetro un mensaje pidiendo que se ingrese una cantidad a restar
                    cantidad = errorInt("Digita una cantidad a restar: ");
                    Console.WriteLine(resta(cantidad)); // Enviamos la cantidad digitada a la función "resta()"
                } else if (opcion == 3)
                {
                    // Si la opción digitada es igual a 3, volvemos a llamar a la función errorInt
                    // Le pasamos como parámetro un mensaje pidiendo que se ingrese una cantidad a multiplicar
                    cantidad = errorInt("Digita una cantidad a multiplicar: ");
                    Console.WriteLine(multiplicación(cantidad)); // Enviamos la cantidad digitada a la función "multiplicacion()"
                } else if (opcion == 4)
                {
                    // Si la opción digitada es igual a 4, volvemos a llamar a la función errorInt
                    // Le pasamos como parámetro un mensaje pidiendo que se ingrese una cantidad a dividir
                    cantidad = errorInt("Digita una cantidad a dividir: ");

                    try
                    {
                        Console.WriteLine(division(cantidad)); // Enviamos la cantidad digitada a la función "division()"
                    } catch (System.DivideByZeroException)
                    {
                        Console.WriteLine("\nError!!!... División entre cero"); // Esto se ejecutará si existe una división entre cero dentro de la función "division()"
                    }
                } else if (opcion == 5)
                {
                    // Si la opción digitada es igual a 5, solamente llamamos a la función "porcentaje()"
                    Console.WriteLine(porcentaje());
                } else if (opcion == 0)
                {
                    // Si la opción digitada es igual a 0, Le pasamos un valor de true a la variable "pass" para detener la ejecución del programa
                    Console.WriteLine($"\nHas elegido la opción \"{opcion}.) Salir.\"" +
                                        "\nHasta pronto...");
                    pass = true;
                } else
                {
                    Console.WriteLine("\nError!!!.. Opción incorrecta"); // Si se ha digitado una opción que no esté entre 0 y 5
                }
            }
        }

        // Creamos una función "suma()" que recibe el parámetro de "cantidad"
        private static String suma(int cantidad)
        {
            Double ? suma = null; // Declaramos una variable "suma" con un valor nulo
            Double numero; // Declaramos una variable "numero" sin ningún valor

            // Recorremos la cantidad digitada por el usuario
            for (int i = 0; i < cantidad; i++)
            {
                numero = errorDouble($"Digita el número {i + 1}: "); // En cada iteración pedimos que se ingrese un número

                if (suma == null)
                {
                    suma = numero; // En el caso de que suma sea igual a null, le pasamos el valor del número ingresado
                } else
                {
                    suma = suma + numero; // Si existe un valor en la variable "suma", hacemos una suma entre el valor de "suma" más el valor de "numero"
                }
            }
            
            return $"\nEl resultado de la suma es: {suma}"; // Retornamos el valor de la suma
        }

        // Creamos una función "resta()" que recibe el parámetro de "cantidad"
        // Para esta función, aplicamos los pasos de la función "suma()" con la diferencia de que haremos una operación de resta
        private static String resta(int cantidad)
        {
            Double ? resta = null;
            Double numero;

            for (int i = 0; i < cantidad; i++)
            {
                numero = errorDouble($"Digita el número {i + 1}: ");

                if (resta == null)
                {
                    resta = numero;
                } else
                {
                    resta = resta - numero;
                }
            }
            
            return $"\nEl resultado de la resta es: {resta}"; // Retornamos el valor de la resta
        }

        // Creamos una función "multiplicacion()" que recibe el parámetro de "cantidad"
        // Para esta función, aplicamos los pasos de la función "suma()" con la diferencia de que haremos una operación de multiplicación
        private static String multiplicación(int cantidad)
        {
            Double ? multiplicación = null;
            Double numero;

            for (int i = 0; i < cantidad; i++)
            {
                numero = errorDouble($"Digita el número {i + 1}: ");

                if (multiplicación == null)
                {
                    multiplicación = numero;
                } else
                {
                    multiplicación = multiplicación * numero;
                }
            }
            
            return $"\nEl resultado de la multiplicación es: {multiplicación}"; // Retornamos el valor de la multiplicación
        }

        // Creamos una función "division()" que recibe el parámetro de "cantidad"
        // Para esta función, aplicamos los pasos de la función "suma()" con la diferencia de que haremos una operación de división
        private static String division(int cantidad)
        {
            Double ? division = null;
            Double numero;

            for (int i = 0; i < cantidad; i++)
            {
                numero = errorDouble($"Digita el número {i + 1}: ");

                if (division == null)
                {
                    division = numero;
                } else
                {
                     // Si cualquiera de los divisores ingresados es un número cero, el programa ejecutará la excepción que creamos dentro de la función "menu()"
                    if (numero == 0) throw new DivideByZeroException();
                    division = division / numero;
                }
            }
            
            return $"\nEl resultado de la division es: {Double.Round((Double)division!, 2)}"; // Retornamos el valor de la división redondeada a 4 decimales
        }

        // Creamos una función "porcentaje()" sin ningún parámetro
        // Para esta función solamente pedimos un número y calculamos su porcentaje dividiendo entre 100
        private static String porcentaje()
        {
            Double porcentaje;
            Double numero;

            numero = errorDouble("\n\nDigita un número para calcular su porcentaje: ");
            porcentaje = numero / 100;

            return $"El porcentaje de {numero} es: {porcentaje}"; // Retornamos el porcentaje del número ingresado
        }

        // Funciones por si se ingresan letras y no números
        // Creamos una función llamada "errorInt()" y le pasamaos el parámetro "message"
        // Esta función evaluará si la opción ingresada es un entero o no
        private static int errorInt(String message)
        {
            String? userDataString;  // Declaramos una variable llamada "userDataString"
            bool isDataValid = false; // Declaramos una variable llamada "isDataValid" con el valor de false
            int userDataInt = 0; // Declaramos una variable llamada "userDataInt" con el valor de 0
            
            // Mientras que "isDataValid" sea igual a false, haremos lo siguiente
            while (isDataValid == false)
            {
                Console.Write(message); // Imprimimos el valor que le hallamos pasado al parámetro "message"
                userDataString = Console.ReadLine(); // Dentro de "userDataString" guardamos lo que ingrese el usuario por consola
                
                if (!int.TryParse(userDataString, out userDataInt)) // Hacemos una conversión de "userDataString" a enteros y la guardamos dentro de "userDataInt"
                {
                    Console.WriteLine("Error!!!... Solo debes ingresar números enteros\n"); // imprimimos un mensaje de error si el valor ingresado no es un entero
                } else
                {
                    isDataValid = true; // Si el número ingresado es un entero, se rompe el ciclo y el programa continúa con su ejecución
                }
            }

            return userDataInt; // Retornamos el valor de "userDataInt"
        }

        // Creamos una función llamada "errorDouble()" y le pasamaos el parámetro "message"
        // Repetimos los mismos pasos de la función "errorInt()" con la diferencia de que solo evaluaremos si se han ingresado decimales o no
        private static Double errorDouble(String message)
        {
            String? userDataString;
            bool isDataValid = false;
            Double userDataDouble = 0;

            while (isDataValid == false)
            {
                Console.Write(message);
                userDataString = Console.ReadLine();

                if (!Double.TryParse(userDataString, out userDataDouble))
                {
                    Console.WriteLine("Error!!!... Solo debes ingresar números");
                } else
                {
                    isDataValid = true;
                }
            }

            return userDataDouble;
        }
    }
}
