void main(List<String> arguments) {
  int a = 10;
  int b = 25;
  int c = 10;

  var mayor = a > b;
  var menor = a < b;
  var mayorIgual = a >= b;
  var menorIgual = a <= b;
  var mayorIgual2 = a >= c;
  var menorIgual2 = a <= c;

  print("${a} > ${b} = ${mayor}");
  print("${a} < ${b} = ${menor}");
  print("${a} >= ${b} = ${mayorIgual}");
  print("${a} <= ${b} = ${menorIgual}");
  print("${a} >= ${c} = ${mayorIgual2}");
  print("${a} <= ${c} = ${menorIgual2}");
}
