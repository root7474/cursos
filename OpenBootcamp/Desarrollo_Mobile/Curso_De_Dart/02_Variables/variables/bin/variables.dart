import 'package:variables/variables.dart' as variables;

void main(List<String> arguments) {
  // Esta variable sirve para guardar el nombre de la persona
  var nombre = "David";

  // Variable edad de tipo entero
  var edad = 27;

  print("Nombre: " + nombre + "\nEdad: " + edad.toString());

  /* 
  Este trozo de código sive para conocer el tipo de variable
  Para ello usamos runtimeType
   */
  print("Nombre es de tipo: " + nombre.runtimeType.toString());
  print("Edad es de tipo: " + edad.runtimeType.toString());
}
