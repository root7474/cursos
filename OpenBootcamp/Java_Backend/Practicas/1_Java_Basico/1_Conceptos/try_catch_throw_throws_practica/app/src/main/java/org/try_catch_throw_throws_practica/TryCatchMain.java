package org.try_catch_throw_throws_practica;

public class TryCatchMain {
    public static void main(String[] args) {
        try {
            Integer division = 5 / 5;
            System.out.println("El resultado de la división es: " + division);
        } catch (ArithmeticException e) {
            System.out.println("Error!!!... División por cero");
        } finally {
            System.out.println("Cierre de recursos");
        }

        System.out.println("Fin");
    }
}
