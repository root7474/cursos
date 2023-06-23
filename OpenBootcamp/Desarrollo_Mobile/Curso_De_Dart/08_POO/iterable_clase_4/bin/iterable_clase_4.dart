void main(List<String> arguments) {
  Iterable<int> iterable = [1, 2, 3];
  List<int> listaEnteros = [1, 2, 3];

  listaEnteros[1];
  iterable.elementAt(1);

  Iterable<String> alimentos = ["Tomate", "Carne", "Lechuga"];

  for (String alimento in alimentos) print(alimento);
  // alimentos[alimentos.length]; // Error
  // alimentos[0]; // Error

  print("El primer alimento es: ${alimentos.first}.");
  print("El último alimento es: ${alimentos.last}.");

  var elementoEncontrado1 = alimentos.firstWhere((element) => element.startsWith("C"));
  print(elementoEncontrado1);

  var elementoEncontrado2 = alimentos.firstWhere((element) {
    return element.startsWith("C");
  });

  print(elementoEncontrado2);

  var elementoEncontrado3 = alimentos.firstWhere((element) => element.startsWith("W"),
                                                 orElse: () => "No lo hay");
  
  print(elementoEncontrado3);

  var elementoSingle = alimentos.singleWhere((element) => element.contains('g') && element.startsWith('L'));
  print(elementoSingle);

  var variableEvery = alimentos.every((element) => element.length > 10);
  print(variableEvery);

  var variableAny = alimentos.any((element) => element.length > 6);
  print(variableAny);

  Iterable<User> users = [User(14, "David"), User(19, "Andrés")];
  var todosMayoresDe13 = users.every((user) => user.edad > 13);
  var mayor18 = users.any((user) => user.edad > 18);

  print(todosMayoresDe13);
  print(mayor18);
}

class User {
  var edad;
  var name;

  User(this.edad, this.name);
}
