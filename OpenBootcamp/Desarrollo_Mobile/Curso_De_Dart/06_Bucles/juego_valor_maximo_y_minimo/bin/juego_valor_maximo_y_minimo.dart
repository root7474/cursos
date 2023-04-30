import "dart:math";

void main(List<String> arguments) {
  var lista = [3, 41, 12, 73, 2, 20];
  var maximo = 0;
  var minimo;

  // Calcular el valor máximo
  for (var numero in lista) {
    if (maximo < numero) maximo = numero;
    print("Ciclo: $maximo $numero");
  }

  print("El máximo es: $maximo");

  // Calcular el mínimo
  for (var numero in lista) {
    if (minimo == null || minimo > numero) minimo = numero;
    print("Ciclo: $minimo $numero");
  }

  print("El mínimo es: $minimo");
  print("El mínimo es: ${lista.reduce(min)}");
  print("El máximo es: ${lista.reduce(max)}");
}
