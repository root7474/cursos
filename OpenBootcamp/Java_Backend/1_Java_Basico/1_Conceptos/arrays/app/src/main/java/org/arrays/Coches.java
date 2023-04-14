package org.arrays;

public class Coches {
    String name = "Nombre de coche";

    public Coches() {}

    public Coches(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Coches [name=" + name + "]";
    }
}
