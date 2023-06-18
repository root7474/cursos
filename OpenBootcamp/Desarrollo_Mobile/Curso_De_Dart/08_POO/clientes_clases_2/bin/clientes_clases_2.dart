import 'personas.dart';
import 'direccion.dart';

void main(List<String> arguments) {
  Direccion direccion = Direccion(1, "Las cuadras", "520001", "San Juan de Pasto");
  Personas david = Personas("David", edad: 27, direccion: direccion, telefono: "3167002210");

  print("Diredcción: ${david.direccion!.getCodPostal}"
        "\nCiudad: ${david.direccion!.getCiudad}");
  
  david.direccion!.setCiudad = "Ipiales";

  print("Diredcción: ${david.direccion!.getCodPostal}"
        "\nCiudad: ${david.direccion!.getCiudad}");
}
