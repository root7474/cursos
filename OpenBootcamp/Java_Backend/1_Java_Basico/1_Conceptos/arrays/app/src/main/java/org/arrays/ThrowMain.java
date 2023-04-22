package org.arrays;
import java.util.Scanner;

public class ThrowMain {
    public static void main(String[] args) {
        /* try {
            leerNombres();
        } catch(NameFormatException e) {
            e.printStackTrace();
        } */
        leerNombres("Introduce un nombre: ");
    }

    private static void leerNombres(String message) {
        Scanner teclado = new Scanner(System.in);
        // System.out.println("Introduce un nombre: ");
        boolean pass = false;

        while (pass == false) {
            System.out.print(message);
            String nombre = teclado.nextLine();

            if (nombre.length() < 8) {
                // teclado.close();
                // throw new NameFormatException("El nombre debe contener mínimo 8 caracteres");
                System.out.println("El nombre debe contener mínimo 8 caracteres\n");
                continue;
            } else {
                System.out.println("Nombre correcto. Bienvenido " + nombre);
                pass = true;
            }
        }

        teclado.close();
    }
}
