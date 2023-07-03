package org.calculadora;

// Importamos la librerías a usar 
import java.util.NoSuchElementException; // Importamos a la librería "NoSuchElementException" que sirve para verificar si existen datos de entrada
import java.util.Scanner; // Importamos a la librería "Scanner" para el ingreso de datos

/**
 * Clase principal
 * Esta se encargará de la ejecucón del programa
 */
public class Main {
    /**
     * Método principal que ejecuta el programa y que tendrá como parámetros:
     * @param args
     */
    public static void main(String[] args) {
        Scanner nombreScanner = new Scanner(System.in); // Instanciamos a la clase "Scanner()" con el parámetro "System.in" para la entrada de datos
        System.out.print("Bienvenido!!!...\nDigita tu nombre: "); // Imprimimos un mensaje de bienvenida
        
        try {
            // Bloque try por si no ocurre ningúna excepción durante la ejecución del programa
            String nombre = nombreScanner.nextLine(); // Guardamos el nombre que ingrese el usuario
            Operaciones operacionesCalculos = new Operaciones(nombre); // Instanciamos la clase "Operaciones()" y le pasamos como parámetro el nombre del usuario
            operacionesCalculos.menu(); // Llamamos a la función "menu()" de la clase "Operaciones()"
        } catch (NoSuchElementException e) {
            // Bloque catch por si hay una excepción durante el programa
            System.out.println("\nHasta pronto..."); // Si se han ingresado datos vacios, el programa detendrá su ejecución
        }
    }
}
