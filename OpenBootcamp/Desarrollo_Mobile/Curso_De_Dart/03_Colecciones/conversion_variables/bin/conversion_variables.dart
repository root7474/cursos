import 'package:conversion_variables/conversion_variables.dart'
    as conversion_variables;

void main(List<String> arguments) {
  String numeroString = "100";
  int numeroInt = 200;
  int suma = int.parse(numeroString) + numeroInt;

  print("${numeroString} + ${numeroInt} = ${suma}");

  String a = "Uno";
  String b = "Dos";
  print(a + b);

  double numeroDecimal = 100.504;
  String numeroDecimalString = numeroDecimal.toStringAsFixed(2);
  print("El número decimal convertido a String es: ${numeroDecimalString}");

  var miSet = <int>[numeroInt, int.parse(numeroString)];
  print("Set: ${miSet}");
}
