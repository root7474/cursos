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
        
        for (int i = 0; i < cantidad; i++) {
            numero = doubleSumaError("Digita el número " + (i + 1) + ": ");

            if (suma == null) {
                suma = numero;
            } else {
                suma = suma + numero;
            }
        }

            resultado = "\nEl resultado de la suma es: " + suma;
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
