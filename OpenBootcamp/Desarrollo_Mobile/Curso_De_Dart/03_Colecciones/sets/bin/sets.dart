import 'package:sets/sets.dart' as sets;

void main(List<String> arguments) {
  var miPrimerSet = <String>["David", "Patricia", "Felipe"];
  print("Mi primer set: ${miPrimerSet}");

  miPrimerSet.add("Gloria");
  miPrimerSet.add("David");
  print("Mi primer set: ${miPrimerSet}");

  print("Nombre: ${miPrimerSet.elementAt(2)}");
  print("Longitud: ${miPrimerSet.length}");

  miPrimerSet.remove(miPrimerSet[4]);
  print("Mi primer set: ${miPrimerSet}");

  miPrimerSet.clear();
  print("Mi primer set: ${miPrimerSet}");
}
