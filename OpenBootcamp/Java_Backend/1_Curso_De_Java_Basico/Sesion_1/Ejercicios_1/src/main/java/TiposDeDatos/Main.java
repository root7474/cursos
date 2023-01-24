package TiposDeDatos;

public class Main {
    public static void main(String[] args) {
        // Numericos
        // Enteros
        byte numByte = 10;
        short numShort = 1;
        int numInt = 5;
        long numLong = 30000000000L;

        // Decimales
        float numFloat = 5.0F;
        double numDouble = 5.5;

        // Booleanos
        boolean booleano = true;

        // Texto
        char caracter = 'a';
        String cadena= "Hello World In Java!!!";

        // Imprimir tipos de datos
        System.out.println("\nShort: " + numShort +
                           "\nByte: " + numByte +
                           "\nInt: " + numInt +
                           "\nLong: " + numLong +
                           "\nFloat: " + numFloat +
                           "\nDouble: " + numDouble +
                           "\nBooleano: " + booleano +
                           "\nChar: " + caracter +
                           "\nString: " + cadena);
    }
}
