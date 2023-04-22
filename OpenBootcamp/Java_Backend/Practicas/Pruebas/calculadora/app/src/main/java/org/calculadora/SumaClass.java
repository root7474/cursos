package org.calculadora;

import java.util.Scanner;

public class SumaClass extends Operaciones {
    String resultado;

    public SumaClass(String nombre) {
        super(nombre);
    }

    public void suma(int cantidad) {
        Double suma = null;
        Double numero;
        Scanner numeroScanner = new Scanner(System.in);

        try {
            for (int i = 0; i < cantidad; i++) {
                System.out.print("Digita el número " + (i + 1) + ": ");
                numero = Double.parseDouble(numeroScanner.next());
        
                if (suma == null) {
                    suma = numero;
                } else {
                    suma = suma + numero;
                }
            }

            resultado = "\nEl resultado de la suma es: " + suma;
        } catch (NumberFormatException e) {
            resultado = "Error!!!... Solo debes ingresar números";
        }
    }

    @Override
    public String toString() {
        return resultado;
    }
}
