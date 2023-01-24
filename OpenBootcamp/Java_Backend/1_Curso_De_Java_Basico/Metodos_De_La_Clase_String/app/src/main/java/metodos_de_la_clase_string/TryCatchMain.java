package metodos_de_la_clase_string;

public class TryCatchMain {
    public static void main(String[] args) {
        try {
            int result = 5 / 0;
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        } finally {
            System.out.println("Cierre de recursos");
        }

        System.out.println("Fin");
    }
}
