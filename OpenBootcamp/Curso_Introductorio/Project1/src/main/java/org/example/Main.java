package org.example;

public class Main {
    public static void main(String[] args) {
        // System.out.println("Hello World In Java 17 From IntelliJ Idea!!!");
        /* int resultado = Suma(10, 30);
        System.out.println("El resultado de la suma es: " + resultado); */

        Potatoe miPotatoe = new Potatoe();
        miPotatoe.QuitarBrazo();
        miPotatoe.QuitarBrazo();
        miPotatoe.QuitarBrazo();

        System.out.println(miPotatoe.brazos);
    }

    public static int Suma(int a, int b) {
        return a + b;
    }
}

class Potatoe {
    public int brazos = 0;

    public void QuitarBrazo() {
        this.brazos--;
    }
}
