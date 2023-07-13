// Clase para operaciones matemáticas
namespace Calculadora3
{
    interface Calculadora
    {
        public int Menu(string nombre);
        public double? Suma(int cant);
        public double? Resta(int cant);
        public double? Multiplicacion(int cant);
        public double? Division(int cant);
        public double? Modulo(int cant);
    }

    public class  Operaciones : Calculadora
    {
        // Función que muestra un menú de opciones
        public int Menu(string nombre)
        {
            int opcion;

            Console.Write($"\nQué deseas hacer {nombre}?: \n" +
                           "\n1.) Sumar." +
                           "\n2.) Restar." +
                           "\n3.) Multiplicar" +
                           "\n4.) Dividir" +
                           "\n5.) Módulo de un división." +
                           "\n0.) Salir \n" +
                           "\nOpción: ");

            opcion = int.Parse(Console.ReadLine()!);
            return opcion;
        }

        // Función que calcula el resultado de una suma
        public double? Suma(int cant)
        {
            double? suma = null;
            double numero;

            for (var i = 0; i < cant; i++)
            {
                Console.Write($"Digita el número {i + 1}: ");
                numero = double.Parse(Console.ReadLine()!);

                if (suma is null)
                {
                    suma = numero;
                } else
                {
                    suma = suma + numero;
                }
            }

            Console.WriteLine($"\nEl resultado de la suma es: {suma}");
            return suma;
        }

        // Función que calcula el resultado de una resta
        public double? Resta(int cant)
        {
            double? resta = null;
            double numero;

            for (var i = 0; i < cant; i++)
            {
                Console.Write($"Digita el número {i + 1}: ");
                numero = double.Parse(Console.ReadLine()!);

                if (resta is null)
                {
                    resta = numero;
                } else
                {
                    resta = resta - numero;
                }
            }

            Console.WriteLine($"\nEl resultado de la resta es: {resta}");
            return resta;
        }

        // Función que calcula el resultado de una multiplicación
        public double? Multiplicacion(int cant)
        {
            double? multiplicacion = null;
            double numero;

            for (var i = 0; i < cant; i++)
            {
                Console.Write($"Digita el número {i + 1}: ");
                numero = double.Parse(Console.ReadLine()!);

                if (multiplicacion is null)
                {
                    multiplicacion = numero;
                } else
                {
                    multiplicacion = multiplicacion * numero;
                }
            }

            Console.WriteLine($"\nEl resultado de la multiplicación es: {multiplicacion}");
            return multiplicacion;
        }

        // Función que calcula el resultado de una devisión
        public double? Division(int cant)
        {
            double? division = null;
            double numero;

            
            for (var i = 0; i < cant; i++)
            {
                Console.Write($"Digita el número {i + 1}: ");
                numero = double.Parse(Console.ReadLine()!);

                if (division is null)
                {
                    division = numero;
                } else
                {
                    division = division / numero;
                }
            }

            Console.WriteLine($"\nEl resultado de la división es: {division}");
            return division;
        }

        // Función que calcula el resultado del módulo de una división
        public double? Modulo(int cant)
        {
            double? modulo = null;
            double numero;

            for (var i = 0; i < cant; i++)
            {
                Console.Write($"Digita el número {i + 1}: ");
                numero = double.Parse(Console.ReadLine()!);
                
                if (modulo is null)
                {
                    modulo = numero;
                } else
                {
                    modulo = modulo % numero;
                }
            }

            Console.WriteLine($"\nEl resultado de la división es: {modulo}");
            return modulo;
        }
    }
}
