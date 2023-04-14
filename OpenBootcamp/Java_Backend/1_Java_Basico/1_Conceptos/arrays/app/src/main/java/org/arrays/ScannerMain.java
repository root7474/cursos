package org.arrays;

import java.util.Scanner;

public class ScannerMain {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Introduce tu nombre: ");
        String nombre = scanner.nextLine();
        
        System.out.print("Introduce tu edad: ");
        double numero = scanner.nextDouble();

        System.out.println("\nNombre: " + nombre);
        System.out.println("Edad: " + numero);

        System.out.println("\nHola Mundo!!!");
    }
}
