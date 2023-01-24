package org.david;

public class Main {
    public static void main(String[] args) {
        // Parte 1
        System.out.println("Parte 1: \n");
        var numeroIf = -0.1;

        if (numeroIf < 0) {
            System.out.println("El número " + numeroIf + " es negativo.");
        } else if (numeroIf > 0) {
            System.out.println("El número " + numeroIf + " es positivo.");
        } else {
            System.out.println("El número " + numeroIf + " es igual a cero.");
        }

        // Parte 2
        System.out.println("\nParte 2: \n");
        var numeroWhile = 0;

        while (numeroWhile < 3) {
            numeroWhile++;
            System.out.println("Número: " + numeroWhile);
        }

        // Parte 3
        System.out.println("\nParte 3: \n");
        var numeroDoWhile = 3;

        do {
            // numeroDoWhile++;
            System.out.println("Número: " + numeroDoWhile);
            // break;
        } while (numeroDoWhile < 3);

        // Parte 4
        System.out.println("\nParte 4: \n");
        // var numeroFor = 0;

        for (var numeroFor = 0; numeroFor <= 3; numeroFor++) {
            System.out.println("Número: " + numeroFor);
        }

        // Parte 5
        System.out.println("\nParte 5: \n");
        var estacion = "otoño";

        switch (estacion) {
            case "verano":
                System.out.println("Es verano.");
                break;

            case "primavera":
                System.out.println("Es primavera.");
                break;

            case "otoño":
                System.out.println("Es otoño.");
                break;

            case "invierno":
                System.out.println("Es invierno.");
                break;
        }
    }
}