package org.calculadora;

import java.util.Scanner;

import javax.lang.model.type.NullType;

public class Operaciones {
    String nombre;
    Double numero;
    boolean pass = false;
    int opcion;
    int cantidad;

    Scanner opcionScanner = new Scanner(System.in);
    Scanner cantidadScanner = new Scanner(System.in);
    Scanner numeroScanner = new Scanner(System.in);
    
    public Operaciones(String nombre) {
        this.nombre = nombre;
    }

    // Menú de opciones
    public void menu() {

        SumaClass calcularSuma = new SumaClass(nombre);
        RestaClass calcularResta = new RestaClass(nombre);
        MultiplicacionClass calcularMultiplicaion = new MultiplicacionClass(nombre);
        DivisionClass calcularDivision = new DivisionClass(nombre);
        PorcentajeClass calcularPorcentaje = new PorcentajeClass(nombre);

        while (pass == false) {
            System.out.print("\n" + nombre + " Elige una opción:\n" +
                             "\n1.) Suma." +
                             "\n2.) Resta." +
                             "\n3.) Multiplicación." +
                             "\n4.) División." +
                             "\n5.) Porcentaje." +
                             "\n0.) Salir." +
                             "\n\nOpción: ");

            try {
                opcion = Integer.parseInt(opcionScanner.next());

                if (opcion == 1) {
                    System.out.print("\nDigita una cantidad a sumar: ");
                    cantidad = Integer.parseInt(cantidadScanner.next());
                    calcularSuma.suma(cantidad);
                    System.out.println(calcularSuma);
                } else if (opcion == 2) {
                    System.out.print("\nDigita una cantidad a restar: ");
                    cantidad = Integer.parseInt(cantidadScanner.next());
                    calcularResta.resta(cantidad);
                    System.out.println(calcularResta);
                } else if (opcion == 3) {
                    System.out.print("\nDigita una cantidad a multplicar: ");
                    cantidad = Integer.parseInt(cantidadScanner.next());
                    calcularMultiplicaion.multiplicacion(cantidad);
                    System.out.println(calcularMultiplicaion);
                } else if (opcion == 4) {
                    System.out.print("\nDigita una cantidad a dividir: ");
                    cantidad = Integer.parseInt(cantidadScanner.next());

                    try {
                        calcularDivision.division(cantidad);
                        System.out.println(calcularDivision);
                    } catch (ArithmeticException e) {
                        // TODO Auto-generated catch block
                        e.printStackTrace();
                    }
                } else if (opcion == 5) {
                    System.out.print("\nDigita un número para calcular su porcentaje: ");
                    numero = Double.parseDouble(numeroScanner.next());
                    calcularPorcentaje.porcentaje(numero);
                    System.out.println(calcularPorcentaje);
                } else if (opcion == 0) {
                    System.out.println("Hasta pronto...");
                    pass = true;
                } else {
                    System.out.println("Error!!!... Opción desconcocida");
                }
            } catch (NumberFormatException e) {
                System.out.println("Error: Solo debe ingresar números");
                continue;
            }
        }
    }
}
