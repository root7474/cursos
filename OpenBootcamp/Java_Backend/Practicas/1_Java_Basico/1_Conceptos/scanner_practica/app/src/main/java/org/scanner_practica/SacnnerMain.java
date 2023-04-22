package org.scanner_practica;

import java.util.Scanner;

public class SacnnerMain {
    public static void main(String[] args) {
        String nombre;
        Integer edad;
        Scanner scanner = new Scanner(System.in);

        System.out.print("Introduce tu nombre: ");
        nombre = scanner.nextLine();

        System.out.print("Introduce tu edad: ");
        edad = Integer.parseInt(scanner.nextLine());

        System.out.println("\nNombre: " + nombre + "\n" + "Edad: " + edad);
    }
}
