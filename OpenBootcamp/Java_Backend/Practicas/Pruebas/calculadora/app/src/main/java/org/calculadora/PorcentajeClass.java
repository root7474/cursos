package org.calculadora;

import java.util.Scanner;

public class PorcentajeClass extends Operaciones {
    String resultado;

    public PorcentajeClass(String nombre) {
        super(nombre);
    }

    public void porcentaje() {
        Double porcentaje;
        Double numero = doubleSumaError("\nDigita un número para calcular su porcentaje: ");
        
        porcentaje = numero / 100;
        resultado = "\nEl porcentaje de " + numero + " es: " + porcentaje;
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
