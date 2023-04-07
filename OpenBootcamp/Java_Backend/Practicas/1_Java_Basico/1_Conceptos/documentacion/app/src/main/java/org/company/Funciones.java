package org.company;

public class Funciones {
    public static void main(String[] args) {
        // holaMundo();
        // holaMundo("David");
        // holaMundo("Andrés");

        // String hola = devolverHola("David");
        // System.out.println(hola);

        holaMundo();
        holaMundo(4);
        holaMundo("David");
        holaMundo("David", "Rodríguez");

        int suma = suma(7, 3);
        System.out.println("La suma es: " + suma);
    }

    public static void holaMundo() {
        System.out.println("Hola Mundo Desde un Método");
    }

    public static void holaMundo(String nombre) {
        System.out.println("Hola " + nombre);
    }

    public static void holaMundo(int number) {
        System.out.println("El número es: " + number);
    }

    public static void holaMundo(String nombre, String apellido) {
        System.out.println("Hola " + nombre + " " + apellido);
    }

    public static String devolverHola(String nombre) {
        return "Hola " + nombre;
    }

    public static int suma(int num1, int num2) {
        return num1 + num2;
    }
}
