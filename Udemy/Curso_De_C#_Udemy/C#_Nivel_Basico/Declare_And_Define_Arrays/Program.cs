// See https://aka.ms/new-console-template for more information
namespace Declare_And_Define_Arrays
{
    class Program
    {
        public static void Main(string[] args)
        {
            /* int[] degrees = {20, 30, 31, 32, 40};
            string[] fruits = {"Apple", "Banana", "Fig", "Cherry"}; */

            // Accessing values
            /* Console.WriteLine(fruits[0]); // Apple
            Console.WriteLine(fruits[1]); // Banana
            Console.WriteLine(fruits[3]); // Fig */

            /* fruits[0] = "Watermelon";
            fruits[1] = "Lemon";
            Console.WriteLine(fruits[0]);
            Console.WriteLine(fruits[1]); */

            // How many elemnts?:
            /* Console.WriteLine(fruits.Length);
            Console.WriteLine(degrees.Length); */

            int[] degrees = {200, 30, 31, 32, 40};
            string[] fruits = {"Apple", "Banana", "Fig", "Cherry"};

            // Loop through fruits
            /* for (int fruit = 0; fruit < fruits.Length; fruit++)
            {
                Console.WriteLine(fruits[fruit]);
            } */

            /* Array.Sort(fruits);

            foreach (string i in fruits)
            {
                Console.WriteLine(i);
            } */

            Array.Sort(degrees);

            foreach (int i in degrees)
            {
                Console.WriteLine(i);
            }
        }
    }
}