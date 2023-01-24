package org.Intro_POO;

public class Main {
    public static void main(String[] args) {
        Coche coche1 = new Coche();
        Coche coche2 = new Coche(2, 90);

        System.out.println("\nCoche 1: \n" +
                           "\nNúmero de puertas: " + coche1.numPuertas +
                           "\nVelocidad máxima: " + coche1.velocidadMaxima +
                           "\nVelocidad inicial: " + coche1.velocidadInicial);

        System.out.println("\nCoche 2: \n" +
                           "\nNúmero de puertas: " + coche2.numPuertas +
                           "\nVelocidad máxima: " + coche2.velocidadMaxima +
                           "\nVelocidad inicial: " + coche2.velocidadInicial + "\n");
    }
}

class Coche {
    int numPuertas;
    int velocidadMaxima;
    float velocidadInicial;

    public Coche() {
        numPuertas = 4;
        velocidadMaxima = 78;
    }

    public Coche(int numPuertas, int velocidadMaxima) {
        this.numPuertas = numPuertas;
        this.velocidadMaxima = velocidadMaxima;
    }
}
