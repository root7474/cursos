import "dart:io";

void main(List<String> arguments) {
  var quiereJugar;
  var puntuacion;
  var respuesta;

  print("Quieres jugar a un juego?:" +
        "\n1.) Sí." +
        "\n2.) No.");

  quiereJugar = int.parse(stdin.readLineSync()!);

  if (quiereJugar == 2) {
    exit(0);
  }

  print("Juguemos :D");
  puntuacion = 0;

  print("Qué significana las siglas \"CPU\"?:");
  respuesta = stdin.readLineSync();

  if (respuesta.toLowerCase() == "control process unit") {
    print("Correcto");
    puntuacion++;
  } else {
    print("Incorrecto");
  }

  print("Qué significana las siglas \"RAM\"?:");
  respuesta = stdin.readLineSync();

  if (respuesta.toLowerCase() == "random access memory") {
    print("Correcto");
    puntuacion++;
  } else {
    print("Incorrecto");
  }

  print("Qué significana las siglas \"GPU\"?:");
  respuesta = stdin.readLineSync();

  if (respuesta.toLowerCase() == "graphics processing unit") {
    print("Correcto");
    puntuacion++;
  } else {
    print("Incorrecto");
  }

  print("Qué significana las siglas \"PSU\"?:");
  respuesta = stdin.readLineSync();

  if (respuesta.toLowerCase() == "power suply") {
    print("Correcto");
    puntuacion++;
  } else {
    print("Incorrecto");
  }

  print("\nHas obtenido $puntuacion respuestas correctas" +
        "\nTu puntuación es de ${puntuacion / 4 * 100}%");
}
