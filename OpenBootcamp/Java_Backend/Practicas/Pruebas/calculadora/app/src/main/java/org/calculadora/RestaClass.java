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

        for (int i = 0; i < cantidad; i++) {
            numero = doubleSumaError("Digita el número " + (i + 1) + ": ");

            if (resta == null) {
                resta = numero;
            } else {
                resta = resta - numero;
            }
        }

        resultado = "\nEl resultado de la resta es: " + resta;
    }

    public static Double doubleSumaError(String message) {
        boolean pass = false;
        Double userDataDouble = 0.0;
        Scanner userDataScanner = new Scanner(System.in);
        
        while (pass == false) {
            System.out.print(message);

            try {
                userDataDouble = Double.parseDouble(userDataScanner.next());
                pass = true;
            } catch (NumberFormatException e) {
                System.out.println("Error!!!... Solo debes ingresar números");
            }
        }

        return userDataDouble;
    }

    @Override
    public String toString() {
        return resultado;
    }
}
