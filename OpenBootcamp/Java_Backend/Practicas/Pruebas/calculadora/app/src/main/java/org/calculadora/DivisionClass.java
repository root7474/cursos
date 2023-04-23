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

        for (int i = 0; i < cantidad; i++) {
            numero = doubleSumaError("Digita el número " + (i + 1) + ": ");
            
            if (division == null) {
                division = numero;
            } else {
                if (numero == 0) throw new ArithmeticException();
                division = division / numero;
            }
        }

        resultado = "\nEl resultado de la división es: " + ((double)Math.round(division * 100) / 100);
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
