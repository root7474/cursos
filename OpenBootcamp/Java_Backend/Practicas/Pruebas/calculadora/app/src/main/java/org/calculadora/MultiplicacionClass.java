package org.calculadora;

public class MultiplicacionClass extends Operaciones {
    Double multiplicacion = null;

    public MultiplicacionClass(String nombre) {
        super(nombre);
    }

    public void multiplicacion(int cantidad) {
        cantidad = cantidad;

        for (int i = 0; i < cantidad; i++) {
            System.out.print("Digita el número " + (i + 1) + ": ");
            numero = Double.parseDouble(numeroScanner.next());

            if (multiplicacion == null) {
                multiplicacion = numero;
            } else {
                multiplicacion = multiplicacion * numero;
            }
        }
    }

    @Override
    public String toString() {
        return "\nEl resultado de la multiplicación es: " + multiplicacion;
    }
}
