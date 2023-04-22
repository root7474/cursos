package org.calculadora;

import java.util.Scanner;

public class DivisionClass extends Operaciones {
    String resultado;

    public DivisionClass (String nombre) {
        super(nombre);
    }

    public void division(int cantidad) {
        Double numero;
        Double division = null;
        Scanner numeroScanner = new Scanner(System.in);

        try {
            for (int i = 0; i < cantidad; i++) {
                System.out.print("Digita el número " + (i + 1) + ": ");
                numero = Double.parseDouble(numeroScanner.next());
                
                
                if (division == null) {
                    division = numero;
                } else {
                    if (numero == 0) throw new ArithmeticException("Error!!!... Division entre cero");
                    division = division / numero;
                }
            }

            resultado = "\nEl resultado de la división es: " + division;
        } catch (NumberFormatException e) {
            resultado = "Error!!!... Solo debes ingresar números";
        }
    }

    @Override
    public String toString() {
        return resultado;
    }
}
