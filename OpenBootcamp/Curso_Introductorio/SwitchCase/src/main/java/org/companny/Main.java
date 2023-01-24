package org.companny;

public class Main {
    public static void main(String[] args) {
        var estacion = "verano";

        switch (estacion) {
            case "verano":
                System.out.println("Es verano");
                break;

            case "invierno":
                System.out.println("Es invierno");
                break;

            default:
                System.out.println("La estación es variable");
                break;
        }
    }
}