void main(List<String> arguments) {
  var a = 10;
  var b = 25;

  // Suma
  print("${a} + ${b} = ${a + b}");

  // Resta
  print("${a} - ${b} = ${a - b}");

  // Multiplicación
  print("${a} x ${b} = ${a * b}");

  // División
  var division = a / b;
  print("${a} / ${b} = ${division}");
  print(
      "Tipo de la división entre de la división entre ${a} y ${b}: ${division.runtimeType}");

  // Incremento y decremento
  print("Número: ${a}");

  a++;
  print("Número incrementado: ${a}");

  a--;
  print("Número decrementado: ${a}");

  // Resultado división entera
  print("El resultado de la división entera entre ${b} y ${a} es: ${b ~/ a}");

  // Resto de una división
  print("El resto de la divisón entre ${b} ${a} es: ${b % a}");

  // Cambiar el signo
  print("Número negativo: ${-a}");
}
