package poo.herencia;
import poo.clases.Motor;
import poo.clases.Vehiculo;

/**
 * Clase derivada, Clase hija o subclase
 */
public class Motocicleta extends Vehiculo {
    Boolean baul;

    public Motocicleta() {
    }

    public Motocicleta(String fabricante, String modelo, Double cc, Integer year, Boolean sport, Integer speed, Motor motor, Boolean baul) {
        super(fabricante, modelo, cc, year, sport, speed, motor);
        this.baul = baul;
    }
}
