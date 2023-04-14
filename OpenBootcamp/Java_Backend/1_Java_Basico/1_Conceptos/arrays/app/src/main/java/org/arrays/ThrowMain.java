package org.arrays;
import java.util.Scanner;

public class ThrowMain {
    public static void main(String[] args) {
        try {
            leerNombres();
        } catch(NameFormatException e) {
            e.printStackTrace();
        }
    }

    private static void leerNombres() throws NameFormatException {
        Scanner teclado = new Scanner(System.in);
        System.out.println("Introduce un nombre: ");

        while (teclado.hasNext()) {
            System.out.println("Introduce un nombre: ");
            String nombre = teclado.nextLine();

            if (nombre.length() < 8) {
                teclado.close();
                throw new NameFormatException("El nombre debe contener mínimo 8 caracteres");
            }
        }

        teclado.close();
    }
}
