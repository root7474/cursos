enum EstadoUsuario { notLogged, logged, logging, registering }

void main(List<String> arguments) {
  var estadoActual = EstadoUsuario.notLogged;
  print("Estado actual: ${estadoActual}");

  // Aquí pasa algo yse loggea
  estadoActual = EstadoUsuario.logged;
  print("Estado actual: ${estadoActual}");
}
