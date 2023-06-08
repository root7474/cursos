package poo.herencia;
import poo.clases.Motor;
import poo.clases.Vehiculo;

public class Camion extends Vehiculo {
    Double capacidadCarga;

    public Camion() {
    }

    public Camion(String fabricante, String modelo, Double cc, Integer year, Boolean sport, Integer speed, Motor motor, Double capacidadCarga) {
        super(fabricante, modelo, cc, year, sport, speed, motor);
        this.capacidadCarga = capacidadCarga;
    }
}
