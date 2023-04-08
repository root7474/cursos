void main(List<String> arguments) {
  var soyDesarrollador = false;
  print("Soy desarrollador?: ${soyDesarrollador}");

  var a = 10;
  var b = 25;

  // && and, || or, ! not
  var esVerdad = a > 20 || b > 20;
  print("${a} > 20 o ${b} > 20: ${esVerdad}");

  var esVerdad_2 = a > 20 && b > 25;
  print("${a} > 20 y ${b} > 25: ${esVerdad_2}");

  var esVerdad_3 = !esVerdad_2;
  print("${a} > 20 y ${b} > 25: ${esVerdad_3}");
}
