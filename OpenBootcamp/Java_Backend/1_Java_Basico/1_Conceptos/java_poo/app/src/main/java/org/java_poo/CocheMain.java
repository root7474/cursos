package org.java_poo;

public class CocheMain {
    public static void main(String[] args) {
        String coche = "alfa romeo";
        Coche cocheObj = new CocheHibrido();
        // Coche cocheObj2 = new Coche("rojo", "Honda", "Civic", 1430.45, 4.5);
        Coche cocheObj2 = new CocheElectrico("rojo", "Honda", "Civic", 1430.45, 4.5, "Txz");

        cocheObj2.acelerar(50);
        System.out.println(cocheObj2);

        cocheObj2.peso = 1150.8;
        System.out.println(cocheObj2);

        CocheElectrico cocheElectrico = new CocheElectrico();
        cocheElectrico.motorElectrico = "Ejemplo motor";
        cocheElectrico.color = "verde";
        cocheElectrico.fabricante = "Honda";
        cocheElectrico.modelo = "Civic";

        System.out.println(cocheElectrico);

        CocheElectrico cocheElectrico2 = new CocheElectrico("Azul", "Alfa", "Romeo", 1500.0, 4.99, "Txz");
        System.out.println(cocheElectrico2);

        cocheElectrico2.acelerar(50);
        System.out.println(cocheElectrico2);
    }
}
