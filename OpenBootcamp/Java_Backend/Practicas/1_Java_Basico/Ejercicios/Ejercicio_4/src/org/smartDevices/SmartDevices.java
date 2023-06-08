package org.smartDevices;

public abstract class SmartDevices {
    // Creamos los atributos de la clase
    private String marca;
    private String modelo;
    private String color;
    private String resolucionPantalla;

    /**
     * Generamos un constructor vacio
     */
    protected SmartDevices() {
    }

    /**
     * Generamos otro constructor con sus respectivos parámetros
     * @param marca parámetro de tipo string que indica la marca del fabricante
     * @param modelo parámetro de tipo string que indica el modelo del fabricante
     * @param color parámetro de tipo string que indica el color del dispositivo
     * @param resolucionPantalla parámetro de tipo string que indica la resolución de pantalla del dispositivo
     */
    protected SmartDevices(String marca, String modelo, String color, String resolucionPantalla) {
        this.marca = marca;
        this.modelo = modelo;
        this.color = color;
        this.resolucionPantalla = resolucionPantalla;
    }

    // Generamos los métodos que nos permitirán retornar los valores de los atributos de la clase
    public String getMarca() {
        return marca; // Retornamos el valor del atributo "marca"
    }

    public String getModelo() {
        return this.modelo; // Retornamos el valor del atributo "modelo"
    }

    public String getColor() {
        return this.color; // Retornamos el valor del atributo "color"
    }

    public String getResolucionPantalla() {
        return this.resolucionPantalla; // Retornamos el valor del atributo "resolucionPantalla"
    }
}
