void main(List<String> arguments) {
  int a = 10;
  int b = 25;

  // suma
  print("${a} + ${b} = ${a + b}");

  // Resta
  print("${a} - ${b} = ${a - b}");

  // Multiplicación
  print("${a} X ${b} = ${a * b}");

  // División
  var division = a / b;
  print("${a} / ${b} = ${division}");
  print("Tipo de la división entre ${a} y ${b}: ${division.runtimeType}");

  // Incremento y decremento
  print(a);

  a++;
  print(a);

  a--;
  print(a);

  // Resultado división entera
  print("El resultado de la división entera entre ${b} y ${a} es: ${b ~/ a}");

  // Resto de una división
  print("El resto de la divisón entre ${b} y ${a} es: ${b % a}");

  // Cambiar el signo
  print("Número negativo: ${-a}");
}
