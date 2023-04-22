package org.java_poo_practica;

public class CocheHibrido extends Coche {
    String motorHibrido;

    public CocheHibrido() {
    }

    public CocheHibrido(String motorHibrido) {
        this.motorHibrido = motorHibrido;
    }

    public CocheHibrido(String color, String fabricante, String modelo, Double peso, Double largo, String motorHibrido) {
        super(color, fabricante, modelo, peso, largo);
        this.motorHibrido = motorHibrido;
    }

    @Override
    public void acelerar(Integer cantidad) {
        // TODO Auto-generated method stub
        Integer cantidadAjustada = cantidad * 2;
        super.acelerar(cantidadAjustada);
    }
    
    @Override
    public String toString() {
        return "Coche hibrido [color=" + color + ", fabricante=" + fabricante + ", modelo=" + modelo + ", peso=" + peso
                + ", largo=" + largo + ", velocidad=" + velocidad + ", motor=" + motorHibrido + "]";
    }
}
