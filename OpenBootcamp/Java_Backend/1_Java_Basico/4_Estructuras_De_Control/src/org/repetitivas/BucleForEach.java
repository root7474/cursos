

public class BucleForEach {
    public static void main(String[] args) {
        /* String[] nombres = {"David", "Patricia", "Felipe"};

        for (String nombre : nombres) {
            System.out.println("Nombre: " + nombre);
        } */

        int suma = 0;
        int[] numeros = {5, 7, 8};

        for (int numero : numeros) {
            suma += numero;
            System.out.println(suma);
        }
    }
}
