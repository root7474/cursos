package com.funciones;

public class Operadores {
    public static void main(String[] args) {
        // Aritméticos
        int numero1 = 10;
        int numero2 = 20;
        int resultado = numero1 + numero2;
        
        System.out.println(resultado);
        System.out.println(resultado + 5.77);

        /* 
         * Comparación:
         * > mayor que
         * < menor que
         * >= mayor o igual que
         * <= menor o igual que
         * == igual que
         */

        boolean mayorQue = numero1 > numero2;
        System.out.println(mayorQue);

        boolean menorQue = numero1 < numero2;
        System.out.println(menorQue);

        /* 
         * Lógicos
         * and &&
         * or ||
         */

        boolean resultado1 = numero1 > 5 && numero1 < 10;
        int edad = 17;
        boolean carnetJoven = edad >= 15 && edad <= 26;
    }
}
