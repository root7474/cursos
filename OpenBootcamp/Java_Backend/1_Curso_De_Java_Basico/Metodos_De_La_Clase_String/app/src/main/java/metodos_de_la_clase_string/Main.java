package metodos_de_la_clase_string;

public class Main {
    public static void main(String[] args) {
        // L clase String

        /* 
            lenght()
            startsWith("")
            endsWidth("")
            indexOf("")
            subString(1, 5)
            trim()
            equals()
            compareTo
        */

        String mensaje = "  Hola mundo  ";
        System.out.println(mensaje.length());

        String mensajeMay = mensaje.toUpperCase();
        System.out.println(mensajeMay);

        String mensajeTrim = mensajeMay.trim();
        System.out.println(mensajeTrim);

        String otro = "hola mundo";

        if (mensajeTrim.equalsIgnoreCase(otro)) {
            System.out.println("Verdadero");
        } else {
            System.out.println("Falso");
        }
    }
}
