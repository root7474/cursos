void main(List<String> arguments) {
  var miPrimerLista = [10, 4];
  var miSegundaLista = ["David", "Patricia", "Felipe"];

  var listaDeListas = [
    miPrimerLista,
    miSegundaLista,
    [12.5, 16.3]
  ];

  // Acceder a un elemento de la lista
  /* var miNombre = miSegundaLista[0];
  print("Mi nombre es: ${miNombre}");

  // Tamño de una lista
  var size = listaDeListas.length;
  print("Tamaño de la lista: ${size}");

  // Acceder al elemento de una sublista
  var accediendo = listaDeListas[1][0];
  print("Nombre: ${accediendo}"); */

  // Listas fijas
  var listaFija = List.filled(4, '', growable: false);

  listaFija[0] = "David";
  listaFija[1] = miSegundaLista[1];
  // listaFija.add("Hola"); // Error, no se puede añadir más elementos a una lista fija

  print(listaFija);
  print("Tamaño actual de mi segunda lista: ${miSegundaLista.length}");

  // Función add()
  miSegundaLista.add("Hola");
  print(miSegundaLista);
  print("Tamaño actual de mi segunda lista: ${miSegundaLista.length}");

  // Acceder al último elemento de la lista
  print("Último elemento de mi segunda lista: ${miSegundaLista.last}");
  print(
      "Último elemento de mi segunda lista: ${miSegundaLista[miSegundaLista.length - 1]}");

  // Imprimir listas desde el último elemento
  print("Mi segunda lista al revés: ${miSegundaLista.reversed}");
}
