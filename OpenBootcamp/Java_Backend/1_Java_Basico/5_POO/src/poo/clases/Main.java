package poo.clases;

import poo.herencia.Camion;
import poo.herencia.Coche;
import poo.herencia.Motocicleta;

public class Main {
    public static void main(String[] args) {
        // 1. Clases y objetos
        // Clase identyificador = new Clase();
        // Crear un objeto utilizando un constructor vacio
        Vehiculo toyotaPrius = new Vehiculo();

        // Crear un objeto utilizando un constructor con parámetros
        Motor motorGTI =new Motor("GTI", 190, 459.0, 6);
        Vehiculo fordMondeo = new Vehiculo("Ford", "Mondeo", 2.1, 2010, false, 0, motorGTI);
        System.out.println(fordMondeo.fabricante + "\n" + fordMondeo.year + "\n" + fordMondeo.speed);
        
        fordMondeo.acelerar(50);
        System.out.println(fordMondeo.fabricante + "\n" + fordMondeo.year + "\n" + fordMondeo.speed);
    
        // 2. Herencia
        Motocicleta kawasakiNinja = new Motocicleta();
        kawasakiNinja.fabricante = "Kawasaki";
        System.out.println("Fin del programa");

        // ,3. Polimorfismo
        Vehiculo vehiculo;

        vehiculo = new Motocicleta();
        vehiculo.acelerar(50);

        vehiculo = new Coche();
        vehiculo.acelerar(50);
        
        vehiculo = new Camion();
        vehiculo.acelerar(50);

        // 4. Clases abstractas: No se pueden instanciar, solo se instancian las clases hija
    }
}
