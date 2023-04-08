void main(List<String> arguments) {
  // Definimos el set
  var miPrimerSet = <String>["David", "Patricia", "Felipe"];
  print("Set: ${miPrimerSet}");

  // Agregamos elementos al set
  miPrimerSet.add("Andrés");
  miPrimerSet.add("Gloria");
  print("Set: ${miPrimerSet}");

  // Eliminamos elementos del set
  miPrimerSet.remove(miPrimerSet[4]);
  print("Set: ${miPrimerSet}");

  // Limpiar todo el set
  miPrimerSet.clear();
  print("Set: ${miPrimerSet}");
}
