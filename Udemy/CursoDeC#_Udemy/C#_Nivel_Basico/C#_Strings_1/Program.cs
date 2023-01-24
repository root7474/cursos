// See https://aka.ms/new-console-template for more information
namespace C_Sharp_Strings_1
{
    class Program
    {
        public static void Main(string[] args)
        {
            /* string newMessage = "Hi C# developers!";
            Console.WriteLine(newMessage);

            // Length of newMessage
            Console.WriteLine("The number of characters in '" + newMessage + "' is: " + newMessage.Length);
            
            // Uppercase conversion
            Console.WriteLine("Uppercase: " + newMessage.ToUpper());

            // Lowercase conversion
            Console.WriteLine("Lowercase: " + newMessage.ToLower()); */

            // String concatenation
            // string firstText = "Hello and ";
            // string secondText = "welcome to C#";
            /* string fullText = firstText + secondText;

            Console.WriteLine(fullText);

            // Concat Method
            Console.WriteLine(string.Concat(firstText, secondText)); */

            // String Interpolation
            /* string fullText = $"The full text is: {firstText} {secondText}";
            Console.WriteLine(fullText);

            // Access string characters
            Console.WriteLine(fullText[0]);
            Console.WriteLine(fullText[1]);
            Console.WriteLine(fullText[2]);

            // Find position
            Console.WriteLine(fullText.IndexOf("x")); */
            string newMsg = "Hi there!\nWelcome \t\t\t\tto this \"C# \b\bcourse\"";
            Console.WriteLine(newMsg);
        }
    }
}
