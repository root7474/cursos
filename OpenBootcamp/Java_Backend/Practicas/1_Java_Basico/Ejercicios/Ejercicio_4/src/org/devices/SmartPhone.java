package org.devices;

import org.smartDevices.SmartDevices; // Importamos a la clase "SmartDevices()"

/**
 * Generamos una clase que guarda los datos de un smart phone
 * Creamos un contructor para la clase
 * Creamos sus atributos de tipo private y los inicializamos dentro del constructor
 * Generamos una función de tipo private
 * Creamos los métodos "get" que permitan leer lo valores de los atributos y de la función de tipo private
 * Retornamos a través de un método "toString()" los valores de cada atributo
 */
public class SmartPhone extends SmartDevices {
    // Creamos los atributos de la clase
    private Double ram;
    private String procesador;
    private Integer nucleosProcesador;
    private Double velocidadProcesador;
    private Double almacenamiento;
    private Boolean dualSim;

    /**
     * Generamos un constructor vacio
     */
    public SmartPhone() {
    }

    /**
     * Generamos otro constructor con sus respectivos parámetros
     * @param marca parámetro de tipo string que indica la marca del fabricante
     * @param modelo parámetro de tipo string que indica el modelo del fabricante
     * @param color parámetro de tipo string que indica el color del dispositivo
     * @param resolucionPantalla parámetro de tipo string que indica la resolución de pantalla del dispositivo
     * @param ram parámetro de tipo Double que indica la cantidad en Giga Bytes de la memoria ram del dispositivo
     * @param procesador parámetro de tipo string que indica la marca y el modelo del procesador
     * @param nucleosProcesador parámetro de tipo entero que indica la cantidad de núcleos del procesador
     * @param velocidadProcesador parámetro de tipo Double que indica la velocidad del procesador en Giga Hertz
     * @param almacenamiento  parámetro de tipo Double que indica el almacenamiento e Giga Bytes del alamacenamiento interno
     * @param dualSim parámetro de tipo Boolean que indica si el dispositivo es compatible con sim dual o no
     */
    public SmartPhone(String marca, String modelo, String color, String resolucionPantalla, Double ram, String procesador, Integer nucleosProcesador, Double velocidadProcesador, Double almacenamiento, Boolean dualSim) {
        super(marca, modelo, color, resolucionPantalla);
        this.ram = ram;
        this.procesador = procesador;
        this.nucleosProcesador = nucleosProcesador;
        this.velocidadProcesador = velocidadProcesador;
        this.almacenamiento = almacenamiento;
        this.dualSim = dualSim;
    }

    // Creamos una función que nos permita saber si el smart phone tiene sim dual
    private String esDualSim() {
        String esDualSim; // Generamos una atributo para esta función

        if (this.dualSim.equals(true)) {
            esDualSim = "Sí"; // Si el atributo "dualSim" es igual a true, imprimimos "Sí"
        } else {
            esDualSim = "No"; // De lo contrario imprimimos "No"
        }

        return esDualSim; // Retornamos el valor del atributo de la función
    }

    // Generamos los métodos que nos permitirán retornar los valores de los atributos de la clase
    public Double getRam() {
        return this.ram; // Retornamos el valor del atributo "ram"
    }

    public String getProcesador() {
        return this.procesador; // Retornamos el valor del atributo "procesador"
    }

    public Integer getNucleosProcesador() {
        return this.nucleosProcesador; // Retornamos el valor del atributo "nucleosProcesador"
    }

    public Double getVelocidadProcesador() {
        return this.velocidadProcesador; // Retornamos el valor del atributo "velocidadProcesador"
    }

    public Double getAlmacenamiento() {
        return this.almacenamiento; // Retornamos el valor del atributo "almacenamiento"
    }

    public String getDualSim() {
        return this.esDualSim(); // Retornamos el valor que devuelve la función "esDualSim()"
    }

    // Generamos un método "toString()" que retorna una cadena con el valor de los atributos de esta clase
    @Override
    public String toString() {
        return "Smart phone:\n" +
               "\nMarca: " + getMarca() + 
               "\nModelo: " + getModelo() +
               "\nColor: " + getColor() +
               "\nRam: " + getRam() + "GB" +
               "\nProcesador: " + getProcesador() +
               "\nNucleos procesador: " + getNucleosProcesador() +
               "\nVelocidad procesador: " + getVelocidadProcesador() + "GHz" +
               "\nAlmacenamiento: " + getAlmacenamiento() + "GB" +
               "\nSim dual: " + getDualSim() +
               "\nPantalla: " + getResolucionPantalla();
    }
}
