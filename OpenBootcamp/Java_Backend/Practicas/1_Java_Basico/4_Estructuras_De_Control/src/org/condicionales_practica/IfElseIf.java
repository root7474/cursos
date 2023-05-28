package org.condicionales_practica;

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
        } else if (dia.equals("Sabado")) {
            System.out.println("Hoy es Sabado");
        } else {
            System.out.println("Día incorrecto");
        }
    }
}
