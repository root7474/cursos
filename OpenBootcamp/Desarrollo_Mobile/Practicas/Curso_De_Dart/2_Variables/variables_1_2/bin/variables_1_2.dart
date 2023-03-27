import 'dart:ffi';

import 'package:variables_1_2/variables_1_2.dart' as variables_1_2;

void main(List<String> arguments) {
  // Declaramos variables para los datos del usuario
  String nombre = "David";
  int edad = 27;
  double peso = 55.0;
  double estatura = 1.66;
  bool esIngenieroFullStack = true;

  // Imprimimos los valores de dichas variables por pantalla
  print("Nombre: " +
      nombre +
      "\nEdad: " +
      edad.toString() +
      "\nPeso: " +
      peso.toString() +
      "\nEstatura: " +
      estatura.toString() +
      "\nEs ingeniero full satck?: " +
      esIngenieroFullStack.toString());
}
