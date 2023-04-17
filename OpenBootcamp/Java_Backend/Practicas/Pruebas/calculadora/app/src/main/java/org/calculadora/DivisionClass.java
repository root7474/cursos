package org.calculadora;

import javax.lang.model.type.NullType;

public class DivisionClass extends Operaciones {
    Double division = null;

    public DivisionClass (String nombre) {
        super(nombre);
    }

    public void division(int cantidad) throws DivisionFormatError {
        cantidad = cantidad;

        for (int i = 0; i < cantidad; i++) {
            System.out.print("Digita el número " + (i + 1) + ": ");
            numero = Double.parseDouble(numeroScanner.next());
            
            
            if (division == null) {
                division = numero;
            } else {
                if (numero == 0) throw new DivisionFormatError("Error!!!... Division entre cero");
                division = division / numero;
            }
        }
    }

    @Override
    public String toString() {
        return "\nEl resultado de la división es: " + this.division;
    }
}
