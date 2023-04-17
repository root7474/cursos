package org.calculadora;

public class PorcentajeClass extends Operaciones {
    Double porcentaje;

    public PorcentajeClass(String nombre) {
        super(nombre);
    }

    public void porcentaje(double numero) {
        porcentaje = numero / 100;
        System.out.println("\nEl porcentaje de " + numero + " es: " + porcentaje);
    }
}
