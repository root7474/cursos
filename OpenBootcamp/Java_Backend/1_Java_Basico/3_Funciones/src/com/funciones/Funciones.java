package com.funciones;

public class Funciones {
    public static void main(String[] args) {
        // Opción 1: Función sin parámetros y sin tipo de retorno
        // showMenu();

        // Opción 2: Función sin parámetros y con tipo de retorno
        /* String menu = getMenu();
        System.out.println(menu);
        System.out.println("\n" + getMenu());

        Double price = getPrice();
        System.out.println(price); */

        // Opción 3: Función con parámetros y sin tipo de retorno
        // imprimirSaludoBuenosDias("OpenBootcamp");

        // Opción 4: Función con parámetros y con tipo de retorno
        String nombre = "David";
        String apellido = "Rodríguez";
        String saludo = obtenerSaludo(nombre, apellido);
        System.out.println(saludo);

        int resultado1 = suma(50, 200);
        System.out.println(resultado1);
    }

    private static int suma(int numero1, int numero2) {
        return numero1 + numero2;
    }

    private static String obtenerSaludo(String nombre, String apellido) {
        return "Buenas tardes " + nombre + " " + apellido;
    }

    /* private static void imprimirSaludoBuenosDias(String nombre) {
        System.out.println("Buenos días: " + nombre);
    } */

    /* private static Double getPrice() {
        return 100.99;
    } */

    /* 
     * Void indica que no devuelve nada
     */

    /* static void showMenu() {
        System.out.println("Bienvenidos al E-commerce de zapatillas:\n" +
                           "\n1 - Ver zapatillas" +
                           "\n2- Comprar zapatillas" +
                           "\n3 - Salir");
    }

    static String getMenu() {
        return "Bienvenidos al E-commerce de zapatillas:\n" +
               "\n1 - Ver zapatillas" +
               "\n2 - Comprar zapatillas" +
               "\n3 - Salir";
    } */
}
