// See https://aka.ms/new-console-template for more information
namespace OOP_Interfaces_For_Abstraction
{
    public interface ICar
    {
        public void carColor(); // No body for this interface method
    }

    // Class to implement the ICar interface
    public class Car01 : ICar
    {
        public void carColor()
        {
            Console.WriteLine("The color for our car is white!!!");
        }

        public class Program
        {
            public static void Main(string[] args)
            {
                Car01 newCar = new Car01();
                newCar.carColor();
            }
        }
    }
}
