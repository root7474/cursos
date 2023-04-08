enum EstadoUsuario { notLogged, logged, logging, registering }

void main(List<String> arguments) {
  var usuarioEstadoActual = EstadoUsuario.notLogged;
  print("Estado usuario: ${usuarioEstadoActual}");

  // Aquí pasa algo y se loggea
  usuarioEstadoActual = EstadoUsuario.logged;
  print("Estado usario: ${usuarioEstadoActual}");
}
