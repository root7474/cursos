package org.arrays;

import java.util.ArrayList;
import java.util.List;

public class LisatasMain {
    public static void main(String[] args) {
        List<String> nombres = new ArrayList<>();
        
        nombres.add("Nombre 1");
        nombres.add("Nombre 2");
        nombres.add("Nombre 3");
        nombres.add("Nombre 4");

        System.out.println(nombres);

        for(String nombre : nombres) System.out.println(nombre);
    
        List<Coches> coches = new ArrayList<>();

        coches.add(new Coches("Honda Civic"));
        coches.add(new Coches("Alfa Romeo"));
        coches.add(new Coches("Ford Mondeo"));

        System.out.println(coches);

        for(Coches coche : coches) System.out.println(coche);
    }
}
