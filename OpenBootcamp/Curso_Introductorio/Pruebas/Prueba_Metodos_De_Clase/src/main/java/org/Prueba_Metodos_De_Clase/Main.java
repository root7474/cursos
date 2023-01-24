package org.Prueba_Metodos_De_Clase;

public class Main {
    public static void main(String[] args) {
        /* Coche coche = new Coche();
        coche.Acelerar(50);

        suma(50, 20); */

        /* Coche coche = new Coche();
        Moto moto = new Moto();

        EjecutarAcelerar(coche);
        EjecutarAcelerar(moto); */

        /* int valA = 50;
        int valB = 20;

        Suma(valA, valB);
        System.out.println("\nNúmero 1: " + valA + "\nNúmero 2: " + valB); */

        Coche coche = new Coche();
        
        CocheChanger(coche);
        System.out.println("Velocidad actual: " + coche.velocidad);
        CocheChanger(coche);
        System.out.println("Velocidad actual: " + coche.velocidad);

        System.out.println("\nFactorial recursivo");
        Factorial(17, 20);
        System.out.println("\nFactorial no recursivo");
        FactorialNR(17);
    }

    /* public static int suma(int operandoA, int operandoB) {
        int resultado = operandoA + operandoB;
        System.out.println("El resultado de la suma entre " + operandoA + " + " + operandoB + " es: " + resultado);
        return resultado;
    } */

    /* public static void EjecutarAcelerar(Vehiculo vehiculo) {
        vehiculo.Acelerar(15);
    } */

    /* public static int Suma(int a, int b) {
        int resultado = a + b;
        System.out.println("El resultado de la suma entre " + a + " + " + b + " es: " + resultado);
        return resultado;
    } */

    public static void CocheChanger(Coche coche) {
        coche.velocidad += 50;
    }

    /* public static int Factorial(int numero) {
        int resultado;

        if (numero == 1) {
            return 1;
        }

        resultado = Factorial(numero - 1) * numero;
        System.out.println("El factorial de " + numero + " es: " + resultado);
        
        return resultado;
    } */

    public static void Factorial(int  a, int b) {
        int temp = a + b;
        System.out.println("a vale: " + a + " | b vale: " + b + " | temp vale: " + temp);

        if (b >= 90) {
            return;
        }

        Factorial(a, temp);
    }

    public static int FactorialNR(int numero) {
        int resultado = 1;

        for (int temp = 1; temp <= numero; temp++) {
            resultado = resultado * temp;
        }

        System.out.println("El factorial de " + numero + " es: " + resultado);
        return resultado;
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
        System.out.println("Coche() -> Frenar()");
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
