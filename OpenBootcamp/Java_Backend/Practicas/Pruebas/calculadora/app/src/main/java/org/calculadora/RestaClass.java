package org.calculadora;

import java.util.Scanner; // Importamos a la librería "Scanner" para el ingreso de datos

/**
 * Clase que se encargará de ejecutar una operación de resta
 * Dentro de esta clase tendremos:
 * Un atributo llamado "resultado"
 * Un constructor para esta clase
 * Una función para calcular la resta
 * Una función para evaluar los datos que se ingresen por consola
 * Un método "toString()" que devuelve el resultado de la resta
 * Esta clase hereda los atributos de la clase "Operaciones()"
 */

public class RestaClass extends Operaciones {
    String resultado; // Declaramos un atributo resultado de tipo String

    /**
     * Constructor de la clase que tiene como parámetros:
     * @param nombre // Que recibe el nombre de usuario, heredado de la clase padre
     */
    public RestaClass(String nombre) {
        super(nombre); // Invocamos al método "super()" para heredar el atributo "nombre" del constructor de la clase superior
    }

    /**
     * Creamos una función "resta()" que tiene como parámetros:
     * @param cantidad que recibe una cantidad de números ingresada por el usuario
     */
    public void resta(int cantidad) {
        Double numero; // Declaramos una variable "numero"
        Double resta = null; // Declaramos una variable "resta" y la inicializamos en null

        // Creamos un bucle "for()" para recorrer la cantidad ingresada por el usuario
        for (int i = 0; i < cantidad; i++) {
            numero = doubleRestaError("Digita el número " + (i + 1) + ": "); // Dentro de "numero", invocamos a la función "doubleRestaError()" y le pasamos una cadena de caracteres

            if (resta == null) {
                resta = numero; // Si el valor de "resta" el null entonces le asignamos el valor de "numero"
            } else {
                resta = resta - numero; // Si no es null, hacemos una operación de resta en cada iteración
            }
        }

        resultado = "\nEl resultado de la resta es: " + resta; // Dentro de "resultado" guardamos una una cadena junto con el resultado de la resta
    }

    /**
     * Creamos una función en donde evaluaremos si lo que se ha ingresado es un número o un caracter
     * Esta función solo acepta números decimales
     * Los parámetros de esta función son:
     * @param message que recibe el valor de un String
     * @return devolvemos un String convertido a decimal
     */
    public static Double doubleRestaError(String message) {
        boolean pass = false; // Declaramos una variable "pass" que la usaremos como condicional para el bucle "while()" de esta función
        Double userDataDouble = 0.0; // Declaramos una variable "userDataDouble" de tipo Double y la inicializamos en cero
        Scanner userDataScanner = new Scanner(System.in); // Dentro de la variable "userDataScanner" Creamos una instancia de la clase "Scanner()"

        // Mientras que "pass" sea igual a false, haremos lo siguiente
        while (pass == false) {
            System.out.print(message); // Imprimimos lo que hay dentro del parámetro "message"

            try {
                // Ejecutamos este bloque try si no hay errores durante la ejecución
                userDataDouble = Double.parseDouble(userDataScanner.next()); // Convertimos a decimales lo que se ingrese por teclado y guardamos dicho valor dentro de "userDataDouble"
                pass = true; // Si se ha ingresado un número, "pass" será igual a true y se romperá el ciclo
            } catch (NumberFormatException e) {
                // Generamos un bloque catch para generar un error si lo que se ha ingresado son caracteres
                // Este bloque se ejecutará hasta que se ingrese un número
                System.out.println("Error!!!... Solo debes ingresar números");
            }
        }

        return userDataDouble; // Retornamos el valor de "userDataDouble"
    }

    // Agregamos un método "toString()" en el que retornaremos el valor del atributo resultado
    @Override
    public String toString() {
        return resultado;
    }
}
