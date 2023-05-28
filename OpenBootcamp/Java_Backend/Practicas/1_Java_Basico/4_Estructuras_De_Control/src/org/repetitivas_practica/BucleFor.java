package org.repetitivas_practica;

public class BucleFor {
    public static void main(String[] args) {
        // for ()
        /* String[] nombres = {"David", "Felipe", "Patricia"};

        // for (int i = 0; i < 10; i++) System.out.println("Número: " + (i + 1));
        for (int i = 0; i < nombres.length; i++) System.out.println("Nombre " + (i + 1) + ": " + nombres[i]); */

        int suma = 0;
        int[] numeros = {1, 2, 3, 4, 5, 6, 7};

        for (int i = 0; i < numeros.length; i++) {
            suma += numeros[i];
            System.out.println(suma);
        }
    }
}
