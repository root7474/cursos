package org.calculadora;

import java.util.Scanner; // Importamos a la librería "Scanner" para el ingreso de datos

/**
 * Clase que se encargá de ejecutar las opciones que eliga el usuario
 * Dentro de esta clase tendremos:
 * Un atributo "nombre" de tipo String donde recibiremos el nombre de usuario de la clase principal
 * Un constructor en donde inicializamos el atributo "nombre"
 * Una función para el menú de opciones
 * Una función para evaluar los datos ingresados por el usuario
 */
public class Operaciones {
    String nombre; // Creamos un atributo para el nombre del usuario
    
    /**
     * Constructor de la clase que tiene como parámetro: 
     * @param nombre que contendrá el nombre de usuario
     */
    public Operaciones(String nombre) {
        this.nombre = nombre; // Inicializamos al atributo "nombre" con lo que halla dentro del parámetro "nombre" del constructor
    }

    // Menú de opciones
    public void menu() {
        boolean pass = false; // Declaramos una variable booleana que utilizaremos como condicional del bucle "While()"
        Integer cantidad; // Declaramos una variable "cantidad" para ingresar una cantidad de números a operar

        // Instanciamos las clases necesarias para los respectivos cálculos y les pasamos como parámetro el atributo "nombre"
        SumaClass calcularSuma = new SumaClass(nombre);
        RestaClass calcularResta = new RestaClass(nombre);
        MultiplicacionClass calcularMultiplicaion = new MultiplicacionClass(nombre);
        DivisionClass calcularDivision = new DivisionClass(nombre);
        PorcentajeClass calcularPorcentaje = new PorcentajeClass(nombre);

        // Mientras "pass" sea igual a false, se ejecutará lo siguiente
        while (pass == false) {
            // Declaramos una variable "userData" que recibirá la opción que ingrese el usuario
            Integer userDataInt = integerError("\n" + nombre + " Elige una opción:\n" +
                                               "\n1.) Suma." +
                                               "\n2.) Resta." +
                                               "\n3.) Multiplicación." +
                                               "\n4.) División." +
                                               "\n5.) Porcentaje." +
                                               "\n0.) Salir." +
                                               "\n\nOpción: "); // Llamamos a la función "integerError()" para evaluar la cantidad ingresada
            
            if (userDataInt.equals(1)) {
                // Si el usuario ha ingresado la opción 1, pedimos que se ingrese una cantidad de números a sumar
                cantidad = integerError("\nDigita una cantidad a sumar: "); // Llamamos otra vez a la función "integerError()" para evaluar la cantidad ingresada
                calcularSuma.suma(cantidad); // Enviamos dicha cantidad a la función "suma()" de la clase "SumaClass()"
                System.out.println(calcularSuma); // Imprimimos el resultado de la suma
            } else if (userDataInt.equals(2)) {
                // Si el usuario ha ingresado la opción 2, pedimos que se ingrese una cantidad de números a restar
                cantidad = integerError("\nDigita una cantidad a restar: "); // Llamamos de nuevo a la función "integerError()" para evaluar la cantidad ingresada
                calcularResta.resta(cantidad); // Enviamos dicha cantidad a la función "resta()" de la clase "RestaClass()"
                System.out.println(calcularResta); // Imprimimos el resultado de la resta
            } else if (userDataInt.equals(3)) {
                // Si el usuario ha ingresado la opción 3, pedimos que se ingrese una cantidad de números a multiplicar
                cantidad = integerError("\nDigita una cantidad a multplicar: "); // Volvemos a llamar a la función "integerError()" para evaluar la cantidad ingresada
                calcularMultiplicaion.multiplicacion(cantidad); // Enviamos dicha cantidad a la función "multiplicacion()" de la clase "MultiplicacionClass()"
                System.out.println(calcularMultiplicaion); // Imprimimos el resultado de la multiplicación
            } else if (userDataInt.equals(4)) {
                // Si el usuario ha ingresado la opción 4, pedimos que se ingrese una cantidad de números a dividir
                cantidad = integerError("\nDigita una cantidad a dividir: "); // Volvemos a llamar a la función "integerError()" para evaluar la cantidad ingresada

                // A continuación creamos un bloque tryCatch para evaluar si existe una división entre cero
                try {
                    // Si no existe una división entre cero, el programa continuará su ejecución
                    calcularDivision.division(cantidad); // Enviamos ls cantidad ingresada a la función "division()" de la clase "DivisionClass()"
                    System.out.println(calcularDivision); // Imprimimos el resultado de la división
                } catch (ArithmeticException e) {
                    System.out.println("Error!!!... División entre cero"); // Si existe una división entre cero, el programa nos lanza un error
                }
            } else if (userDataInt.equals(5)) {
                // Si el usuario ha ingresado la opción 5, entonces solo llamaremos a la función "porcentaje()" de la clase "PorcentajeClass()"
                calcularPorcentaje.porcentaje();
                System.out.println(calcularPorcentaje); // Mostramos el resultado del cálculo del porcentaje de un número ingresado por consola
            } else if (userDataInt.equals(0)) {
                // Si el usuario ha ingresado la opción 0
                System.out.println("Hasta pronto..."); // Imprimimos un mensaje de despedida
                pass = true; // "pass" será igual a true y el programa detendrá su ejecución
            } else {
                System.out.println("Opción desconcocida. Ingresa números del 0 al 5"); // Si la opción ingresada es incorrecta, lanzaremos este error
            }
        }
    }

    /**
     * Creamos una función en donde evaluaremos si lo que se ha ingresado es un número o un caracter
     * Esta función solo acepta números enteros
     * Los parámetros de esta función son:
     * @param message que recibirá un String en cada llamada a la función
     * @return en donde devolveremos un dato de tipo String convertido a entero
     */
    public Integer integerError(String message) {
        boolean pass = false; // Declaramos una variable "pass" que la usaremos como condicional para el bucle "while()" de esta función
        Integer userDataInt = 0; // Declaramos una variable "userDataInt" de tipo entero y la inicializamos en cero
        Scanner opcionScanner = new Scanner(System.in); // Dentro de la variable "opcionScanner" Creamos una instancia de la clase "Scanner()"

        // Mientras que "pass" sea igual a false, haremos lo siguiente
        while (pass == false) {
            try {
                // Ejecutamos este bloque try si no hay errores durante la ejecución
                System.out.print(message); // Imprimimos lo que hay dentro del parámetro "message"
                userDataInt = Integer.parseInt(opcionScanner.next()); // Convertimos a entero lo que se ingrese por teclado y guardamos dicho valor dentro de "userDataInt"
                pass = true; // Si se ha ingresado un número, "pass" será igual a true y se romperá el ciclo
            } catch (NumberFormatException e) {
                // Generamos un bloque catch para generar un error si lo que se ha ingresado son caracteres
                // Este bloque se ejecutará hasta que se ingrese un número
                System.out.println("Error!!!... No debes ingresar números decimales ni tampocos letras o símbolos especiales");
            }
        }

        return userDataInt; // Retornamos el valor de "userDataInt"
    }
}
