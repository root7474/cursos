void main(List<String> arguments) {
  // Creamos el mapa
  var miPrimerMapa = {
    "nombre": "David",
    "edad": 27,
    "email": "davidrodriguezbolanos777@hotmail.com",
    "execelente desarrollador": true,
  };

  // Impprimimos el mapa
  print("Mapa: ${miPrimerMapa}");

  // Añadimos información
  miPrimerMapa["ciudad"] = "Pasto";
  print("Mapa: ${miPrimerMapa}");

  // Modificamos información que ya existe
  miPrimerMapa["execelente desarrollador"] = false;
  print("Mapa: ${miPrimerMapa}");
  print("Longitud del mapa: ${miPrimerMapa.length}");

  // Convertir listas en mapas
  var lista = ["David", "Patricia", "Felipe"];
  print("Lista convertida en mapa: ${lista.asMap()}");
}
