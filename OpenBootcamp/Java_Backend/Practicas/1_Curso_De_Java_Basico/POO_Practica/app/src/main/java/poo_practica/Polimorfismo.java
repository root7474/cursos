package app.src.main.java.poo_practica;

public class Polimorfismo {
    public static void main(String[] args) {
        // Polimorfismo
        Coche coche = new CocheElectrico();

        if (coche instanceof CocheElectrico) {
            System.out.println("\nCoche Eléctrico.\n");
        }
        if (coche instanceof CocheHibrido) {
            System.out.println("\nCoche Híbrido.\n");
        }
    }
}
