package metodos_de_la_clase_string_practica;

import java.util.ArrayList;
import java.util.List;

public class ListMain {
    public static void main(String[] args) {
        List<String> nombres = new ArrayList<>();

        nombres.add("1.) David");
        nombres.add("2.) Felipe");
        nombres.add("3.) Patricia");

        System.out.println("\n" + nombres);
        System.out.println();

        for (String nombre : nombres) {
            System.out.println(nombre);
        }

        System.out.println();
        List<Coche> coches = new ArrayList<>();

        coches.add(new Coche("Nissan"));
        coches.add(new Coche("Ford"));
        coches.add(new Coche("Buggaty"));

        System.out.println(coches);
        System.out.println();

        for (Coche coche : coches) {
            System.out.println(coche);
        }
    }
}
