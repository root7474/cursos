package org.condicionales;

public class IfElseIf {
    public static void main(String[] args) {
        String dia = "Lunes";

        if (dia.equals("Lunes")) {
            System.out.println("Hoy es Lunes");
        } else if (dia.equals("Martes")) {
            System.out.println("Hoy es Martes");
        } else if (dia.equals("Miércoles")) {
            System.out.println("Hoy es Miércoles");
        } else if (dia.equals("Jueves")) {
            System.out.println("Hoy es Jueves");
        } else if (dia.equals("Viernes")) {
            System.out.println("Hoy es Viernes");
        } else if (dia.equals("Sábado")) {
            System.out.println("Hoy es Sábado");
        } else if (dia.equals("Domingo")) {
            System.out.println("Hoy es Domingo");
        } else {
            System.out.println("Día incorrecto");
        }
    }
}
