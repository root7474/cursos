import 'package:strings_2/strings_2.dart' as strings_2;

void main(List<String> arguments) {
  String uno = "Uno";
  String dos = "Dos";
  String tres = '''
Uno
Dos
Tres
''';

  // Métodos para convertir números en Strings
  // toString()
  int cuatro = 4;
  String cuatroString = cuatro.toString();
  // print("Número: " + cuatroString);

  // Imprimimos el tipo de las variables "cuatro" y "cuatroString"
  /* print("Número tipo int: " +
      cuatro.runtimeType.toString() +
      "\nNúmero tipo String: " +
      cuatroString.runtimeType.toString()); */

  // toStringAsFixed()
  double peso = 55.1234;
  String pesoString = peso.toStringAsFixed(
      2); // Convierte un número double a String de dos decimales
  // print("Peso: " + pesoString);

  // Contains
  var refran = "En Abril, aguas mil";
  // print(refran.contains("aguas"));

  // split()
  var email = "rodriguezbolanosdavid20@gmail.com";
  // print("Eldominio de la dirección es: " + email.split("@")[1]);

  // startsWith()
  // print(refran.startsWith("En"));

  // endsWith()
  // print(refran.endsWith("mil"));

  // indexOf()
  // print(email.indexOf("da"));

  // substring()
  print(email.substring(email.indexOf("da"), email.indexOf("2")));
}
