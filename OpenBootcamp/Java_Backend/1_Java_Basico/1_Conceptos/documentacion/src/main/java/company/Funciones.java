package company;

public class Funciones {
    public static void main(String[] args) {
        // holaMundo();
        // holaMundo();

        // holaMundo("David");
        // holaMundo("Andrés");

        // String hola = devolverHola();
        // System.out.println(hola);

        holaMundo();
        holaMundo(4);
        holaMundo("David");
        holaMundo("David", "Rodríguez");
    }

    public static void holaMundo() {
        System.out.println("Hola mundo desde un método");
    }

    private static void holaMundo(String nombre) {
        System.out.println("Hola " + nombre);
    }

    private static void holaMundo(int number) {
        System.out.println("El número es:  " + number);
    }

    private static void holaMundo(String nombre, String apellido) {
        System.out.println("Hola " + nombre + " " + apellido);
    }

    private static String devolverHola() {
        return "Hola";
    }

    private static int suma(int num1, int num2) {
        return num2 + num2;
    }
}
