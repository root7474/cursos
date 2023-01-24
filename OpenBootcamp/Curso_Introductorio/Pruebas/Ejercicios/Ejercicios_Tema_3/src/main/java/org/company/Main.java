package org.company;

public class Main {
    public static void main(String[] args) {

        // Parte 1
        int resultado = sumaNumeros(13, 15, 17);
        System.out.println("Parte 1:" +
                           "\nEl resultado de la suma es: " + resultado);

        // Parte 2
        miCoche coche = new miCoche();
        coche.sumaPuertas();
        System.out.println("\nParte 2: " +
                           "\nEl número de puertas es: " + coche.numPuertas);
    }

    // Parte 1: creamos una función para sumar números
    public static int sumaNumeros(int num1, int num2, int num3) {
        return num1 + num2 + num3;
    }
}

// Parte2: Creamos una clase llamada miCoche para la parte 1
class miCoche {
    public int numPuertas = 0;

    public void sumaPuertas() {
        this.numPuertas++;
    }
}
