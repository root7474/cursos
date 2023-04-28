package com.funciones;

/**
 * Sobrecarga permite duplicar un método siempre y cuando tengan diferente númeor/tipo de parámetros
 */

public class Sobrecarga {
    public static void main(String[] args) {
        
    }

    private static double suma(double numero1, double numero2) {
        return numero1 + numero2;
    }

    private static int suma(int numero1, int numero2) {
        return numero1 + numero2;
    }

    private static int suma(int numero1, int numero2, int numero3) {
        return numero1 + numero2 + numero3;
    }
}
