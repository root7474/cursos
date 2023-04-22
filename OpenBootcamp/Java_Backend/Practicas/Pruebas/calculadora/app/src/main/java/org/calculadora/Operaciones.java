package org.calculadora;

import java.util.Scanner;

public class Operaciones {
    String nombre;
    Integer userDataInt;
    Scanner opcionScanner = new Scanner(System.in);
    Scanner cantidadScanner = new Scanner(System.in);
    
    public Operaciones(String nombre) {
        this.nombre = nombre;
    }

    // Menú de opciones
    public void menu() {
        boolean pass = false;

        SumaClass calcularSuma = new SumaClass(nombre);
        RestaClass calcularResta = new RestaClass(nombre);
        MultiplicacionClass calcularMultiplicaion = new MultiplicacionClass(nombre);
        DivisionClass calcularDivision = new DivisionClass(nombre);
        PorcentajeClass calcularPorcentaje = new PorcentajeClass(nombre);

        while (pass == false) {
            integerError("\n" + nombre + " Elige una opción:\n" +
                             "\n1.) Suma." +
                             "\n2.) Resta." +
                             "\n3.) Multiplicación." +
                             "\n4.) División." +
                             "\n5.) Porcentaje." +
                             "\n0.) Salir." +
                             "\n\nOpción: ");
            
            if (userDataInt == 1) {
                integerError("\nDigita una cantidad a sumar: ");
                calcularSuma.suma(userDataInt);
                System.out.println(calcularSuma);
            } else if (userDataInt == 2) {
                integerError("\nDigita una cantidad a restar: ");
                calcularResta.resta(userDataInt);
                System.out.println(calcularResta);
            } else if (userDataInt == 3) {
                integerError("\nDigita una cantidad a multplicar: ");
                calcularMultiplicaion.multiplicacion(userDataInt);
                System.out.println(calcularMultiplicaion);
            } else if (userDataInt == 4) {
                integerError("\nDigita una cantidad a dividir: ");

                try {
                    calcularDivision.division(userDataInt);
                    System.out.println(calcularDivision);
                } catch (ArithmeticException e) {
                    e.printStackTrace();
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

    private void integerError(String message) {
        boolean pass = false;
        
        while (pass == false) {
            try {
                System.out.print(message);
                userDataInt = Integer.parseInt(opcionScanner.next());
                pass = true;
            } catch (NumberFormatException e) {
                System.out.println("Error!!!... No debes ingresar números decimales ni tampocos letras o símbolos especiales");
            }
        }
    }
}
