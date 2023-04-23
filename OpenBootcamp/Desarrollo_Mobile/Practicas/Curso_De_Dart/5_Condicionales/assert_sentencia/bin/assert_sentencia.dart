void main(List<String> arguments) {
  int edad = 19;

  print("Inicio del programa");
  assert(true, "Hay fallo en la tercera línea");
  assert(edad >= 20, "La edad es $edad");

  if (edad >= 20) print("Aún no es starde para programar en Dart");
  print("Fin del programa");
}
