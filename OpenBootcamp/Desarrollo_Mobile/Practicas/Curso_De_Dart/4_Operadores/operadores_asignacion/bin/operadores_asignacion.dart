void main(List<String> arguments) {
  var a = 10;
  var b = 20;
  var c;

  c ??= 1;
  print("Valor de c = ${c}");

  c += a;
  print("Valor de c = ${c}");

  c -= a;
  print("Valor de c = ${c}");

  c *= a;
  print("Valor de c = ${c}");

  c /= a;
  print("Valor de c = ${c}");

  c %= a;
  print("Valor de c = ${c}");
}
