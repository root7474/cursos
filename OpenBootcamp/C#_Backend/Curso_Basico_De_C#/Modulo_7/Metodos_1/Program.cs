// See https://aka.ms/new-console-template for more information
using System;

namespace Metodos_1
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Motos motos = new Motos();

            Motos.Arrancar();
            motos.ArrancarMoto();
            
            // Extensión
            ExtensionMotos extensionMotos = new ExtensionMotos();
            extensionMotos.Acelerar();

            // Retornos de métodos
            int cantidadGasolina = motos.CantidadGasolina();
            Console.WriteLine($"Nos queda {cantidadGasolina} litros de combustible.");

            // Sobrecarga
            dynamic echarGasolinaFloat = motos.EcharGasolina(10.555);
            Console.WriteLine($"Ahora tenemos {echarGasolinaFloat} litros de combustible.");
        }
    }

    public class Motos
    {
        public static void Arrancar()
        {
            Console.WriteLine("Arranca");
        }

        public void ArrancarMoto()
        {
            Console.WriteLine("Arrancar moto");
        }

        public int CantidadGasolina()
        {
            // Código
            int gasolina = 20; // Litros
            return gasolina;
        }

        public int EcharGasolina(int litros)
        {
            int nivelDeposito = CantidadGasolina() + litros;
            return nivelDeposito;
        }

        public float EcharGasolina(float litros)
        {
            float nivelDeposito = CantidadGasolina() + litros;
            return nivelDeposito;
        }

        public double EcharGasolina(double litros)
        {
            double nivelDeposito = CantidadGasolina() + litros;
            return nivelDeposito;
        }
    }
}
