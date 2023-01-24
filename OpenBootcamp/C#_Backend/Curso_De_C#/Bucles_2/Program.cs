// SWITCH CASE
Console.Write("Qué día es hoy?: ");
string hoy = Console.ReadLine()!.ToUpper();

switch (hoy)
{
    case "LUNES":
        Console.WriteLine("Hoy es Lunes");
        break;
    case "MARTES":
        Console.WriteLine("Hoy es Martes");
        break;
    case "MIERCOLES":
        Console.WriteLine("Hoy es Miercoles");
        break;
    case "JUEVES":
        Console.WriteLine("Hoy es Jueves");
        break;
    case "VIERNES":
        Console.WriteLine("Hoy es Viernes");
        break;
    case "SABADO":
        Console.WriteLine("Hoy es Sabado");
        break;
    case "DOMINGO":
        Console.WriteLine("Hoy es Domingo");
        break;
    default:
        Console.WriteLine("No conozco ese día");
        break;
}
