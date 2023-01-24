package metodos_de_la_clase_string;

public class ArraysMain {
    public static void main(String[] args) {
        String nombre1 = "Nombre 1";
        String nombre2 = "Nombre 2";
        String nombre3 = "Nombre 3";
        String nombre4 = "Nombre 4";

        String[] nombres1 = new String[4];
        
        String[] nombres2 = new String[] {
            nombre1, 
            nombre2, 
            nombre3, 
            nombre4
        };

        int[] numeros = new int[5];
        Coche[] coches = new Coche[2];

        nombres1[0] = nombre1;
        nombres1[1] = nombre2;
        nombres1[2] = nombre3;
        nombres1[3] = nombre4;

        System.out.println("\n" + nombres1[0] + "\n");

        for (int i = 0; i < nombres2.length; i++) {
            System.out.println(nombres1[i]);
        }

        System.out.println();
    }
}
