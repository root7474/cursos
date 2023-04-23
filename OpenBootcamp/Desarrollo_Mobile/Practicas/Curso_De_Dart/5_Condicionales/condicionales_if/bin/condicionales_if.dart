void main(List<String> arguments) {
  var cielo = "Azúl";
  var hora = 10;

  // if()
  if (cielo == "Azúl" && hora >= 6) {
    // print("Entonces es de día");
  }

  if (true) {
    // print("Me estoy ejecutando");
  }

  // else
  var numero = 6;

  if (numero % 2 == 0) {
    // print("El número ${numero} es par");
  } else {
    // print("El número ${numero} es impar");
  }

  var davidCanta = true;

  if (davidCanta) {
    // print("David canta, correeeeee!!!");
  } else {
    // print("No, pero corre cunado lo haga");
  }

  // if... else
  // Detector de milenials 1981 - 1997
  var anioDeNacimiento = 1996;
  var genero = "Hombre";

  if (anioDeNacimiento < 1981) {
    print("No hay milenials a la vista");
  } else if (anioDeNacimiento > 1997) {
    print("No hay milenials a la vista");
  } else {
    if (genero == "Hombre") print("Eres milenial hombre");
    if (genero == "Mujer") print("Eres milenial mujer");
    if (genero == "Otro") print("Eres un milenial sin un genero reconocido!!!");
  }
}
