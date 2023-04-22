package org.listas_y_mapas_practica;

import java.util.HashMap;
import java.util.Map;

public class MapMain {
    public static void main(String[] args) {
        Map<String, String> personas = new HashMap<>();

        personas.put("123456", "Nombre Apellido 1");
        personas.put("123457", "Nombre Apellido 2");
        personas.put("123458", "Nombre Apellido 3");
        System.out.println(personas);

        for (String key : personas.keySet()) System.out.println(key);
        for (String value : personas.values()) System.out.println(value);
        for (Map.Entry<String, String> pair : personas.entrySet()) System.out.println(pair.getKey() + ": " + pair.getValue());
    }
}
