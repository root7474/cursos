package org.calculadora;

import java.util.Scanner;

public class SumaClass extends Operaciones {
    Double suma = null;

    public SumaClass(String nombre) {
        super(nombre);
    }

    public void suma(int cantidad) {
        cantidad = cantidad;

        for (int i = 0; i < cantidad; i++) {
            System.out.print("Digita el número " + (i + 1) + ": ");
            numero = Double.parseDouble(numeroScanner.next());

            if (suma == null) {
                suma = numero;
            } else {
                suma = suma + numero;
            }
        }
    }

    @Override
    public String toString() {
        return "\nEl resultado de la suma es: " + suma;
    }
}
