import 'package:booleanos_5/booleanos_5.dart' as booleanos_5;

void main(List<String> arguments) {
  bool esVerdad_1 = 2 == 1 + 1;
  final esVerdad_2 = "David" == "david";

  print(2.toString() +
      " es igual a " +
      1.toString() +
      " + " +
      1.toString() +
      "?: " +
      esVerdad_1.toString());

  print("David es igual a david?: " + esVerdad_2.toString());
}
