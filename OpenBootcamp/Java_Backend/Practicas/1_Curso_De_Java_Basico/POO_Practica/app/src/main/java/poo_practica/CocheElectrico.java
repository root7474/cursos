package app.src.main.java.poo_practica;

public class CocheElectrico extends Coche {
    String motorElectrico;

    public CocheElectrico() {}

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
        Integer calculoAcelerar = cantidad * 2;
        super.acelerar(calculoAcelerar);
    }

    /* @Override
    public String toString() {
        // TODO Auto-generated method stub
        return super.toString();
    } */

    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return "Coche Eléctrico [color=" + color + ", fabricante=" + fabricante + ", modelo=" + modelo + ", peso=" + peso
                + ", largo=" + largo + ", velocidad=" + velocidad + ", motor=" + motorElectrico + "]";
    }
}
