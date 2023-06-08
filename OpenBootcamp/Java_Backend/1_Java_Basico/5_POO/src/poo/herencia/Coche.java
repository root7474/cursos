package poo.herencia;
import poo.clases.Motor;
import poo.clases.Vehiculo;

public class Coche extends Vehiculo {
    Integer numPuertas;

    public Coche() {
    }

    public Coche(String fabricante, String modelo, Double cc, Integer year, Boolean sport, Integer speed, Motor motor, Integer numPuertas) {
        super(fabricante, modelo, cc, year, sport, speed, motor);
        this.numPuertas = numPuertas;
    }
}
