package org.calculadora;

import java.util.Scanner;

public class OperacionesCalculos implements Operaciones {
    Scanner numeroScanner = new Scanner(System.in);
    Scanner opcionScanner = new Scanner(System.in);
    Scanner cantidadScanner = new Scanner(System.in);

        
    String nombre;
    int opcion;
    int cantidad;
    double numero;

    public OperacionesCalculos(String nombre) {
        this.nombre = nombre;
    }

    public void suma(int cantidad) {
        this.cantidad = cantidad;
        double suma = 0;

        for(int i = 0; i < this.cantidad; i++) {
            System.out.print("Digita el número " + (i + 1) + ": ");
            numero = numeroScanner.nextDouble();

            if (suma == 0) {
                suma = numero;
            } else {
                suma = suma + numero;
            }
        }

        System.out.println("El resultado de la suma es: " + suma);
    }

    public void resta(int cantidad) {
        this.cantidad = cantidad;
        double resta = 0;

        for(int i = 0; i < this.cantidad; i++) {
            System.out.print("Digita el número " + (i + 1) + ": ");
            numero = numeroScanner.nextDouble();

            if (resta == 0) {
                resta = numero;
            } else {
                resta = resta - numero;
            }
        }

        System.out.println("El resultado de la resta es: " + resta);
    }

    public void multiplicacion(int cantidad) {
        this.cantidad = cantidad;
        double multiplicacion = 0;

        for(int i = 0; i < this.cantidad; i++) {
            System.out.print("Digita el número " + (i + 1) + ": ");
            numero = numeroScanner.nextDouble();

            if (multiplicacion == 0) {
                multiplicacion = numero;
            } else {
                multiplicacion = multiplicacion * numero;
            }
        }

        System.out.println("El resultado de la multiplicación es: " + multiplicacion);
    }

    public void division(int cantidad) {
        this.cantidad = cantidad;
        double division = 0;

        for(int i = 0; i < this.cantidad; i++) {
            System.out.print("Digita el número " + (i + 1) + ": ");
            numero = numeroScanner.nextDouble();

            if (division == 0) {
                division = numero;
            } else {
                division = division / numero;
            }
        }

        System.out.println("El resultado de la división es: " + division);
    }

    public void porcentaje(double numero) {
        double porcentaje = numero / 100;
        System.out.println("El resultado de la suma es: " + porcentaje);
    }

    public void menu() {
        while(true) {
            System.out.print(nombre + " Elige una opción: " +
                             "\n1.) Suma." +
                             "\n2.) Resta." +
                             "\n3.) Multiplicación." +
                             "\n4.) División." +
                             "\n5.) Porcentaje." +
                             "\n0.) Salir." +
                             "\n\nOpción: ");

            opcion = opcionScanner.nextInt();

            if (opcion == 1) {
                System.out.print("Digita una cantidad a sumar: ");
                this.cantidad = cantidadScanner.nextInt();
                this.suma(cantidad);
            } else if (opcion == 2) {
                System.out.print("Digita una cantidad a restar: ");
                this.cantidad = cantidadScanner.nextInt();
                this.resta(cantidad);
            } else if (opcion == 3) {
                System.out.print("Digita una cantidad a multplicar: ");
                this.cantidad = cantidadScanner.nextInt();
                this.multiplicacion(cantidad);
            } else if (opcion == 4) {
                System.out.print("Digita una cantidad a dividir: ");
                this.cantidad = cantidadScanner.nextInt();
                this.division(cantidad);
            } else if (opcion == 5) {
                System.out.print("Digita un número para calcular su porcentaje: ");
                this.numero = numeroScanner.nextDouble();
                this.porcentaje(numero);
            } else if (opcion == 0) {
                System.out.println("Hasta pronto...");
                break;
            } else {
                System.out.println("Error!!!... Opción desconcocida");
            }
        }
    }
}
