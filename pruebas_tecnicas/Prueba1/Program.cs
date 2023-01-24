using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;



class Result
{

    /*
     * Complete the 'fizzBuzz' function below.
     *
     * The function accepts INTEGER n as parameter.
     */

    public static void fizzBuzz(int n)
    {
        for (int i = 1; i <= n; i++)
        {
            if (i % 3 == 0 && i == 15)
            {
                Console.WriteLine("FizzBuzz");
                continue;
            } else if (i % 3 == 0)
            {
                Console.WriteLine("Fizz");
                continue;
            } else if (i % 5 == 0)
            {
                Console.WriteLine("Buzz");
                continue;
            }
            
            Console.WriteLine(i);
        }
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        Console.Write("Número: ");
        int n = Convert.ToInt32(Console.ReadLine()!.Trim());
        Result.fizzBuzz(n);
    }
}

