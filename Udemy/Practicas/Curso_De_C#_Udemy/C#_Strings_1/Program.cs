// See https://aka.ms/new-console-template for more information
namespace C_Sharp_Strings_1
{
    class Program
    {
        public static void Main(string[] args)
        {
            /* string nuevoMensaje = "\nHola Mundo Desde c# 9!!!";
            Console.WriteLine(nuevoMensaje);

            // Longitud de nuevoMensaje
            Console.WriteLine("El número de carácteres en '" + nuevoMensaje + "' es: " + nuevoMensaje.Length);

            // Conversión a mayúsculas
            Console.WriteLine("Mayúsculas: " + nuevoMensaje.ToUpper());

            // Conversión a minúsculas
            Console.WriteLine("Minúsculas: " + nuevoMensaje.ToLower() + "\n"); */

            // Concatenación de cadenas
            // string primerTexto = "Hola y ";
            // string segundoTexto = "Bienvenido a C#!!!\n";
            // string textoCompleto = primerTexto + segundoTexto;

            /* Console.WriteLine(textoCompleto);

            // Metodo Concat
            Console.WriteLine(string.Concat(primerTexto, segundoTexto)); */

            // Interpolación de cadenas
            /* string textoCompleto = $"El texto completo es: {primerTexto} {segundoTexto}";
            Console.WriteLine(textoCompleto);

            // Acceso a los carácteres de una cadena
            Console.WriteLine(textoCompleto[0]);
            Console.WriteLine(textoCompleto[1]);
            Console.WriteLine(textoCompleto[2]);
            Console.WriteLine(textoCompleto[3]);

            // Encontrar posición
            Console.WriteLine("Posición de 'x': " + textoCompleto.IndexOf("x")); */

            // Secuencia de escape de carácteres y crácteres especiales
            string nuevoMensaje = "Hola a todos!!!\nBienvenidos \t\t\t\ta este \"curso \b\bde C#\"";
            Console.WriteLine(nuevoMensaje);
        }
    }
}
