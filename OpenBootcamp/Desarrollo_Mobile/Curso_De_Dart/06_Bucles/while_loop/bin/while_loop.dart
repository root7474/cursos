import "dart:io";

void main(List<String> arguments) {
  // Máquina de repetición
  print("Dime algo");

  while (true) {
    String ? linea = stdin.readLineSync();
    if (linea.toString().startsWith("#")) continue;
    if (linea == "Fin") break;

    print("Repito: ${linea}");
  }

  print("Terminamos y a dormir");
}
