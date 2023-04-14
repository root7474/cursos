package org.arrays;

public class TryCatchMain {
    public static void main(String[] args) {
        try {
            int result = 5 / 5;
            System.out.println("El reultado es {result}");
        } catch (ArithmeticException e) {
            System.out.println("Error!!!... División por cero");
        } finally {
            System.out.println("Cierre de recursos");
        }
        
        System.out.println("Fin");
    }
}
