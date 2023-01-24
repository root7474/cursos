package org.david;

public class Main {
    public static void main(String[] args) {
        Coche coche = new Coche();

        System.out.println(coche.numeroDePuertas + "\n" +
                coche.velocidadMaxima);
        System.out.println(coche.velocidadCtual);

        Coche coche2 = new Coche(2, 90);

        System.out.println(coche2.numeroDePuertas + "\n" +
                           coche2.velocidadMaxima);
        System.out.println(coche2.velocidadCtual);
    }
}

class Coche {
    int numeroDePuertas;
    int velocidadMaxima;
    float velocidadCtual;

    public Coche() {
        numeroDePuertas = 5;
        velocidadMaxima = 120;
        System.out.println("Estoy en el constructor sin parámetros");
    }

    public Coche(int numeroDePuertas, int velocidadMaxima) {
        this.numeroDePuertas = numeroDePuertas;
        this.velocidadMaxima = velocidadMaxima;
        System.out.println("Estoy en el constructor con parámetros");
    }
}
