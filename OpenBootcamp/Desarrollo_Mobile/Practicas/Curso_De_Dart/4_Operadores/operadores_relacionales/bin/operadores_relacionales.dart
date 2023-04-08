void main(List<String> arguments) {
  var a = 10;
  var b = 25;
  var c = 10;

  var mayor = a > b;
  var menor = a < b;
  var mayorIgual = a >= b;
  var menorIgual = a <= b;
  var mayorIgual_2 = a >= c;
  var menorIgual_2 = a <= c;

  print("${a} > ${b} = ${mayor}");
  print("${a} < ${b} = ${menor}");
  print("${a} >= ${b} = ${mayorIgual}");
  print("${a} <= ${b} = ${menorIgual}");
  print("${a} >= ${c} = ${mayorIgual_2}");
  print("${a} <= ${c} = ${menorIgual_2}");
}
