package org.java_poo_practica;

public class CocheElectrico extends Coche {
    String motorElectrico;

    public CocheElectrico() {
    }

    public CocheElectrico(String motorElectrico) {
        this.motorElectrico = motorElectrico;
    }

    public CocheElectrico(String color, String fabricante, String modelo, Double peso, Double largo, String motorElectrico) {
        super(color, fabricante, modelo, peso, largo);
        this.motorElectrico = motorElectrico;
    }

    @Override
    public void acelerar(Integer cantidad) {
        // TODO Auto-generated method stub
        Integer cantidadAjustada = cantidad * 2;
        super.acelerar(cantidadAjustada); // Sobreescritura
    }

    @Override
    public String toString() {
        return "Coche eléctrico [color=" + color + ", fabricante=" + fabricante + ", modelo=" + modelo + ", peso=" + peso
                + ", largo=" + largo + ", velocidad=" + velocidad + ", motor=" + motorElectrico + "]";
    }
}
