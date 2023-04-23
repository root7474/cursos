package org.calculadora;

import java.util.Scanner;

public class Operaciones {
    String nombre;
    
    public Operaciones(String nombre) {
        this.nombre = nombre;
    }

    // Menú de opciones
    public void menu() {
        boolean pass = false;
        Integer cantidad;

        SumaClass calcularSuma = new SumaClass(nombre);
        RestaClass calcularResta = new RestaClass(nombre);
        MultiplicacionClass calcularMultiplicaion = new MultiplicacionClass(nombre);
        DivisionClass calcularDivision = new DivisionClass(nombre);
        PorcentajeClass calcularPorcentaje = new PorcentajeClass(nombre);

        while (pass == false) {
            Integer userDataInt = integerError("\n" + nombre + " Elige una opción:\n" +
                                               "\n1.) Suma." +
                                               "\n2.) Resta." +
                                               "\n3.) Multiplicación." +
                                               "\n4.) División." +
                                               "\n5.) Porcentaje." +
                                               "\n0.) Salir." +
                                               "\n\nOpción: ");
            
            if (userDataInt == 1) {
                cantidad = integerError("\nDigita una cantidad a sumar: ");
                calcularSuma.suma(cantidad);
                System.out.println(calcularSuma);
            } else if (userDataInt == 2) {
                cantidad = integerError("\nDigita una cantidad a restar: ");
                calcularResta.resta(cantidad);
                System.out.println(calcularResta);
            } else if (userDataInt == 3) {
                cantidad = integerError("\nDigita una cantidad a multplicar: ");
                calcularMultiplicaion.multiplicacion(cantidad);
                System.out.println(calcularMultiplicaion);
            } else if (userDataInt == 4) {
                cantidad = integerError("\nDigita una cantidad a dividir: ");

                try {
                    calcularDivision.division(cantidad);
                    System.out.println(calcularDivision);
                } catch (ArithmeticException e) {
                    System.out.println("Error!!!... Division entre cero");
                }
            } else if (userDataInt == 5) {
                calcularPorcentaje.porcentaje();
                System.out.println(calcularPorcentaje);
            } else if (userDataInt == 0) {
                System.out.println("Hasta pronto...");
                pass = true;
            } else {
                System.out.println("Opción desconcocida. Ingresa números del 0 al 5");
            }
        }
    }

    public Integer integerError(String message) {
        boolean pass = false;
        Integer userDataInt = 0;
        Scanner opcionScanner = new Scanner(System.in);

        while (pass == false) {
            try {
                System.out.print(message);
                userDataInt = Integer.parseInt(opcionScanner.next());
                pass = true;
            } catch (NumberFormatException e) {
                System.out.println("Error!!!... No debes ingresar números decimales ni tampocos letras o símbolos especiales");
            }
        }

        return userDataInt;
    }
}
