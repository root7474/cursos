package org.openbootcamp;

public class Main {
    public static void main(String[] args) {
        /* CocheElectrico cocheElectrico = new CCocheElectrico();
        cocheElectrico.velocidadMaxima = 14;
        cocheElectrico.matricula = "ABC 1234 ES";

        System.out.println(cocheElectrico.compruebaMatricula("XXX")); */

        /* Coche coche = new Coche();
        coche.setSonido("BRRR");
        System.out.println(coche.getSonido()); */

        // Coche coche = new Coche();
        // coche.diHola();
        // coche.sumaNumeros(3.7, 4.5);
    }
}

interface Vehiculo {
    // int velocidadMaxima;
    // String matricula;
    // String sonido;

    /* public Vehiculo() {
        System.out.println("Estoy en el constructor de vehículo");
    } */

    /* abstract public String getSonido();
    abstract public void setSonido(String sonido); */



   /* public boolean compruebaMatricula(String matricula) {
        if (matricula == "XXX") {
            return true;
        }

        return false;
    } */

    /* public void diHola() {
        System.out.println("Hola!!!");
    } */


    int variables = 0;

    void Acelerar(int cuantaVelocidad);
    void Frenar(int cuantaVelocidad);
}

/* class Coche extends Vehiculo {
    public  String getSonido() {
        return "Soy un súper sonido: " + this.sonido;
    }

    public void setSonido(String sonido) {
        this.sonido = sonido;
    }
} */

/* class CocheElectrico extends Coche {

} */

/* class Moto extends Vehiculo {
    public  String getSonido() {
        return "Soy un sonidillo de moto: " + this.sonido;
    }

    public void setSonido(String sonido) {
        this.sonido = sonido;
    }
} */

/* class Motor {
    String tipoMotor;
    public Motor() {
        System.out.println("Estoy en el constructor de la clase Motor.");
    }
} */

// Java prohíbe de forma explícita la herencia múltiple
// de implementación de Clases
/* class Coche extends Motor, Vehiculo {

} */

/* class Coche extends Vehiculo {
    public void diHola() {
        System.out.println("Soy un coche!!!");
    }

    public int sumaNumeros(int a, int b) {
        System.out.println("Soy el suma números de INT");
        return a + b;
    }

    public float sumaNumeros(float a, float b) {
        System.out.println("Soy el suma números de FLOAT");
        return a + b * (float)9.0;
    }

    public void sumaNumeros(double a, double b) {
        System.out.println("Soy el suma números de DOUBLE");
        System.out.println("El resultado es: " + (a + b));
    }
} */

class Coche implements Vehiculo {
    public void Acelerar(int cuantaVelocidad) {

    }

    public void Frenar(int cuantaVelocidad) {

    }
}
