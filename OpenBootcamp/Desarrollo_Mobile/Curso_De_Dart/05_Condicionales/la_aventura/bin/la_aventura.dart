import "dart:io";

void main(List<String> arguments) {
  int opcion;
  String nombre;

  print("Hola, ¿Cómo te llamas?: ");
  nombre = stdin.readLineSync()!;

  print("\nVas andando por la carretera y esta llega a su fin, tienes dos opciones:\n" +
        "\n1.) Ir a la derecha." +
        "\n2.) Ir a la izquierda." +
        "\n\nOpción: ");

  opcion = int.parse(stdin.readLineSync()!);

  switch (opcion) {
    case 1:
      print("\nTe encuentras en un rí\no y puedes elegir entre estas dos opciones:\n" +
            "\n1.) Nadar." +
            "\n2.) Andar hasta encontrar un puente." +
            "\n\nOpción: ");

      opcion = int.parse(stdin.readLineSync()!);

      if (opcion == 1) {
        print("\nMientras nadabas, apareció un cocodrilo que te comió en menos delo que canta un gallo.");
      } else if (opcion == 2) {
        print("\nAnduviste durante muchos días y te quedaste sin comida, finalmente tu cuerpo se desvaneció.");
      } else {
        print("\nOpción no valida, has perdido.");
      }

      break;

    case 2:
      print("\nTras un paseo, te encuentras un puente. ¿Qué quieres hacer?:\n" +
            "\n1.) Cruzar el puente." +
            "\n2.) Darle la vuelta al puente." +
            "\n\nOpción");

      opcion = int.parse(stdin.readLineSync()!);

      switch (opcion) {
        case 1:
          print("\nTras cruzarlo, te encuentras a un  extraño. ¿Quieres hablar con él?:\n" +
                "\n1.) Sí." +
                "\n2.) No." +
                "\n\nOpción: ");

          opcion = int.parse(stdin.readLineSync()!);

          if (opcion == 1) {
            print("\nEl hombre decide regalarte oro. ¡Has ganado!.");
          } else if (opcion == 2) {
            print("\nEl hombre estaba regalando oro, has perdido.");
          } else {
            print("\nOpción no valida, has perdido.");
          }

          break;

        case 2:
          print("\nDas la vuelta y eliges ahora el camino de la derecha, llegas a un río y da igual lo que elijas porque vas a morir.");
          break;

        default:
          print("\nOpción no valida, has perdido.");
          break;
      }
      break;

    default:
      print("\nOpción no valida, has perdido.");
      break;
  }
}
