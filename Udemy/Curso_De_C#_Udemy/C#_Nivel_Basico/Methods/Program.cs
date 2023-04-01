// See https://aka.ms/new-console-template for more information
namespace Methods
{
    class Program
    {
        public static void Main(string[] args)
        {
            /* NewGreeting("David", 26);
            NewGreeting("Andrés", 10); */

            int result = NewAddition(20, 30);
            Console.WriteLine("The result is: " + result);
        }

        public static int NewAddition(int x, int y)
        {
            int Addition = x + y;
            return Addition;
        }

        /* public static void NewGreeting(string name, int number) 
        {
            Console.WriteLine($"Hello and welcome {name} and your number is {number}");
        } */
    }
}
