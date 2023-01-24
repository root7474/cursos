package org.PropiedadPublicaPrivada;

public class Main {
    public static void main(String[] args) {
        Vehiculo coche = new Vehiculo();
        coche.setTipo("Coupe");
        coche.setVelocidadMaxima(128);
        coche.setRapido(true);

        Vehiculo moto = new Vehiculo();
        moto.setTipo("Scooter");
        moto.setVelocidadMaxima(50);
        moto.setRapido(false);

        System.out.println("\nTipo: " + coche.getTipo() +
                           "\nVelocidad: " + coche.getVelocidadMaxima() +
                           "\nRápido?: " + coche.isRapido());

        System.out.println("\nTipo: " + moto.getTipo() +
                           "\nVelocidad: " + moto.getVelocidadMaxima() +
                           "\nRápido?: " + moto.isRapido() + "\n");
    }
}

// abstract class Vehiculo
class Vehiculo {
    private String tipo;
    private int velocidadMaxima;
    private boolean rapido;
    // private  String sonido;

    /* abstract public void setSonido();
    abstract public void getSonido(); */

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public int getVelocidadMaxima() {
        return velocidadMaxima;
    }

    public void setVelocidadMaxima(int velocidadMaxima) {
        this.velocidadMaxima = velocidadMaxima;
    }

    public boolean isRapido() {
        return rapido;
    }

    public void setRapido(boolean rapido) {
        this.rapido = rapido;
    }
}
