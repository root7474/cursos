// See https://aka.ms/new-console-template for more information
namespace OOP_Enumerations
{
    enum MonthsOfYear
    {
        January,
        Februeary,
        March,
        April,
        May,
        June,
        July,
        August,
        September,
        October,
        November,
        Dicember
    }

    class Program
    {
        public static void Main(string[] args)
        {
            /* MonthsOfYear myMonth = MonthsOfYear.Februeary;
            Console.WriteLine(myMonth); */

            // This will give an error
            // int myMonthNumber = int.Parse(MonthsOfYear.Februeary);
            int myMonthNumber = (int) MonthsOfYear.Februeary;
            myMonthNumber += 1;
            
            Console.WriteLine("My month number is: " + myMonthNumber);
        }
    }
}
