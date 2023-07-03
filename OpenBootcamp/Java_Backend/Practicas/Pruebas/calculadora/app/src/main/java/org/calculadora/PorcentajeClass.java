package org.calculadora;

import java.util.Scanner; // Importamos a la librería "Scanner" para el ingreso de datos

/**
 * Clase que se encargará de ejecutar una operación de porcentaje
 * Dentro de esta clase tendremos:
 * Un atributo llamado "resultado"
 * Un constructor para esta clase
 * Una función para calcular el porcentaje de un número
 * Una función para evaluar los datos que se ingresen por consola
 * Un método "toString()" que devuelve el resultado del porcentaje de un número
 * Esta clase hereda los atributos de la clase "Operaciones()"
 */
public class PorcentajeClass extends Operaciones {
    String resultado; // Declaramos un atributo resultado de tipo String

    /**
     * Constructor de la clase que tiene como parámetros:
     * @param nombre // Que recibe el nombre de usuario, heredado de la clase padre
     */
    public PorcentajeClass(String nombre) {
        super(nombre); // Invocamos al método "super()" para heredar el atributo "nombre" del constructor de la clase superior
    }

    /**
     * Creamos una función "porcentaje()" sin parámetros:
     */
    public void porcentaje() {
        Double porcentaje; // Declaramos una variable "porcentaje"
        Double numero = doublePorcentajeError("\nDigita un número para calcular su porcentaje: "); // Dentro de la variable "numero", invocamos a la función "doublePorcentajeError()" y le pasamos una cadena de caracteres

        porcentaje = numero / 100; // Calculamos el el porcentaje de un número haciendo una división entre el mismo número y 100
        resultado = "\nEl porcentaje de " + numero + " es: " + porcentaje; // Dentro de "resultado" guardamos una una cadena junto con el porcentaje de dicho número
    }

    /**
     * Creamos una función en donde evaluaremos si lo que se ha ingresado es un número o un caracter
     * Esta función solo acepta números decimales
     * Los parámetros de esta función son:
     * @param message que recibe el valor de un String
     * @return devolvemos un String convertido a decimal
     */
    public static Double doublePorcentajeError(String message) {
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
