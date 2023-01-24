// See https://aka.ms/new-console-template for more information
namespace Inheritance
{
    class Program
    {
        public static void Main(string[] args)
        {
            PL01 newPlayer = new PL01();
            newPlayer.Speaking(); // Calling speaking method to display the speaking on screen
        
            // Output value of name and ID
            Console.WriteLine($"Name: {newPlayer.name}, ID: {newPlayer.playerID}");
        }
    }
}
