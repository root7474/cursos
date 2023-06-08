package poo.clases;

/**
 * Clase base, clase padre o superclase
 */
public class Vehiculo {
    // 1. Atributos
    protected String fabricante;
    protected String modelo;
    protected Double cc;
    protected Integer year;
    protected Boolean sport;
    protected Integer speed;
    protected Motor motor;

    // 2. Constructores
    public Vehiculo() {
    }

    public Vehiculo(String fabricante, String modelo, Double cc, Integer year, Boolean sport, Integer speed, Motor motor) {
        this.fabricante = fabricante;
        this.modelo = modelo;
        this.cc = cc;
        this.year = year;
        this.sport = sport;
        this.speed = speed;
        this.motor = motor;
    }

    public Vehiculo(String fabricante, String modelo) {
        this.fabricante = fabricante;
        this.modelo = modelo;
    }

    // 3. Métodos (comportamiento)
    public void acelerar(Integer quantity) {
        this.speed += quantity;
    }

    // getter y setter


    // toString
}
