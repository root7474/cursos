import 'package:mapas/mapas.dart' as mapas;

void main(List<String> arguments) {
  var miPrimerMapa = {
    "nombre": "David",
    "edad": "27",
    "email": "davidrodriguezbolanos777@hotmail.com",
    "excelenteDesarrollador": true,
  };

  print(miPrimerMapa);

  // Añadimos información
  miPrimerMapa["ciudad"] = "Pasto";

  // Modificamos información que ya existe
  miPrimerMapa["excelenteDesarrollador"] = false;
  print("Mapa: ${miPrimerMapa}");
  print("Longitud: ${miPrimerMapa.length}");

  var lista = ["David", "Patricia", "Felipe"];
  print("Lista convertida en mapa: ${lista.asMap()}");
}
