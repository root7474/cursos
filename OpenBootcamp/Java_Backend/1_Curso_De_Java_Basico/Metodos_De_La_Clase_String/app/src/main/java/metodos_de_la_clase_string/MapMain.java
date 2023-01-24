package metodos_de_la_clase_string;

import java.util.HashMap;
import java.util.Map;

public class MapMain {
    public static void main(String[] args) {
        Map<String, String> personas = new HashMap<>();

        personas.put("12345678H", "Nombre Apellido 1");
        personas.put("12345678L", "Nombre Apellido 2");
        personas.put("12345678F", "Nombre Apellido 3");

        System.out.println(personas);

        for (String key : personas.keySet()) {
            System.out.println(key);
        }

        for (String value : personas.values()) {
            System.out.println(value);
        }

        for (Map.Entry<String, String> pair : personas.entrySet()) {
            System.out.println(pair.getKey() + " / " + pair.getValue());
        }
    }
}
