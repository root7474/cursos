package com.company;

public class Funciones {
    public static void main(String[] args) {
        holaMundo();
        holaMundo("David");
        holaMundo("David", "Rodríguez");
        holaMundo(26);

        /* String hola = devolverHola();
        System.out.println(hola); */
    }

    private static void holaMundo() {
        System.out.println("Hola Mundo en Java!!!");
    }

    private static void holaMundo(String name) {
        System.out.println("Hola " + name);
    }
    
    private static void holaMundo(String name, String surname) {
        System.out.println("Hola " + name + " " + surname);
    }

    private static void holaMundo(int number) {
        System.out.println("El número es: " + number);
    }

    /* private static String devolverHola() {
        return "Hola";
    } */
}
