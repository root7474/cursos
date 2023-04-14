package org.calculadora;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner nombreScanner = new Scanner(System.in);
        System.out.print("Bienvenido!!!... Digita tu nombre: ");
        String nombre = nombreScanner.nextLine();

        OperacionesCalculos operacionesCalculos = new OperacionesCalculos(nombre);
        operacionesCalculos.menu();
    }
}
