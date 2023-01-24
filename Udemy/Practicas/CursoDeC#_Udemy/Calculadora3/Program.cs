// See https://aka.ms/new-console-template for more information
namespace Calculadora3
{
    class Program
    {
        public static void Main(string[] args)
        {
            Operaciones operaciones = new Operaciones();
            Opciones(operaciones);
        }

        public static void Opciones(Operaciones op) 
        {
            string? nombre;
            int opcion;
            int cant;

            Console.Write("\nBienvenido... \nDigita tu nombre: ");
            nombre = Console.ReadLine()!;

            while (true)
            {
                try
                {
                    opcion = op.Menu(nombre);

                    switch (opcion)
                    {
                        case 1:
                            Console.WriteLine("\nHaz elegido la opción \"1.) Sumar.\"");
                            Console.Write("\nDigita una cantidad de números a sumar: ");
                            cant = int.Parse(Console.ReadLine()!);
                            op.Suma(cant);

                            break;

                        case 2:
                            Console.WriteLine("\nHaz elegido la opción \"2.) Restar.\"");
                            Console.Write("\nDigita una cantidad de números a restar: ");
                            cant = int.Parse(Console.ReadLine()!);
                            op.Resta(cant);

                            break;

                        case 3:
                            Console.WriteLine("\nHaz elegido la opción \"3.) Multiplicar.\"");
                            Console.Write("\nDigita una cantidad de números a multiplicar: ");
                            cant = int.Parse(Console.ReadLine()!);
                            op.Multiplicacion(cant);
                            
                            break;

                        case 4:
                            Console.WriteLine("\nHaz elegido la opción \"4.) Dividir.\"");
                            Console.Write("\nDigita una cantidad de números a dividir: ");
                            cant = int.Parse(Console.ReadLine()!);
                            op.Division(cant);
                            
                            break;

                        case 5:
                            cant = 2;
                            Console.WriteLine("\nHaz elegido la opción \"5.) Módulo de un división.\"");
                            Console.WriteLine($"\nSolo debes digitar {cant} números");
                            op.Modulo(cant);
                            
                            break;
                        
                        case 0:
                            Console.WriteLine("\nHaz elegido la opcion \"0.) Salir\"... \n" +
                                              "\nHasta pronto!!!... \n");
                            break;

                        default:
                            Console.WriteLine("\nError!!!... Opción incorrecta!!!");
                            break;
                    } if (opcion == 0) break;
                } catch (System.Exception)
                {
                    // TODO
                    Console.WriteLine("Error!!!... no se permiten letras, caracteres especiales o espacios en blanco");
                }
            }
        }
    }
}
