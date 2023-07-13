// See https://aka.ms/new-console-template for more information
namespace Cadenas
{
    public class Program
    {
        public static void Main(string[] args)
        {
            /* String ? str1;
            String ? str2 = null;
            String str3 = System.String.Empty;
            String str4 = "";
            String str5 = " ";

            str1 = null;

            // Tipo y salida
            Console.WriteLine($"str1: {str1}");
            Console.WriteLine($"str2: {str2}");
            Console.WriteLine($"str3: {str3.GetType()}");
            Console.WriteLine($"str4: {str4.GetType()}");
            Console.WriteLine($"str5: {str5.GetType()}"); */

            // Array
            /* char[] letras = {'#', 'D', '$'};
            Console.WriteLine(letras[0]);
            String str6 = "Hola, este es mi mensaje";
            Console.WriteLine(str6[0]); */

            // Concatenación
            /* String msg1 = "Buenos días";
            String msg2 = "estoy programando en C#";

            // Imprimir un mensaje
            Console.WriteLine($"{msg1}, {msg2}");

            String msg3 = msg1 + ", " + msg2;
            String msg4 = msg1;

            msg4 += ", " + msg2;
            Console.WriteLine(msg3);
            Console.WriteLine(msg4); */

            // Literales
            // Cracteres escapados -> \n, \u00c6, \r, \t
            /* String columns = "Column 1\tColumn 2\tColumn 3";
            String hr ="---------------------------------";
            String contents = "Contenido 1\tContenido 1\tContenido 1" +
                              "\nContenido 2\tContenido 2\tContenido 2" +
                              "\nContenido 3\tContenido 3\tContenido 3";

            Console.WriteLine(columns);
            Console.WriteLine(hr);
            Console.WriteLine(contents);

            String rows = "Contenido 4\tContenido 4\tContenido 4\r\n" +
                          "Contenido 5\tContenido 5\tContenido 5\r\nRow 3";
            Console.WriteLine(rows); */

            // Algunos caracteres escapados: \', \", \\, \v, etc
            /* String multiLinea1 = "Hola " +
                                 "este es un mensaje " +
                                 "en varias líneas";

            String multiLinea2 = @"Hola
                                   este es un mensaje
                                   en varias líneas";
            
            String comillas = "Él se autoprclama \"programador\"";
            Console.WriteLine(comillas); */

            // Interpolación
            /* var persona = (nombre: "David", edad: 27,
                           lenguajes: "Pyton, Java, C#, JavaScript, TypeScript, Dart, PHP");
            
            Console.WriteLine($"Nombre: {persona.nombre}" +
                              $"\nEdad: {persona.edad}" +
                              $"\nLenguajes de programación: {persona.lenguajes}"); */
            
            // Subcadenas
            /* String miCadena = "    Este es mi mensaje    ";

            // Substring(), Replace()
            String miCadena2 = miCadena.Substring(0, 10);
            Console.WriteLine(miCadena2);

            String miCadena3 = miCadena.Replace("mensaje", "podcast");
            Console.WriteLine(miCadena3);
            
            // Limpiar espacios
            String miCadena4 = miCadena.Trim();
            Console.WriteLine(miCadena4);
            
            // Encontrar caracter
            int index = miCadena4.IndexOf("m");
            Console.WriteLine(index); */

            // Strings nulos y vacios
            /* String str1 = "Hello";
            String nullStr = null!;
            String emptyStr = String.Empty;
            String tempStr = str1 + nullStr;
            Console.WriteLine(tempStr);

            bool b = emptyStr == nullStr;
            Console.WriteLine(b);

            String newStr = emptyStr + nullStr;
            Console.WriteLine(newStr);
            Console.WriteLine(emptyStr.Length);
            // Console.WriteLine(nullStr.Length); // Error
            Console.WriteLine(newStr.Length);

            nullStr = "a";
            Console.WriteLine(nullStr.Length);

            emptyStr = "";
            emptyStr += nullStr;
            Console.WriteLine(emptyStr); // a

            // StringBuilder
            StringBuilder strBuilder = new StringBuilder("Hola mundo");
            Console.WriteLine(strBuilder[0]); // H
            Console.WriteLine(strBuilder); // Hola mundo */

            // Pasar cadena a número si es posible
            int i = 0;
            String s = "Hola";
            bool resultado = int.TryParse(s, out i);
            Console.WriteLine($"{resultado}, i: {i}");
        }
    }
}
