

public class BucleFor {
    public static void main(String[] args) {
        // for ()
        /* for (int i = 0; i < 10; i++) {
            System.out.println("Número: " + (i + 1));
        } */

        /* String[] nombres = {"David", "Patricia", "Felipe"};

        for (int i= 0; i < nombres.length; i++) {
            System.out.println("Nombre " + (i + 1) + ": " + nombres[i]);
        } */

        int suma = 0;
        int[] numeros = {5, 7, 8};

        for (int i = 0; i < numeros.length; i++) {
            suma += numeros[i];
            System.out.println(suma);
        }
    }
}
