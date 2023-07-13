// See https://aka.ms/new-console-template for more information
using System;

namespace MyNamespace
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Puerta puerta = new Puerta(3, 200, "Café", "Madera", false);
            puerta.MostrarEstado();
            puerta.abrir();
            puerta.MostrarEstado();
        }
    }

    public class Puerta
    {
        int ancho;
        int alto;
        string ? color;
        string ? material;
        bool abierta;

        public Puerta()
        {
            
        }

        public Puerta(int ancho, int alto, string color, string material, bool abierta)
        {
            this.ancho = ancho;
            this.alto = alto;
            this.color = color;
            this.material = material;
            this.abierta = abierta;
        }

        public void abrir()
        {
            int opcion;

            Console.Write("\nQué deseas hacer?\n:" +
                          "\n1.) Abrir puerta." +
                          "\n2.) Cerrar puerta." +
                          "\n\nOpción: ");
            
            opcion = int.Parse(Console.ReadLine()!);

            if (opcion.Equals(1)) this.abierta = true;
            if (opcion.Equals(2)) this.abierta = false;
        }

        public void MostrarEstado()
        {
            Console.WriteLine($"\nAncho: {ancho}" +
                              $"\nAlto: {alto}" +
                              $"\nColor: {color}" +
                              $"\nMaterial: {material}" +
                              $"\nAbierta?: {abierta}");
        }
    }
}
