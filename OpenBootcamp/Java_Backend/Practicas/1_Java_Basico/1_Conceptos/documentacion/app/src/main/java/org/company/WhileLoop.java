package org.company;

public class WhileLoop {
    public static void main(String[] args) {
        int count = 0;

        while (count < 10) {
            count++;
            // if (count == 6) continue; // Continúa con la siguiente iteración

            if (count == 6) break; // Rompe el ciclo
            System.out.println("Número: " + count);
        }

        System.out.println("Fin");
    }
}
