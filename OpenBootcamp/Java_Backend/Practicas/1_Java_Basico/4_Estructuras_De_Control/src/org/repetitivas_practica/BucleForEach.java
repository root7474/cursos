package org.repetitivas_practica;

public class BucleForEach {
    public static void main(String[] args) {
        //forEach ()
        /* String[] nombres = {"David", "Felipe", "Patricia"};
        for (String nombre : nombres) System.out.println("Nombre: " + nombre); */

        int suma = 0;
        int[] numeros = {1, 2, 3, 4, 5, 6, 7};

        for (int numero : numeros) {
            suma += numero;
            System.out.println(suma);
        }
    }
}
