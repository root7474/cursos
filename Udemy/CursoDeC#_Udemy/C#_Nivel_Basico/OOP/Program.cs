// See https://aka.ms/new-console-template for more information
namespace OOP
{
    class Program
    {
        public static void Main(string[] args)
        {
            Player newOBJ_1 = new Player();
            Player newOBJ_2 = new Player();
            Player newOBJ_3 = new Player();

            Console.WriteLine("\nName: " + newOBJ_1.name + ", Number: " + newOBJ_1.number);
            Console.WriteLine("Name: " + newOBJ_2.name + ", Number: " + newOBJ_2.number);
            Console.WriteLine("Name: " + newOBJ_3.name + ", Number: " + newOBJ_3.number);
        }
    }
}
