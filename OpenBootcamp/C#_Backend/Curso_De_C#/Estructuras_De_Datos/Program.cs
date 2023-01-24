// See https://aka.ms/new-console-template for more information
Coords misCoordenadas = new Coords(2.5, 10.1, 5);
Console.WriteLine($"X: {misCoordenadas.X}");
Console.WriteLine($"Y: {misCoordenadas.Y}");
Console.WriteLine($"Z: {misCoordenadas.Z}");

Coords misCoordenadas2 = misCoordenadas with { X = 10 };
Console.WriteLine(misCoordenadas2);

public struct Coords
{
    public Coords(double x, double y, double z)
    {
        X = x;
        Y = y;
        Z = z;
    }

    public double X { get; set; }
    public double Y { get; set; }
    public double Z { get; set; }

    public override string ToString() => $"({X}, {Y}, {Z})";
}
