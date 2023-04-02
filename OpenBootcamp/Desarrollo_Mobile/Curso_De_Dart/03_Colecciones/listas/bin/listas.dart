import 'package:listas/listas.dart' as listas;

void main(List<String> arguments) {
  var miPrimeraLista = [10, 14];
  var miSegundaLista = ["Luís", "António", "Lucia"];

  var listaDeListas = [
    miPrimeraLista,
    miSegundaLista,
    [12.5, 16.3]
  ];

  /* var miNombre = miSegundaLista[0];
  print(miNombre); */

  /* var size = listaDeListas.length;
  print(size); */

  /* var accediendo = listaDeListas[1][0];
  print(accediendo); */

  var listaFija = List.filled(4, '', growable: false);

  listaFija[0] = "Luís";
  listaFija[1] = miSegundaLista[1];
  // listaFija.add("Hola"); // Error, no se puede añadir más elementos a una lista fija

  print(listaFija);
  print("Tamaño actual de mi segunda lista: ${miSegundaLista.length}");

  miSegundaLista.add("Hola");
  print(miSegundaLista);
  print("Tamaño actual de mi segunda lista: ${miSegundaLista.length}");
  print("Último elemento de mi segunda lista: ${miSegundaLista.last}");
  print(
      "Último elemento de mi segunda lista: ${miSegundaLista[miSegundaLista.length - 1]}");
  print(miSegundaLista.reversed);
}
