namespace Cadenas
{
    public class Program
    {
        public static void Main(string[] args)
        {
            /* string ? str1;
            string ? str2 = null;
            string str3 = System.String.Empty;
            string str4 = "";
            string str5 = " ";

            str1 = null;

            // Tipo y salida
            Console.WriteLine($"str1: {str1}");
            Console.WriteLine($"str2: {str2}");
            Console.WriteLine($"str3: {str3.GetType()}");
            Console.WriteLine($"str4: {str4.GetType()}");
            Console.WriteLine($"str5: {str5.GetType()}");

            // Array
            char[] letters = {'#', 'D', '$'};
            Console.WriteLine(letters[0]);
            string str6 = "Hola, este es mi mensaje";
            Console.WriteLine(str6[0]);

            // Concatenación
            string msg1 = "Buenos días";
            string msg2 = "estoy programando en C#";

            // Imprimir un mensaje
            Console.WriteLine($"{msg1}, {msg2}");
            
            string msg3 = msg1 + msg2;
            string msg4 = msg1;
            
            msg4 += ", " + msg2;
            Console.WriteLine(msg4); */

            // Literales
            // Cracteres escapados -> \n, \u00c6, \r, \t
            /* string columns = "Column 1\tColumn 2\tColumn 3";
            string hr = "---------------------------------";
            string contents = "Contenido 1\nContenido 1\nContenido 1" +
                              "\tContenido 2 Contenido 2 Contenido 2" +
                              "\tContenido 3 Contenido 3 Contenido 3";

            Console.WriteLine(columns);
            Console.WriteLine(hr);
            Console.WriteLine(contents);

            string rows = "Contenido 1 Contenido 1 Contenido 1\r\n" +
                          "Contenido 2 Contenido 2 Contenido 2\r\nRow 3";
            Console.WriteLine(rows);

            // Algunos caracteres escapados: \', \", \\, \v, etc
            string multilinea1 = "Hola " +
                                 "este es un mensaje " +
                                 "en varias líneas";
            string multilinea2 = @"Hola
                                   este es un mensaje
                                   en varias líneas";
            
            string comillas = "Él se autoprclama \"programador\".";
            Console.WriteLine(comillas); */

            // Interpolación
            /* var persona = (nombre: "David", edad: "27", 
                           lenguajes: "Pyton, Java, C#, JavaScript, TypeScript, Dart, PHP");
            
            Console.WriteLine($"Nombre: {persona.nombre}\n" +
                              $"Edad: {persona.edad}\n" +
                              $"Lenguajes de desarrollo: {persona.lenguajes}"); */
            
            // Subcadenas
            /* string miCadena = "Este es mi mensaje";

            // Substring(), Replace()
            string miCadena2 = miCadena.Substring(0, 10);
            Console.WriteLine(miCadena2);

            string miCadena3 = miCadena.Replace("mensaje", "podcast");
            Console.WriteLine(miCadena3);

            // Limpiar espacios
            string miCadena4 = miCadena.Trim();
            Console.WriteLine(miCadena4);

            // Encontrar caracter
            int index = miCadena.IndexOf('m');
            Console.WriteLine(index); */

            // Strings nulos y vacios
            /* string str1 = "Hello";
            string nullStr = null!;
            string emptyStr = String.Empty;
            string tempStr = str1 + nullStr;
            Console.WriteLine(tempStr);

            bool b = emptyStr == nullStr;
            Console.WriteLine(b);

            string newStr = emptyStr + nullStr;
            Console.WriteLine(newStr);
            Console.WriteLine(emptyStr.Length);
            // Console.WriteLine(nullStr.Length);
            Console.WriteLine(newStr.Length);

            nullStr =  "a";
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
            string s = "Hola";
            bool result = int.TryParse(s, out i);
            Console.WriteLine($"{result}, i: {i}");
        }
    }
}
