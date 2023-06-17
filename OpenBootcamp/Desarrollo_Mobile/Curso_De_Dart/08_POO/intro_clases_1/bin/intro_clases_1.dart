import 'package:test/test.dart';

import 'galleta_de_gengibre.dart';

void main(List<String> arguments) {
  GalletaDeJengibre tom = GalletaDeJengibre("Tom", 27);
  
  String nombreTom = tom.name!;
  int edadTom = tom.getEdad;

  print("\nNombre: $nombreTom"
        "\nEdad: $edadTom");

  GalletaDeJengibre mary = GalletaDeJengibre("Mary", 27);
  
  String nombreMary = mary.name!;
  mary.setEdad = 25;
  int edadMary = mary.getEdad;

  print("\nNombre: $nombreMary"
        "\nEdad: $edadMary");

  GalletaDeJengibre jerry = GalletaDeJengibre.avanzada("Jerry", 27, tipo: "Sin gluten", volteretas: false);

  String nombreJerry = jerry.name!;
  int edadJerry = jerry.getEdad;
  String tipoJerry = jerry.tipo!;
  bool volteretas = jerry.volteretas!;

  volteretas? print("\nNombre: $nombreJerry"
                    "\nEdad: $edadJerry"
                    "\nTipo: $tipoJerry"
                    "\nSabe dar volteretas?: Sí") : 
              print("\nNombre: $nombreJerry"
                    "\nEdad: $edadJerry"
                    "\nTipo: $tipoJerry"
                    "\nSabe dar volteretas?: No");

  // GalletaDeJengibre mary = GalletaDeJengibre.sinDatos();

  // Volteretas
  bool volteretaTom = tom.getVolteretas;
  bool volteretaMary = mary.getVolteretas;
  bool volteretaJerry = jerry.getVolteretas;

  volteretaTom ? print("Tom ha aprendido") : print("Tom no ha aprendido");
  volteretaMary ? print("Mary ha aprendido") : print("Mary no ha aprendido");
  volteretaJerry ? print("Jerry ha aprendido") : print("Jerry no ha aprendido");
}
