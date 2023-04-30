void main(List<String> arguments) {
  var gastos = [1.23, 14.5, 300.67, 0.60, 125.5];
  int cuenta = 0;
  double suma = 0;

  // Contar el número de elementos y sumarlos
  for (var gasto in gastos) {
    suma += gasto;
    cuenta++;
  }
  
  print("El número total de gastos es: $cuenta");
  print("El total de gastos es de: ${suma.toStringAsFixed(2)} euros");
}
