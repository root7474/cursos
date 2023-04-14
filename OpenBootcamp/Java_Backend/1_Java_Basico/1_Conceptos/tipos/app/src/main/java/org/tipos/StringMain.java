package org.tipos;

public class StringMain {
    public static void main(String[] args) {
        // La clase String

        /* 
         * length()
         * startsWith()
         * ebdsWith()
         * indexOf()
         * subString()
         * trim()
         * equals()
         * compareTo
         */

        String mensaje = "  Hola Mundo  ";
        System.out.println(mensaje.length());
        
        String mensaje2 = mensaje.toUpperCase();
        System.out.println(mensaje2);
        System.out.println(mensaje2.trim());
        
        String mensaje3 = mensaje2.trim();
        String otro = "hola mundo";
        if (mensaje3.equalsIgnoreCase(otro)) System.out.println("Verdadero");
    }
}
