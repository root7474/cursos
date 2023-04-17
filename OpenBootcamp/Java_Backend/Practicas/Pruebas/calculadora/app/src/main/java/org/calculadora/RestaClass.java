package org.calculadora;

public class RestaClass extends Operaciones {
    Double resta = null;

    public RestaClass(String nombre) {
        super(nombre);
    }

    public void resta(int cantidad) {
        cantidad = cantidad;

        for (int i = 0; i < cantidad; i++) {
            System.out.print("Digita el número " + (i + 1) + ": ");
            numero = Double.parseDouble(numeroScanner.next());

            if (resta == null) {
                resta = numero;
            } else {
                resta = resta - numero;
            }
        }
    }

    @Override
    public String toString() {
        return "\nEl resultado de la resta es: " + resta;
    }
}
