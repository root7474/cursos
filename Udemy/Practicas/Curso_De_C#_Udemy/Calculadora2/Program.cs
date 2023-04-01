// See https://aka.ms/new-console-template for more information
using System;

namespace Calculadora
{
    class Calculadora
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("\nBienvenido...");
            Console.Write("Digita tu nombre: ");
            String nombre = Console.ReadLine()!;
            
            Console.Write("\nQué deseas hacer " + nombre + "?:\n");
            Menu();

            while (true)
            {
                try
                {
                    int opcion = int.Parse(Console.ReadLine()!);
                    
                    switch (opcion)
                    {
                        case 1:
                            try
                            {
                                double? suma = Suma();
                                Console.WriteLine("\nEl resultado de la suma es: " + suma + "\n");
                            } catch (System.Exception ex)
                            {
                                // TODO
                                Console.Write("\nError: " + ex.Message + "\n");
                            }
                            
                            break;

                        case 2:
                            try
                            {
                                double? resta = Resta();
                                Console.WriteLine("\nEl resultado de la resta es: " + resta + "\n");
                            } catch (System.Exception ex)
                            {
                                // TODO
                                Console.Write("\nError: " + ex.Message + "\n");
                            }

                            break;
                        
                        case 3:
                            try
                            {
                                double? multi = Multiplicar();
                                Console.WriteLine("\nEl resultado de la multiplicación es: " + multi + "\n");
                            } catch (System.Exception ex)
                            {
                                // TODO
                                Console.Write("\nError: " + ex.Message + "\n");
                            }

                            break;

                        case 4:
                            try
                            {
                                double? division = Dividir();
                                Console.WriteLine("\nEl resultado de la división es: " + division + "\n");
                            } catch (System.Exception ex)
                            {
                                // TODO
                                Console.Write("\nError: " + ex.Message + "\n");
                            }

                            break;

                        case 5:
                            try
                            {
                                double? resto = Resto();
                                Console.WriteLine("\nEl resultado del resto de la división es: " + resto + "\n");                                                            
                            } catch (System.Exception ex)
                            {
                                // TODO
                                Console.Write("\nError: " + ex.Message + "\n");
                            }

                            break;

                        case 0:
                            Salir();
                            break;

                        default:
                            Error();
                            break;
                    }
                    
                    if (opcion == 0) break;

                    Console.Write("\nQué más deseas hacer " + nombre + "?:\n");
                    Menu();

                } catch (System.Exception ex)
                {
                     // TODO
                    Console.Write("\nError: " + ex.Message + "\n\nOpcion: ");
                }
            }
        }

        public static void Menu() 
        {

            Console.Write("\n1.) Sumar." +
                          "\n2.) Restar." +
                          "\n3.) Multiplicar." +
                          "\n4.) Dividir." +
                          "\n5.) Resto de una división" +
                          "\n0.) Salir." +
                          "\n\nOpción: ");

        }

        public static double? Suma() 
        {
            Console.WriteLine("\n\nHaz elegido la opción '1.) Sumar.'");
            Console.Write("Digita la cantidad a sumar: ");

            int cantidad = int.Parse(Console.ReadLine()!);
            Console.WriteLine();

            double? suma = null;

            for (int i = 0; i < cantidad; i++)
            {
                Console.Write("Digita el número " + (i + 1) + ": ");
                double numero = double.Parse(Console.ReadLine()!);

                if (suma == null)
                {
                    suma = numero;
                } else
                {
                    suma = suma + numero;
                }
            }

            return suma;
        }

        public static double? Resta() 
        {
            Console.WriteLine("\n\nHaz elegido la opción '1.) Restar.'");
            Console.Write("Digita la cantidad a restar: ");

            int cantidad = int.Parse(Console.ReadLine()!);
            Console.WriteLine();

            double? resta = null;

            for (int i = 0; i < cantidad; i++)
            {
                Console.Write("Digita el número " + (i + 1) + ": ");
                double numero = double.Parse(Console.ReadLine()!);

                if (resta == null)
                {
                    resta = numero;
                } else
                {
                    resta = resta - numero;
                }
            }

            return resta;
        }

        public static double? Multiplicar() 
        {
            Console.WriteLine("\n\nHaz elegido la opción '1.) Multiplicar.'");
            Console.Write("Digita la cantidad a multiplicar: ");

            int cantidad = int.Parse(Console.ReadLine()!);
            Console.WriteLine();

            double? multi = null;

            for (int i = 0; i < cantidad; i++)
            {
                Console.Write("Digita el número " + (i + 1) + ": ");
                double numero = double.Parse(Console.ReadLine()!);

                if (multi == null)
                {
                    multi = numero;
                } else
                {
                    multi = multi * numero;
                }
            }

            return multi;
        }

        public static double? Dividir() 
        {
            Console.WriteLine("\n\nHaz elegido la opción '1.) Dividir.'");
            Console.Write("Digita la cantidad a dividir: ");

            int cantidad = int.Parse(Console.ReadLine()!);
            Console.WriteLine();

            double? division = null;

            for (int i = 0; i < cantidad; i++)
            {
                Console.Write("Digita el número " + (i + 1) + ": ");
                double numero = double.Parse(Console.ReadLine()!);

                if (division == null)
                {
                    division = numero;
                } else
                {
                    division = division / numero;
                }
            }

            return division;
        }

        public static double? Resto() 
        {
            Console.WriteLine("\n\nHaz elegido la opción '1.) Resto de una división.'");
            Console.Write("Solo debes digitar dos números: \n");
            Console.WriteLine();

            double? resto = null;

            for (int i = 0; i < 2; i++)
            {
                Console.Write("Digita el número " + (i + 1) + ": ");
                double numero = double.Parse(Console.ReadLine()!);

                if (resto == null)
                {
                    resto = numero;
                } else
                {
                    resto = resto % numero;
                }
            }

            return resto;
        }

        public static void Salir() 
        {
            Console.WriteLine("\n\nHaz elegido la opción '0.) Salir.'");
            Console.WriteLine("\nHasta luego!!!...\n");
        }

        public static void Error()
        {
            Console.WriteLine("\nError!!!... Opción Incorrecta!!!\n");
        }
    }
}
