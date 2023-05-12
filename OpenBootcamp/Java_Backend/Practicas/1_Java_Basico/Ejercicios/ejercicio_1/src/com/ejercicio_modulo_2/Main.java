package com.ejercicio_modulo_2;

/**
 * Clase para crear tipos de datos y imprimirlos por consola
 */

public class Main {
    /**
     * Función principal para ejecutar la aplicación
     * Creamos variables con surespectivo tipo de datos
     * Imprimimos el valor de esas variable
     * @param args
     */

    public static void main(String[] args) {
        // Creamos unas variables numericas de tipo entero
        byte numero1 = 1;
        short numero2 = 2;
        int numero3 = 3;
        long numero4 = 3167002210l;

        // Creamos unas variables numericas de tipo decimal
        float numero5 = 3.5f;
        double numero6 = 5.5;

        // Creamos unas variables de tipo booleano
        boolean verdadero = true;
        boolean falso = false;

        // Creamos una variable de texto de tipo caracter y de tipo cadena
        char caracter = 'D';
        String saludo = "Hola Mundo!!!";

        // Imprimimos por consola el valor de las variables
        System.out.println("Variables numericas enteras\n" +
                           "\nByte: " + numero1 +
                           "\nShort: " + numero2 +
                           "\nInt: " + numero3 +
                           "\nLong: " + numero4);

        System.out.println("\nVariables numericas decimales\n" +
                           "\nFloat: " + numero5 +
                           "\nDouble: " + numero6);

        System.out.println("\nVariables booleanas\n" +
                           "\nVerdadero: " + verdadero +
                           "\nFalso: " + falso);

        System.out.println("\nVariables de texto\n" +
                           "\nCaracter: '" + caracter + "'" +
                           "\nCadena: \"" + saludo + "\"");
    }
}
