// Ejercicio 4
// Autor: David Rodríguez
package org.smartDevices;

// Importamos a las clases "SmartPhone()" y "SmartWatch()"
import org.devices.SmartPhone;
import org.devices.SmartWatch;

/**
 * Clase principal para la ejecución del programa
 */
public class Main {
    public static void main(String[] args) {
        // Creamos una instancia de las clases "SmartPhone()" y "SmartWatch()"
        SmartDevices smartPhone = new SmartPhone("Xiaomi", "Redmi Note 9", "Verde", "2.340 x 1.080 px (19,5:9)", 4.0, "SnapDragon", 6, 15.0, 128.0, true);
        SmartDevices smartWatch = new SmartWatch("Xiaomi", "Redmi Watch 2 Lite", "Negro", "320 x 360 píxeles", "Ritmo cardíaco, saturación de oxígeno en sangre, monitorización sueño", "iOS / Android", true);
        System.out.println(smartPhone + "\n\n" + smartWatch); // Imprimimos por consola el valor de cada uno de sus atributos
    }
}
