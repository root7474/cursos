package org.java_poo;

public class CocheElectrico extends Coche {
    String motorElectrico;

    public CocheElectrico() {

    }

    public CocheElectrico(String motorElectrico) {

    }

    // Método super()
    public CocheElectrico(String color, String fabricante, String modelo, Double peso, Double largo, String motorElectrico) {
        super(color, fabricante, modelo, peso, largo);
        this.motorElectrico = motorElectrico;
    }

    @Override
    public void acelerar(Integer cantidad) {
        Integer cantidadAjustada = cantidad * 2;
        super.acelerar(cantidadAjustada); // Sobreescritura
    }

    @Override
    public String toString() {
        return "Coche [" + 
                "color=" + color + 
                ", fabricante=" + fabricante + 
                ", modelo=" + modelo + 
                ", peso=" + peso + 
                ", largo=" + largo + 
                ", velocidad=" + velocidad + 
                ", motorElectrico=" + motorElectrico + 
                "]";
    }
}
