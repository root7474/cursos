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

        try {
            for (int i = 0; i < cantidad; i++) {
                numero = doubleSumaError("Digita el número " + (i + 1) + ": ");

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
