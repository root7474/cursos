void main(List<String> arguments) {
  var soyExcelenteDesarrollador = false;
  print("Soy un excelente desarrollador?: ${!soyExcelenteDesarrollador}");

  var a = 10;
  var b = 25;

  var esVerdad = a > 20 || b > 20;
  print("${a} > 20 o ${b} > 20: ${esVerdad}");

  var esVerdad2 = a > 20 && b > 25;
  print("${a} > 20 y ${b} > 20: ${esVerdad2}");
}
