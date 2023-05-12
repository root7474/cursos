package com.funciones_practica;

public class Operadores {
    public static void main(String[] args) {
        // Aritméticos
        int numero1 = 10;
        int numero2 = 30;
        int suma = numero1 + numero2;

        System.out.println(numero1 + " + " + numero2 + " = " + suma);
        System.out.println(suma + 5.55);

        /* 
         * Comparación:
         * > mayor que
         * < menor que
         * >= mayor o igual que
         * <= menor o igual que
         * == igual que
         */

        boolean mayorQue = numero2 > numero1;
        System.out.println(numero2 + " > " + numero1 + " = " + mayorQue);

        boolean menorQue = numero1 < numero2;
        System.out.println(numero1 + " < " + numero2 + " = " + menorQue);

        /* 
         * Lógicos
         * and &&
         * or ||
         */

        boolean resultado1 = numero1 > 4 && numero2 < 40;
        int edad = 27;
        boolean resultado2 = edad >= 25 && edad <= 26;
    }
}
