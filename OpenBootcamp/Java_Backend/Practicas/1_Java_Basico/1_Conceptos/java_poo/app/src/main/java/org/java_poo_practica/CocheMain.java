package org.java_poo_practica;

public class CocheMain {
    public static void main(String[] args) {
        /* Coche coche1 = new Coche();
        Coche coche2 = new Coche("Rojo", "Honda", "Civic", 1500.5, 130.5);
        System.out.println(coche2);
        
        coche2.acelerar(50);
        System.out.println(coche2 + "\n"); */
        
        Coche cocheElectrico1 = new CocheElectrico();
        Coche cocheElectrico2 = new CocheElectrico("T220");
        Coche cocheElectrico3 = new CocheElectrico("Amarillo", "Ford", "Fiesta", 1403.9, 130.4, "T220");

        System.out.println(cocheElectrico2);
        System.out.println(cocheElectrico3);

        cocheElectrico3.acelerar(50);
        System.out.println(cocheElectrico3 + "\n");

        Coche cocheHibrido1 = new CocheHibrido();
        Coche cocheHibrido2 = new CocheHibrido("TXZ200");
        Coche cocheHibrido3 = new CocheHibrido("Azul", "Chevrolet", "Camaro", 1200.4, 120.5, "TXZ200");
        
        System.out.println(cocheHibrido2);
        System.out.println(cocheHibrido3);

        cocheHibrido3.acelerar(50);
        System.out.println(cocheHibrido3);
    }
}
