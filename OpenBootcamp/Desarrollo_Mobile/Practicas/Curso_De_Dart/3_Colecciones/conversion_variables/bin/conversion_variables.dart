void main(List<String> arguments) {
  String numeroString = "100"; // Declaramos una variable de tipo string
  int numeroInt = 50; // Declaramos una variable de tipo int
  int suma = int.parse(numeroString) +
      numeroInt; // Convertimos la variable de tipo string y la sumamos con la variable de tipo int

  // Imprimimos el resultado de la suma
  print("${numeroString} + ${numeroInt} = ${suma}");

  // Concatenar
  String a = "Uno";
  String b = "Dos";
  print(a + b);

  // Función toStringAsFixed(). Convierte un decimal a string de dos decimales
  double numeroDecimal = 100.504;
  print("Número decimal: ${numeroDecimal.toStringAsFixed(2)}");

  // Conertir un string a entero y agregarlo a un set del mismo tipo (entero)
  var miSet = <int>[numeroInt, int.parse(numeroString)];
  print("Set: ${miSet}");
}
