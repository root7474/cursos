package org.OpenBootcamp;

public class Main {
    public static void main(String[] args) {
        /* Coche coche = new Coche();
        coche.Acelerar(50);

        var resultado = Suma(2, 5);
        System.out.println("La suma es: " + resultado); */

        /* Coche coche = new Coche();
        Moto moto = new Moto();

        EjecutarAcelerar(coche);
        EjecutarAcelerar(moto); */

        /* var valA = 5;
        var valB = 10;

        suma(valA, valB);
        System.out.println(valA + "\n" + valB); */

        Coche coche = new Coche();
        cocheChanger(coche);
        cocheChanger(coche);

        System.out.println(coche.velocidad);
        factorial(18, 20);
    }

    /* public static int Suma(int operandoA, int operandoB) {
        var suma = operandoA + operandoB;
        return suma;
    } */

    public static void factorial(int a, int b) {
        int temp = a + b;
        System.out.println("A vale: " + a + "\nb vale: " + b + "\ntemp vale: " + temp + "\n");

        if (b >= 90) {
            return;
        }

        // resultado = factorial(numero - 1) * numero;
        factorial(a, temp);
    }

    public static int factorialNR(int numero) {
        int resultado = 1;

        for (int temp = 1; temp <= numero; temp++) {
            resultado = resultado * temp;
        }

        return resultado;
    }

    public static int suma(int A, int B) {
        int resultado = A + B;
        return resultado;
    }

    /* public static void EjecutarAcelerar(Vehiculo vehiculo) {
        vehiculo.Acelerar(15);
    } */

    public static void cocheChanger(Coche coche) {
        coche.velocidad += 50;
    }
}

interface Vehiculo {
    void Acelerar(int cuantaVelocidad);
    void Frenar(int cuantaVelocidad);
}

class Coche implements Vehiculo {
    int velocidad = 0;

    public void Acelerar(int cuantaVelocidad) {
        System.out.println("Coche() -> Acelerar()");
    }

    public void Frenar(int cuantaVelocidad) {
        System.out.println("Coche -> Frenar()");
    }
}

class Moto implements Vehiculo {
    public void Acelerar(int cuantaVelocidad) {
        System.out.println("Moto() -> Acelerar()");
    }

    public void Frenar(int cuantaVelocidad) {
        System.out.println("Moto() -> Frenar()");
    }
}
