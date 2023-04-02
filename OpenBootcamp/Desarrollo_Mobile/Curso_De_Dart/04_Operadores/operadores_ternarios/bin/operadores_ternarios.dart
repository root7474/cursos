void main(List<String> arguments) {
  var soyLuis = false;
  soyLuis
      ? print("Correcto, eres Luís. Puedes pasar")
      : print("Acceso denegado");

  var a = 10;
  a >= 10
      ? print("${a} es mayor o igual que 10")
      : print("${a} es menor que 10");

  var b = [1, null, 2];
  b[1] ?? print("b no tiene valor en esa posición");
}
