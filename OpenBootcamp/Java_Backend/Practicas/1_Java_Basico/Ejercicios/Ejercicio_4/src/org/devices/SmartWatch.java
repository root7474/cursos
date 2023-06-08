package org.devices;

import org.smartDevices.SmartDevices; // Importamos a la clase "SmartDevices()"

/**
 * Generamos una clase que guarda los datos de un smart watch
 * Creamos un contructor para la clase
 * Creamos sus atributos de tipo private y los inicializamos dentro del constructor
 * Generamos una función de tipo private
 * Creamos los métodos "get" que permitan leer lo valores de los atributos y de la función de tipo private
 * Retornamos a través de un string los valores de cada atributo
 */
public class SmartWatch extends SmartDevices {
    // Creamos los atributos de la clase
    private String sensores;
    private String compatibilidad;
    private Boolean resistenciaAgua;

    /**
     * Generamos un constructor vacio
     */
    public SmartWatch() {
    }

    /**
     * Generamos otro constructor con sus respectivos parámetros
     * @param marca parámetro de tipo string que indica la marca del fabricante
     * @param modelo parámetro de tipo string que indica el modelo del fabricante
     * @param color parámetro de tipo string que indica el color del dispositivo
     * @param resolucionPantalla parámetro de tipo string que indica la resolución de pantalla del dispositivo
     * @param sensores parámetro de tipo string que indica las funciones de los sensores del dispositivo
     * @param compatibilidad parámetro de tipo string que indica la compatibilidad con cualquier sistema operativo
     * @param resistenciaAgua parámetro de tipo string que indica si el dispositivo es resitente al agua
     */
    public SmartWatch(String marca, String modelo, String color, String resolucionPantalla, String sensores, String compatibilidad, Boolean resistenciaAgua) {
        super(marca, modelo, color, resolucionPantalla);
        this.sensores = sensores;
        this.compatibilidad = compatibilidad;
        this.resistenciaAgua = resistenciaAgua;
    }

    // Creamos una función que nos permita saber si el smart watch es resistente a la agua
    private String resitencia() {
        String esResistente; // Generamos una atributo para esta función

        if (this.resistenciaAgua.equals(true)) {
            esResistente = "Sí"; // Si el atributo "resistenciaAgua" es igual a true, imprimimos "Sí"
        } else {
            esResistente = "No"; // De lo contrario imprimimos "No"
        }

        return esResistente; // Retornamos el valor del atributo de la función
    }

    // Generamos los métodos que nos permitirán retornar los valores de los atributos de la clase
    public String getSensores() {
        return sensores; // Retornamos el valor del atributo "sensores"
    }

    public String getCompatibilidad() {
        return compatibilidad; // Retornamos el valor del atributo "compatibilidad"
    }

    public String getResistenciaAgua() {
        return resitencia(); // Retornamos el valor que devuelve la función "resitencia()"
    }

    // Generamos un método "toString()" que retorna una cadena con el valor de los atributos de esta clase
    @Override
    public String toString() {
        return "Smart watch:\n" +
               "\nMarca: " + getMarca() + 
               "\nModelo: " + getModelo() +
               "\nColor: " + getColor() +
               "\nSensores: " + getSensores() +
               "\nCompatibilidad: " + getCompatibilidad() +
               "\nResistencia al agua: " + getResistenciaAgua() +
               "\nPantalla: " + getResolucionPantalla();
    }
}
