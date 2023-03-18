import 'package:strings/strings.dart' as strings;

void main(List<String> arguments) {
  String uno = "Uno";
  String dos = "Dos";

  String tres = '''
  Uno
  Dos
  Tres''';

  // Métodos para convertir números en string
  // toString()
  int cuatro = 4;
  String cuatroString = cuatro.toString();

  /* print(cuatro.runtimeType);
  print(cuatroString.runtimeType);
  print(cuatroString); */

  double peso = 55.6945;
  String pesoString = peso.toStringAsFixed(2);
  // print(pesoString);

  // contains()
  var refran = "En Abril aguas mil";
  // print(refran.contains("aguas"));

  // split()
  var email = "davidrodriguezbolanos777@hotmail.com";
  // print("El dominio de la dirección es: " + email.split("@")[1]);

  // startswith()
  // print(refran.startsWith("En"));

  // endswith()
  // print(refran.endsWith("mil"));

  // indexof()
  // print(email.indexOf('@'));

  // substring()
  print(email.substring(24 + 1, email.indexOf('.')));
}
