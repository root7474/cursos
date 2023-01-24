// Ejercicios sesió 4
// Autor: David Rodríguez

// Ejercicio 1 - While
// Declaramos variables para nombre y menú de opciones
string? nombre;
int opcion;

// Pedimos al usuario  su nombre
Console.Write("\nBienvenido" +
              "\nDigita tu nombre: ");
nombre = Console.ReadLine();

// Imprimimos un menú de opciones y pedimos al usuario que eliga una opción
Console.Write($"\n\nQué deseas hacer {nombre}?: \n" +
              "\n1.) Calcular la tabla de multiplicar de un número." +
              "\n2.) Saber si un número es positivo o negativo y su contador." +
              "\n3.) Dibujar rectángulos." +
              "\n0.) Salir." +
              "\n\nOpción: ");

opcion = int.Parse(Console.ReadLine()!);

// Ciclo para repetir las opciones hasta oprimir 0
while(true)
{
    switch (opcion)
    {
        // Ejercicio 1 - While
        case 1:
            // Variables para realizar la operación de multiplicación
            int multiplicacion;
            int contadorWhile = 1;
            int numero_ejercicio_1;

            Console.WriteLine("\nHaz elegido la opción \"Calcular la tabla de multiplicar de un número.\"");
            
            // El usuario deberá ingresar un número por consola
            Console.Write($"\n{nombre} digita un número para saber su tabla de multiplicar: ");
            numero_ejercicio_1 = int.Parse(Console.ReadLine()!);

            Console.WriteLine($"\nTabla del {numero_ejercicio_1}\n");

            // Aquí se imprime por consola la tabla de multiplicar del número ingresado
            while (contadorWhile <= 10)
            {
                multiplicacion = numero_ejercicio_1 * contadorWhile;
                Console.WriteLine($"{numero_ejercicio_1} X {contadorWhile} = {multiplicacion}");

                contadorWhile ++;
            }

            break;
            
        // Ejercicio 2 - Do While
        case 2:
            // Variable que hacepta números enteros positivos y negativos
            int numero_ejercicio_2;
            int contadorDoWhile;
            Console.WriteLine("\nHaz elegido la opción \"Saber si un número es positivo o negativo y su contador.\"");

            // El usuario deberá ingresar un numero entero positivo o negativo
            Console.Write($"\n{nombre} digita un número positivo 0 negativo (ej: 2, -1): ");
            numero_ejercicio_2 = int.Parse(Console.ReadLine()!);

            // Si el número ingresado es mayor a 0, el número es positivo
            if (numero_ejercicio_2 > 0)
            {
                // Iniciamos la variable contador en 1
                contadorDoWhile = 1;
                Console.WriteLine($"\nEl número {numero_ejercicio_2} es positivo\n");

                // Se imprime por consola números de 1 hasta el número ingresado por consola
                do
                {
                    Console.WriteLine($"Contador = {contadorDoWhile}");
                    contadorDoWhile ++;
                } while (contadorDoWhile <= numero_ejercicio_2);

            } else if(numero_ejercicio_2 < 0) // Si el número ingresado es menor a 0, el número es negativo
            {
                // Iniciamos la variable contador en -1
                contadorDoWhile = -1;
                Console.WriteLine($"\nEl número {numero_ejercicio_2} es negativo\n");

                // Se imprime por consola números de -1 hasta el número ingresado por consola
                do
                {
                    Console.WriteLine($"Contador = {contadorDoWhile}");
                    contadorDoWhile --;
                } while (contadorDoWhile >= numero_ejercicio_2);

            }

            break;

        // Ejercicio 3 - For
        case 3:
            // Declaramos las variables a usar para los datos del rectángulo
            int ancho;
            int alto;
            int cantidad_rectangulos;
            string? rellenoString;
            bool rellenoBool;

            // Declaramos un array
            int[,]? arr;

            Console.WriteLine("\nHaz elegido la opción \"Dibujar rectángulos.\" \n");

            // Pedimos los datos que se requieren para el rectángulo
            // Ingresamos el ancho por consola
            Console.Write("Digita el ancho del rectángulo: ");
            ancho = int.Parse(Console.ReadLine()!);

            // Ingresamos el alto por consola
            Console.Write("Digita el alto del rectángulo: "); 
            alto = int.Parse(Console.ReadLine()!);

            // Ingresamos la cantidad de rectángulos que queramos que se dibujen por consola
            Console.Write("Digita el número de rectángulos: ");
            cantidad_rectangulos = int.Parse(Console.ReadLine()!);

            // Ingresamos por consola si queremos o no un rectángulo con relleno
            Console.Write($"{nombre} quieres el rectángulo con relleno? (1. true, 0. false): ");
            rellenoString = Console.ReadLine();

            // Hacemos una conversión de string a boolean, dependiendo de esto el programa sabrá
            // Si lo que le hemos pedido es dibujar rectángulo con relleno o sin relleno
            rellenoBool = Convert.ToBoolean(rellenoString);

            // Inicializamos nuestro array
            // Con esto podremos saber las posiciones de los asteríscos que diburán el rectángulo
            // Y así poder dibujar el rectángulo con relleno o sin relleno
            arr = new int[alto, ancho];

            // Agregamos un salto de línea
            Console.WriteLine();

            // A partir de aquí se comienzan a dibujar los rectángulos
            // Dependiendo de la cantidad que hemos ingresado
            for (var numeroFiguras = 0; numeroFiguras < cantidad_rectangulos; numeroFiguras++)
            {
                Console.WriteLine("--------------------" +
                                  $"\n{numeroFiguras + 1}.) \n");

                // Con la variable a se colocan las posiciones para el alto del rectángulo
                // Que serán de 0 hasta lo que ingresamos en consola para el alto
                for (var a = 0; a < alto; a++)
                {
                    // Con la variable b se colocan las posiciones para el ancho del rectángulo
                    // Que serán de 0 hasta lo que ingresamos en consola para el ancho
                    for (var b = 0; b < ancho; b++)
                    {
                        // Guardamos dichas posicion es en nuestro array
                        arr[a, b] = b;

                        // A partir de aquí se dibujarán los rectángulos con o sin relleno
                        switch (rellenoBool)
                        {
                            case true:
                                for (var i = 0; i < arr.Length; i++)
                                {
                                    if (arr[a, b] == (arr[1, 1] = i)) 
                                    {
                                        Console.Write($"*", b);
                                        continue;
                                    }

                                    if (arr[a, b] == (arr[2, 1] = i)) continue;
                                }

                                break;

                            case false:
                                Console.Write("*", b);
                                break;
                        }
                    }

                    Console.WriteLine(" ");
                }

                Console.WriteLine(" ");
            }

            break;

        // Imprimimos un mensaje de salida
        case 0:
            Console.WriteLine("\nHaz elegido la opción \"Salir.\"" +
                              "\n\nHasta Pronto...\n");
            break;

        // Imprimimos un mensaje de error
        default:
            Console.WriteLine("\nError!!!... Opción incorrecta \n");
            break;
    } if (opcion == 0) break; // Si la opción es igual a 0, se rompe el ciclo y se termina el programa
    
    // Volvemo a imprimir el menú de opciones y a pedir que el usuario vuelva a ingresar una oción
    Console.Write($"\nQué más deseas hacer {nombre}?: \n" +
                  "\n1.) Calcular la tabla de multiplicar de un número." +
                  "\n2.) Saber si un número es positivo o negativo y su contador." +
                  "\n3.) Dibujar rectángulos." +
                  "\n0.) Salir." +
                  "\n\nOpción: ");

    opcion = int.Parse(Console.ReadLine()!);
}
