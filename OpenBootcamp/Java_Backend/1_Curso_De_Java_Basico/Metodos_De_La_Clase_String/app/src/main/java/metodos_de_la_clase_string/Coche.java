package metodos_de_la_clase_string;

public class Coche {
    String name;

    public Coche(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Coche [name=" + name + "]";
    }
}
