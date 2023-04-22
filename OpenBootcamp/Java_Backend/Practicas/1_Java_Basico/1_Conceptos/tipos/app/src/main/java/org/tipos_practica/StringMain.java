package org.tipos_practica;

public class StringMain {
    public static void main(String[] args) {
        /* 
         * length()
         * startsWith()
         * endsWith()
         * indexOf()
         * subString()
         * trim()
         * equals()
         * compareTo()
         */

        String mensaje = "  Hola Mundo  ";
        System.out.println("Logitud de \"" + mensaje + "\": " + mensaje.length());
        System.out.println(mensaje.toUpperCase().trim());

        String mensaje2 = mensaje.trim();
        String otro = "  hola mundo  ";
        if (mensaje2.equalsIgnoreCase(otro.trim())) System.out.println("Verdadero");
    }
}
