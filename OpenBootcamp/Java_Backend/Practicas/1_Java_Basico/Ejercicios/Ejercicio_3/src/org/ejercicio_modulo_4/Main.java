// Ejercicio 3
// Autor: David Rodríguez

package org.ejercicio_modulo_4;

/**
 * Clase principal que ejecuta el programa
 */

public class Main {
    /**
     * Declaramos un array de nombres
     * Recorremos el array con un bucle forEach()
     * @param args
     */

    public static void main(String[] args) {
        String[] nombres = {"David", "Patricia", "Felipe"}; // Declaramos un array de tipo String y le pasamos como valores algunas cadenas de nombres
        
        // Recorremos el array e imprimimos por consola cada uno de sus elementos
        for (String nombre : nombres) {
            System.out.print("| " + nombre + " | "); // Con la función "print()" imprimimos un texto concatenado en una misma línea
        }
    }
}
