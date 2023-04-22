package org.calculadora;

import java.util.Scanner;

public class PorcentajeClass extends Operaciones {
    String resultado;

    public PorcentajeClass(String nombre) {
        super(nombre);
    }

    public void porcentaje() {
        Double porcentaje;

        try {
            System.out.print("\nDigita un número para calcular su porcentaje: ");
            Scanner numeroScanner = new Scanner(System.in);
            Double numero = Double.parseDouble(numeroScanner.next());
            
            porcentaje = numero / 100;
            resultado = "\nEl porcentaje de " + numero + " es: " + porcentaje;
        } catch (NumberFormatException e) {
            resultado = "Error!!!... Solo debes ingresar números";
        }
    }

    @Override
    public String toString() {
        return resultado;
    }
}
