import 'package:variables_1/variables_1.dart' as variables_1;

void main(List<String> arguments) {
  // Guardamos nuestro nombre dentro de la variable "nombre"
  var nombre = "David";

  // Guardamos nuestra edad dentro de la variable "edad"
  var edad = 27;
  print("Nombre: " +
      nombre +
      "\nEdad: " +
      edad.toString()); // Imprimimos nuestro nombre y nuestra edad convertida en cadena

  // Imprimimos el tipo de las variables "nombre" y "edad"
  print("\nNombre es de tipo: " +
      nombre.runtimeType.toString() +
      "\nEdad es de tipo: " +
      edad.runtimeType.toString());
}
