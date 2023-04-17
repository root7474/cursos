package org.calculadora;

import java.util.NoSuchElementException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner nombreScanner = new Scanner(System.in);
        System.out.print("Bienvenido!!!...\nDigita tu nombre: ");
        
        try {
            String nombre = nombreScanner.nextLine();
            Operaciones operacionesCalculos = new Operaciones(nombre);
            operacionesCalculos.menu();
        } catch (NoSuchElementException e) {
            System.out.println("\nHasta pronto...");
        }
    }
}
