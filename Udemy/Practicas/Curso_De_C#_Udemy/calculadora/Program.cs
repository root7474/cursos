// See https://aka.ms/new-console-template for more information
namespace MyNamespace
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Console.Write("\nBienvenido...\n" +
                          "\nDigita tu nombre: ");
            string? nombre = Console.ReadLine();

            while (true)
            {
                Console.Write("\nQué deseas hacer " + nombre + "?:\n" +
                              "\n1.) Suma" +
                              "\n2.) Resta" +
                              "\n3.) Multipĺicacion" +
                              "\n4.) División" +
                              "\n5.) Resto" +
                              "\n0.) Salir" +
                              "\n\nOpción: ");
                              
                string? opcionString = Console.ReadLine();
                int opcionInt = int.Parse(opcionString!);

                switch (opcionInt)
                {
                    case 1:
                        Console.Write("\n\nHas elegído 'Suma'" +
                                        "\nDigita la cantidad de números a sumar: ");
                        string? cantidadString1 = Console.ReadLine();
                        
                        int cantidadInt1 = int.Parse(cantidadString1!);
                        Console.WriteLine();
                        
                        double? suma;
                        suma = null;

                        for (var i = 0; i < cantidadInt1; i++)
                        {
                            Console.Write("Digita el número " + (i + 1) + ": ");
                            string? numeroString1 = Console.ReadLine();
                            double numeroDouble1 = double.Parse(numeroString1!);

                            if (suma is null)
                            {
                                suma = numeroDouble1;
                            }
                            else
                            {
                                suma = suma + numeroDouble1;
                            }
                        }

                        Console.WriteLine("\nEl resultado de la suma es: " + suma + "\n");
                        break;
                    
                    case 2:
                        Console.Write("\n\nHas elegído 'Resta'" +
                                        "\nDigita la cantidad de números a restar: ");
                        string? cantidadString2 = Console.ReadLine();
                        
                        int cantidadInt2 = int.Parse(cantidadString2!);
                        Console.WriteLine();
                        
                        double? resta;
                        resta = null;

                        for (var i = 0; i < cantidadInt2; i++)
                        {
                            Console.Write("Digita el número " + (i + 1) + ": ");
                            string? numeroString2 = Console.ReadLine();
                            double numeroDouble2 = double.Parse(numeroString2!);

                            if (resta is null)
                            {
                                resta = numeroDouble2;
                            }
                            else
                            {
                                resta = resta - numeroDouble2;
                            }
                        }

                        Console.WriteLine("\nEl resultado de la resta es: " + resta + "\n");
                        break;

                    case 3:
                        Console.Write("\n\nHas elegído 'Multiplicacion'" +
                                        "\nDigita la cantidad de números a multiplicar: ");
                        string? cantidadString3 = Console.ReadLine();
                        
                        int cantidadInt3 = int.Parse(cantidadString3!);
                        Console.WriteLine();
                        
                        double? multiplicar;
                        multiplicar = null;

                        for (var i = 0; i < cantidadInt3; i++)
                        {
                            Console.Write("Digita el número " + (i + 1) + ": ");
                            string? numeroString3 = Console.ReadLine();
                            double numeroDouble3 = double.Parse(numeroString3!);

                            if (multiplicar is null)
                            {
                                multiplicar = numeroDouble3;
                            }
                            else
                            {
                                multiplicar = multiplicar * numeroDouble3;
                            }
                        }

                        Console.WriteLine("\nEl resultado de la multiplicacion es: " + multiplicar + "\n");
                        break;

                        case 4:
                            Console.Write("\n\nHas elegído 'División'" +
                                            "\nDigita la cantidad de números a dividir: ");
                        string? cantidadString4 = Console.ReadLine();
                        
                        int cantidadInt4 = int.Parse(cantidadString4!);
                        Console.WriteLine();
                        
                        double? dividir;
                        dividir = null;

                        for (var i = 0; i < cantidadInt4; i++)
                        {
                            Console.Write("Digita el número " + (i + 1) + ": ");
                            string? numeroString4 = Console.ReadLine();
                            double numeroDouble4 = double.Parse(numeroString4!);

                            if (dividir is null)
                            {
                                dividir = numeroDouble4;
                            }
                            else
                            {
                                dividir = dividir / numeroDouble4;
                            }
                        }

                        Console.WriteLine("\nEl resultado de la división es: " + dividir + "\n");
                        break;

                    case 5:
                        Console.WriteLine("\n\nHas elegído 'Resto'" +
                                            "\nSolo puedes digitar dos números: ");
                        Console.WriteLine();
                        
                        double? resto;
                        resto = null;

                        for (var i = 0; i < 2; i++)
                        {
                            Console.Write("Digita el número " + (i + 1) + ": ");
                            string? numeroString5 = Console.ReadLine();
                            double numeroDouble5 = double.Parse(numeroString5!);

                            if (resto is null)
                            {
                                resto = numeroDouble5;
                            }
                            else
                            {
                                resto = resto % numeroDouble5;
                            }
                        }

                        Console.WriteLine("\nEl resultado del resto de la división es: " + resto + "\n");
                        break;

                    case 0:
                        Console.WriteLine("\n\nHasta pronto...\n");
                        break;

                    default:
                        Console.WriteLine("\nOpción incorrecta!!!...\n");
                        break;
                }
                
                if (opcionInt == 0) break;
            }
        }
    }
}
