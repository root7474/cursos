package org.company;

public class Main {
    public static void main(String[] args) {
        // String coche = "Alfa Romeo";
        Coche cocheOBJ = new CocheHibrido();

        Coche cocheOBJ2 = new CocheElectrico("Rojo", "Honda", "Civic", 1430.45, 5.4, "mtor");
        // cocheOBJ2.acelerar(50);
        System.out.println(cocheOBJ2);

        cocheOBJ2.peso = 1350.8;
        System.out.println(cocheOBJ2);

        CocheElectrico cocheElectrico = new CocheElectrico();

        cocheElectrico.motorElectrico = "Ejemplo motor";
        cocheElectrico.color = "Verde";
        cocheElectrico.fabricante = "Honda";
        cocheElectrico.modelo = "Civic";

        System.out.println(cocheElectrico);

        CocheElectrico cocheElectrico2 = new CocheElectrico("Azul", "Alfa", "Romeo", 1500d,
                4.99, "TXZ");

        System.out.println(cocheElectrico2);

        cocheElectrico2.acelerar(50);
        System.out.println(cocheElectrico2);
    }
}