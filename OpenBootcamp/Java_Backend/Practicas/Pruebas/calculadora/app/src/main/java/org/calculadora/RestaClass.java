package org.calculadora;

import java.util.Scanner;

public class RestaClass extends Operaciones {
    String resultado;

    public RestaClass(String nombre) {
        super(nombre);
    }

    public void resta(int cantidad) {
        Double resta = null;
        Double numero;
        Scanner numeroScanner = new Scanner(System.in);

        try {
            for (int i = 0; i < cantidad; i++) {
                System.out.print("Digita el número " + (i + 1) + ": ");
                numero = Double.parseDouble(numeroScanner.next());

                if (resta == null) {
                    resta = numero;
                } else {
                    resta = resta - numero;
                }
            }

            resultado = "\nEl resultado de la resta es: " + resta;
        } catch (NumberFormatException e) {
            resultado = "Error!!!... Solo debes ingresar números";
        }
    }

    @Override
    public String toString() {
        return resultado;
    }
}
