package org.openbootcamp;

public class Main {
    public static void main(String[] args) {
        Persona persona = new Persona();

        persona.setNombre("David");
        persona.setEdad(26);
        persona.setTelefono("(+57) 3167002210");

        System.out.println("\nBienvenido...\n" +
                           "\nNombre: " + persona.getNombre() +
                           "\nEdad: " + persona.getEdad() +
                           "\nTeléfono: " + persona.getTelefono());
    }
}

/**
 * InnerMain
 */
class Persona {
    private int edad;
    private String nombre;
    private String telefono;

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }
}
