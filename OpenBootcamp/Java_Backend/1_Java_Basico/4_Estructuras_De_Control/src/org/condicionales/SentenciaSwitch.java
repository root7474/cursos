

public class SentenciaSwitch {
    public static void main(String[] args) {
        String dia = "Lunes";

        switch (dia) {
            case "Lunes":
                System.out.println("Hoy es Lunes");
                break;

            case "Martes":
                System.out.println("Hoy es Martes");
                break;

            case "Miércoles":
                System.out.println("Hoy es Miércoles");
                break;

            case "Jueves":
                System.out.println("Hoy es Jueves");
                break;

            case "Viernes":
                System.out.println("Hoy es Viernes");
                break;
            
            case "Sabado":
                System.out.println("Hoy es Sabado");
                break;

            case "Domingo":
                System.out.println("Hoy es Domingo");
                break;

            default:
                System.out.println("Día incorrecto");
                break;
        }
    }
}
