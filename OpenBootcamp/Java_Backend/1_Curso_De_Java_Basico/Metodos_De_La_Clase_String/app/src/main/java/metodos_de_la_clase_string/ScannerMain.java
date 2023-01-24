package metodos_de_la_clase_string;

import java.util.Scanner;

public class ScannerMain {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Introduce un nombre: ");
        String nombre = scanner.nextLine();

        System.out.print("Introduce un número: ");
        int numero = scanner.nextInt();

        System.out.println("El nombre introducido es: " + nombre);
        System.out.println("El número introducido es: " + numero);

        System.out.println("Hola mundo");
    }
}
