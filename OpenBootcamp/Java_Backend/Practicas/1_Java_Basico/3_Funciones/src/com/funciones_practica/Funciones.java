package com.funciones_practica;

public class Funciones {
    public static void main(String[] args) {
        // Opción 1: Función sin parámetros y sin tipo de retorno
        // showMenu();

        // Opción 2: Función sin parámetros y con tipo de retorno
        /* String menu = getMenu();
        System.out.println(menu);
        System.out.println("\n" + getMenu());

        Double precio = getPrice();
        System.out.println("Precio: " + precio); */

        // Opción 3: Función con parámetros y sin tipo de retorno
        // imprimirSaludoBuenosDias("David");

        // Opción 4: Función con parámetros y con tipo de retorno
        String nombre = "David";
        String apellido = "Rodríguez";
        String datosPersonales = obtenerDatosPersonales(nombre, apellido);
        System.out.println("Información personal:\n" + datosPersonales);

        int suma = suma(700, 77);
        System.out.println("El resulatado de la suma es: " + suma);
    }

    private static int suma(int numero1, int numero2) {
        return numero1 + numero2;
    }

    private static String obtenerDatosPersonales(String nombre, String apellido) {
        return "\nNombre: " + nombre +
               "\nApellido: " + apellido;
    }

    /* private static void imprimirSaludoBuenosDias(String nombre) {
        System.out.println("Buenos días " + nombre);
    } */

    /* private static Double getPrice() {
        return 200.99;
    } */

    /* 
     * Void indica que no devuelve nada
     */

    /* static void showMenu() {
        System.out.println("Bienvenidos al E-Commerce de zapatillas.\n" +
                           "\n1 - Ver zapatillas" +
                           "\n2 - Comprar zapatillas" +
                           "\n3 - Salir");
    }

    static String getMenu() {
        return "Bienvenidos al E-Commerce de zapatillas.\n" +
                           "\n1 - Ver zapatillas" +
                           "\n2 - Comprar zapatillas" +
                           "\n3 - Salir";
    } */
}
