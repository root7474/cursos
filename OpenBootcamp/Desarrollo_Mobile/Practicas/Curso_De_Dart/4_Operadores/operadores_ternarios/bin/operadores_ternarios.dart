import 'package:test/test.dart';

void main(List<String> arguments) {
  var soyDavid = false;
  soyDavid
      ? print("Correcto eres David, puedes entrar")
      : print("No eres David, no puedes pasar");

  var a = 10;
  a >= 10 ? print("${a} >= 10") : print("${a} < 10");

  var b = [1, null, 2];
  b[1] ?? print("b no tiene valor en esa posición");
}
