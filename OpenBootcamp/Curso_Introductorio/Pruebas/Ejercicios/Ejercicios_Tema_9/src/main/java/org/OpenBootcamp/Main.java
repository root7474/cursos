package org.OpenBootcamp;

public class Main {
    public static void main(String[] args) {
        // Creamos los objetos de la clase Cliente y de la clase Trabajador
        Cliente cliente = new Cliente();
        Trabajador trabajador = new Trabajador();
        
        // Seteamos los datos de la clase Cliente
        cliente.setNombre("David");
        cliente.setEdad(26);
        cliente.setTelefono("+57 316-700-2210");
        cliente.setCredito("$2.000.000 COP");

        // Seteamos los datos de la clase Trabajador
        trabajador.setNombre("Andrés");
        trabajador.setEdad(27);
        trabajador.setTelefono("+57 317-548-9359");
        trabajador.setSalario("$3.500.000 COP");

        // Imprimimos en pantalla los datos de la clase Cliente
        System.out.println("Cliente.\n" + "\nNombre: " + cliente.getNombre() +
                           "\nEdad: " + cliente.getEdad() +
                           "\nTelefono: " + cliente.getTelefono() +
                           "\nCredito: " + cliente.getCredito());

        // Imprimimos en pantalla los datos de la clase Trabajador
        System.out.println("\nTrabajador.\n" + "\nNombre: " + trabajador.getNombre() +
                           "\nEdad: " + trabajador.getEdad() +
                           "\nTelefono: " + trabajador.getTelefono() +
                           "\nSalario: " + trabajador.getSalario());
    }
}

class Persona {
    // Generamos los atributos de la clase Persona 
    int edad;
    String nombre;
    String telefono;

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

class Cliente extends Persona {
    // Heredamos los atributos  de la clase Persona y
    // Agregamos atributos extra para la clase Cliente
    String credito;

    public String getCredito() {
        return credito;
    }

    public void setCredito(String credito) {
        this.credito = credito;
    }
}

class Trabajador extends Persona {
    // Heredamos los atributos  de la clase Persona y
    // Agregamos atributos extra para la clase Trabajador
    String salario;

    public String getSalario() {
        return salario;
    }

    public void setSalario(String salario) {
        this.salario = salario;
    }
}
