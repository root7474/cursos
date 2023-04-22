package org.calculadora;

import java.util.Scanner;

public class MultiplicacionClass extends Operaciones {
    String resultado;

    public MultiplicacionClass(String nombre) {
        super(nombre);
    }

    public void multiplicacion(int cantidad) {
        Double multiplicacion = null;
        Double numero;
        Scanner numeroScanner = new Scanner(System.in);

        try {
            for (int i = 0; i < cantidad; i++) {
                System.out.print("Digita el número " + (i + 1) + ": ");
                numero = Double.parseDouble(numeroScanner.next());

                if (multiplicacion == null) {
                    multiplicacion = numero;
                } else {
                    multiplicacion = multiplicacion * numero;
                }
            }

            resultado = "\nEl resultado de la multiplicación es: " + multiplicacion;
        } catch (NumberFormatException e) {
            resultado = "Error!!!... Solo debes ingresar números";
        }
    }

    @Override
    public String toString() {
        return resultado;
    }
}
