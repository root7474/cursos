void main(List<String> arguments) {
  var iteraciones = 10;
  // Cuenta hacia arriba
  for (var i = 0; i <= iteraciones; i++) {
    print(i);
  }

  // Cuenta hacia abajo
  for (var i = 0; i <= iteraciones; i++) {
    print(iteraciones - i);
  }

  // Otra forma
  for (var i = 10; i >= 0; i--) {
    print(i);
  }

  var lista = ["David", "Felipe", "Patricia"];

  for (var i = 0; i < lista.length; i++) {
    print("Felíz navidad ${lista[i]}");
  }

  for (var nombre in lista) {
    print("Felíz año nuevo $nombre");
  }
}
